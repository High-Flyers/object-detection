"""Tests for object_detection.format.validators module."""
import pytest
import object_detection.format.validators as v


@pytest.mark.parametrize(
    "parent, expected",
    [
        ("valid_base", True),
        ("dir_with_only_files", False),
    ],
)
def test_contains_only_directories(parent, expected, request):
    parent = request.getfixturevalue(parent)
    assert v.contains_only_directories(parent) == expected


@pytest.mark.parametrize(
    "parent, expected",
    [
        ("dir_with_only_files", True),
        ("valid_base", False),
    ],
)
def test_contains_only_files(parent, expected, request):
    parent = request.getfixturevalue(parent)
    assert v.contains_only_files(parent) == expected


@pytest.mark.parametrize(
    "parent, expected",
    [
        ("dir_with_only_files", True),
        ("multiple_formats", False),
    ],
)
def test_contains_only_specified_format(parent, expected, request):
    parent = request.getfixturevalue(parent)
    assert v.contains_only_specified_format(parent, "txt") == expected


@pytest.mark.parametrize(
    "threshold, expected",
    [
        (1, True),
        (2, True),
        (3, False),
    ],
)
def test_validate_enough_files(threshold, expected, request):
    dir = request.getfixturevalue("dir_with_only_files")
    assert v.validate_enough_files(dir, threshold) == expected


@pytest.mark.parametrize(
    "threshold",
    [
        0,
        -1,
    ],
)
def test_validate_enough_files_raises_exception(threshold, request):
    dir = request.getfixturevalue("dir_with_only_files")
    with pytest.raises(ValueError):
        v.validate_enough_files(dir, threshold)
