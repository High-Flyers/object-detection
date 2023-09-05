"""Validators of the data provided by user."""

from pathlib import Path
import re


def contains_only_directories(parent: Path) -> bool:
    """Returns True if there are no files inside parent directory."""
    return not any(elem.is_file() for elem in parent.iterdir())


def contains_only_files(parent: Path) -> bool:
    """Returns True if there are no directories inside parent directory."""
    return not any(elem.is_dir() for elem in parent.iterdir())


def contains_only_specified_format(parent: Path, format: str) -> bool:
    """Returns Ture if there are only image files inside parent directory."""
    return all(re.fullmatch(f"^.+\.{format}$", elem.name) for elem in parent.iterdir())


def validate_enough_files(dir: Path, threshold: int) -> bool:
    """Returns True if there are enough image files inside directory."""
    if threshold <= 0:
        raise ValueError(f"{threshold=} should be a positive number")
    return len(list(dir.iterdir())) >= threshold
