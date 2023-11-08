"""Tests for object_detection.core.config module."""
from pathlib import Path

from object_detection.core.config import Config

TEST_SETTINGS_PATH = Path("tests/core/settings.test.yaml")
EMPTY_SETTINGS_PATH = Path("test/core/empty-settings.test.yaml")


def test_default_variables():
    config = Config(config_path=EMPTY_SETTINGS_PATH)
    assert config.dataset_file_format == "png"
    assert config.file_count_threshold == 20
    assert config.dataset_split == 0.2


def test_load():
    config = Config(config_path=TEST_SETTINGS_PATH)
    assert config.dataset_file_format == "txt"
    assert config.file_count_threshold == 100
