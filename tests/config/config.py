import pytest
from src.config.config import Config

class TestConfig:
    def test_default_variables():
        config = Config()
        assert config.dataset_file_format == "jpg"
        assert config.file_count_threshold == 20