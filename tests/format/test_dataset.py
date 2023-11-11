"""Tests for object_detection.format.dataset module."""
import pytest

from object_detection.format.dataset import (create_dataset,
                                             validate_dataset_source)


@pytest.mark.parametrize(
    "dataset_dir, expected",
    [
        ("valid_base", True),
        ("dir_with_only_files", False),
    ],
)
def test_validate_dataset(dataset_dir, expected, request):
    dataset = request.getfixturevalue(dataset_dir)
    assert validate_dataset_source(dataset, 2, "txt") == expected
