import dataclasses
from pathlib import Path

from object_detection.core.utils import load_yaml_dict

DEFAULT_CONFIG_PATH = Path("settings.yaml")
DEFAULT_DATA_SOURCE_PATH = Path("data_source")


@dataclasses.dataclass
class Config:
    """
    Holds all object-detection settings defined by user in settings.yaml file.
    """

    config_path: dataclasses.InitVar[Path]
    data_source: Path = DEFAULT_DATA_SOURCE_PATH

    dataset_file_format: str = "png"
    file_count_threshold: int = 20

    dataset_split: float = 0.2

    def __post_init__(self, config_path: Path):
        """Load data from conifg file."""
        if config_path:
            try:
                data = load_yaml_dict(config_path)
            except ValueError:
                data = {}

            for field, value in data.items():
                if hasattr(self, field):
                    setattr(self, field, value)


config = Config(config_path=DEFAULT_CONFIG_PATH)
