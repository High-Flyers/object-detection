"""Module for utility functions"""
import yaml
import yaml.parser
import yaml.scanner
from pathlib import Path
from typing import Optional, Dict, Any


def load_yaml_dict(path: Path) -> Optional[Dict[str, Any]]:
    """Load yaml file into dict."""
    if not path.is_file():
        raise ValueError(f"{path=} is not a file.")

    with open(path) as file:
        try:
            data = yaml.safe_load(file) or {}
        except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
            raise ValueError(f"{path} is not a valid YAML file: {str(e)}")

    if not isinstance(data, dict):
        raise ValueError(f"{path} should be a dictionary.")

    return data
