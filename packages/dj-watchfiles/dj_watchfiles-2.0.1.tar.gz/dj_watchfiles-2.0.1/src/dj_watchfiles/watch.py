from __future__ import annotations

import logging
import threading
from collections.abc import Generator, Iterable
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Callable

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import autoreload
from django.utils.autoreload import run_with_reloader
from django.utils.module_loading import import_string
from typing_extensions import ParamSpec
from watchfiles import Change, watch

P = ParamSpec("P")


class MutableWatcher:
    """
    Watchfiles doesn't give us a way to adjust watches at runtime, but it does
    give us a way to stop the watcher when a condition is set.

    This class wraps this to provide a single iterator that may replace the
    underlying watchfiles iterator when roots are added or removed.
    """

    def __init__(
        self, filter: Callable[[Change, str], bool], watchfiles_settings: dict[str, Any]
    ) -> None:
        self.change_event = threading.Event()
        self.stop_event = threading.Event()
        self.roots: set[Path] = set()
        self.filter = filter
        self.watchfiles_settings = watchfiles_settings

    def set_roots(self, roots: set[Path]) -> None:
        if roots != self.roots:
            self.roots = roots
            self.change_event.set()

    def stop(self) -> None:
        self.stop_event.set()

    def __iter__(self) -> Generator[set[tuple[Change, str]]]:
        while True:
            if self.stop_event.is_set():
                return
            self.change_event.clear()
            watch_kwargs = {
                "watch_filter": self.filter,
                "stop_event": self.stop_event,
                "debounce": False,
                "rust_timeout": 100,
                "yield_on_timeout": True,
                **self.watchfiles_settings,
            }

            for changes in watch(*self.roots, **watch_kwargs):
                if self.change_event.is_set():
                    break
                yield changes


class WatchfilesReloader(autoreload.BaseReloader):
    def __init__(self, watchfiles_settings: dict[str, Any]) -> None:
        self.watchfiles_settings = watchfiles_settings
        self.watcher = MutableWatcher(self.file_filter, watchfiles_settings)
        self.watched_files_set: set[Path] = set()
        super().__init__()

    def file_filter(self, change: Change, filename: str) -> bool:
        path = Path(filename)
        if path in self.watched_files_set:
            return True
        for directory, globs in self.directory_globs.items():
            try:
                relative_path = path.relative_to(directory)
            except ValueError:
                pass
            else:
                relative_path_str = str(relative_path)
                for glob in globs:
                    if fnmatch(relative_path_str, glob):
                        return True
        return False

    def watched_roots(self, watched_files: Iterable[Path]) -> frozenset[Path]:
        # Adapted from WatchmanReloader
        extra_directories = self.directory_globs.keys()
        watched_file_dirs = {f.parent for f in watched_files}
        sys_paths = set(autoreload.sys_path_directories())
        all_dirs = (*extra_directories, *watched_file_dirs, *sys_paths)
        existing_dirs = (p for p in all_dirs if p.exists())
        return frozenset(existing_dirs)

    def tick(self) -> Generator[None]:
        self.watched_files_set = set(self.watched_files(include_globs=False))
        roots = set(
            autoreload.common_roots(
                self.watched_roots(self.watched_files_set),
            )
        )
        self.watcher.set_roots(roots)

        for changes in self.watcher:  # pragma: no branch
            for _, path in changes:  # pragma: no cover
                self.notify_file_changed(Path(path))
            yield


def replaced_run_with_reloader(
    main_func: Callable[..., Any], *args: P.args, **kwargs: P.kwargs
) -> int | None:
    try:
        watchfiles_settings = getattr(settings, "WATCHFILES", {}).copy()
    except (ImproperlyConfigured, AttributeError):  # pragma: no cover
        watchfiles_settings = {}  # pragma: no cover

    if "watch_filter" in watchfiles_settings:
        try:
            watchfiles_settings["watch_filter"] = import_string(
                watchfiles_settings["watch_filter"]
            )()
        except (AttributeError, ValueError) as exc:  # pragma: no cover
            logging.warning(  # pragma: no cover
                f"Failed to import watch_filter '{watchfiles_settings['watch_filter']}': {exc}"
            )
            watchfiles_settings.pop("watch_filter")  # pragma: no cover

    settings_verbosity = watchfiles_settings.pop("verbosity", None)

    if watchfiles_settings.get("debug"):
        log_level = logging.DEBUG
    else:
        verbosity = settings_verbosity or kwargs.get("verbosity", 1)
        log_level = 40 - 10 * verbosity

    watchfiles_settings["debug"] = log_level == logging.DEBUG
    logging.getLogger("watchfiles").setLevel(log_level)
    autoreload.get_reloader = lambda: WatchfilesReloader(watchfiles_settings)

    return run_with_reloader(main_func, *args, **kwargs)


autoreload.run_with_reloader = replaced_run_with_reloader
