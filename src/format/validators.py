"""Validators of the data provided by user."""

from pathlib import Path
import re

from src.core.config import config


def validate_dataset(
    dataset_dir: Path,
    threshold: int = config.file_count_threshold,
    file_format: str = config.dataset_file_format,
) -> bool:
    """Return True if dataset is valid."""
    if _contains_only_directories(dataset_dir):
        return all(
            _contains_only_files(name)
            and _contains_only_specified_format(name, file_format)
            and _validate_enough_files(name, threshold)
            for name in dataset_dir.iterdir()
        )
    return False


def _contains_only_directories(parent: Path) -> bool:
    """Returns True if there are no files inside parent directory."""
    return not any(elem.is_file() for elem in parent.iterdir())


def _contains_only_files(parent: Path) -> bool:
    """Returns True if there are no directories inside parent directory."""
    return not any(elem.is_dir() for elem in parent.iterdir())


def _contains_only_specified_format(parent: Path, format: str) -> bool:
    """Returns Ture if there are only image files inside parent directory."""
    return all(re.fullmatch(f"^.+\.{format}$", elem.name) for elem in parent.iterdir())


def _validate_enough_files(dir: Path, threshold: int) -> bool:
    """Returns True if there are enough image files inside directory."""
    if threshold <= 0:
        raise ValueError(f"{threshold=} should be a positive number")
    return len(list(dir.iterdir())) >= threshold
