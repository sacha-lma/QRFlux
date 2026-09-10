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


def Clean() -> None:
    """Recursively remove Python caches and build artifacts."""
    Targets: list[Path] = []

    for Item in ROOT.rglob("*"):
        if _SKIP_DIRS.intersection(Item.parts):
            continue
        if Item.is_dir() and Item.name in _CACHE_DIRS:
            Targets.append(Item)
        elif Item.is_file() and Item.suffix in _CACHE_FILE_SUFFIXES:
            Targets.append(Item)

    for Pattern in _CACHE_GLOBS:
        Targets.extend(
            Item for Item in ROOT.rglob(Pattern) if not _SKIP_DIRS.intersection(Item.parts)
        )

    for Item in dict.fromkeys(Targets):
        if Item.is_dir():
            shutil.rmtree(Item, ignore_errors=True)
        elif Item.exists():
            Item.unlink()

    print(f"clean: removed {len(set(Targets))} item(s)")
