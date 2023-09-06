"""Fixtures for tests.format"""

import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def valid_base(tmp_path_factory):
    """Prepare a valid base directory."""
    base: Path = tmp_path_factory.mktemp("root")

    (label1 := (base / "label1")).mkdir()
    (label1 / "file1.txt").touch()
    (label1 / "file2.txt").touch()

    (label2 := (base / "label2")).mkdir()
    (label2 / "file1.txt").touch()
    (label2 / "file2.txt").touch()

    return base


@pytest.fixture(scope="session")
def dir_with_only_files(valid_base):
    return valid_base / "label1"


@pytest.fixture(scope="session")
def multiple_formats(valid_base):
    ((dir := (valid_base / "label2")) / "file3.yaml").touch()
    return dir
