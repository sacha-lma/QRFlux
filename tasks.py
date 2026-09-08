"""Utility tasks invoked by poethepoet (works on Windows/macOS/Linux)."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).parent

_SKIP_DIRS = {".git", ".venv", "venv", ".env"}
_CACHE_DIRS = {
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".pytype",
    "build",
    "dist",
}
_CACHE_FILE_SUFFIXES = {".pyc", ".pyo", ".pyd"}
_CACHE_GLOBS = ("*.egg-info", "*.coverage", ".coverage")


def clean() -> None:
    """Recursively remove Python caches and build artifacts."""
    targets: list[Path] = []

    for path in ROOT.rglob("*"):
        if _SKIP_DIRS.intersection(path.parts):
            continue
        if path.is_dir() and path.name in _CACHE_DIRS:
            targets.append(path)
        elif path.is_file() and path.suffix in _CACHE_FILE_SUFFIXES:
            targets.append(path)

    for pattern in _CACHE_GLOBS:
        targets.extend(
            p for p in ROOT.rglob(pattern) if not _SKIP_DIRS.intersection(p.parts)
        )

    for path in dict.fromkeys(targets):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        elif path.exists():
            path.unlink()

    print(f"clean: removed {len(set(targets))} item(s)")
