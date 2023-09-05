"""Tests for core.config module."""
from pathlib import Path

from src.core.config import Config

TEST_SETTINGS_PATH = Path("tests/core/settings.test.yaml")


def test_default_variables():
    config = Config()
    assert config.dataset_file_format == "jpg"
    assert config.file_count_threshold == 20


def test_load():
    config = Config(config_path=TEST_SETTINGS_PATH)
    assert config.dataset_file_format == "txt"
    assert config.file_count_threshold == 100
