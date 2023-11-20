"""Tests for object_detection.core.config module."""
from pathlib import Path

import pytest

from object_detection.core.config import Config
from object_detection.core.exceptions import RequiredFieldException

TEST_SETTINGS_PATH = Path("tests/core/test_config_files/settings.test.yaml")
EMPTY_SETTINGS_PATH = Path("tests/core/test_config_files/empty-settings.test.yaml")
ONLY_REQUIRED_SETTINGS_PATH = Path(
    "tests/core/test_config_files/only-required-settings.test.yaml"
)


def test_default_variables():
    config = Config(config_path=ONLY_REQUIRED_SETTINGS_PATH)
    assert config.dataset_file_format == "png"
    assert config.file_count_threshold == 20
    assert config.dataset_split == 0.2


def test_load():
    config = Config(config_path=TEST_SETTINGS_PATH)
    assert config.dataset_file_format == "txt"
    assert config.file_count_threshold == 100


def test_validates_required_fields():
    with pytest.raises(RequiredFieldException):
        Config(config_path=EMPTY_SETTINGS_PATH)
