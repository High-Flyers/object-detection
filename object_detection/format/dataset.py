"""Module for dataset transformation"""
from pathlib import Path
from typing import Literal

import tensorflow as tf
from tensorflow import keras as keras

from object_detection.core.config import config
from object_detection.format.validators import (
    contains_only_directories,
    contains_only_files,
    contains_only_specified_format,
    validate_enough_files,
)

Subset = Literal["training"] | Literal["validation"]


def create_dataset(src: Path, subset: Subset) -> tf.data.Dataset:
    """Creates datasets, standardizes it and optimizes for performance."""
    try:
        if validate_dataset_source(src):
            dataset: tf.data.Dataset = keras.utils.image_dataset_from_directory(
                src,
                validation_split=config.dataset_split,
                subset=subset,
                labels="inferred",
            )
            dataset = standardize_dataset(dataset)
            dataset = dataset.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
            return dataset
    except ValueError as e:
        print(f"Source directory is invalid: {e}")


def validate_dataset_source(
    dataset_dir: Path,
    threshold: int = config.file_count_threshold,
    file_format: str = config.dataset_file_format,
) -> bool:
    """Return True if dataset's source is valid."""
    try:
        if contains_only_directories(dataset_dir):
            return all(
                contains_only_files(name)
                and contains_only_specified_format(name, file_format)
                and validate_enough_files(name, threshold)
                for name in dataset_dir.iterdir()
            )
        return False
    except ValueError as e:
        raise ValueError(e)


def standardize_dataset(dataset: tf.data.Dataset) -> tf.data.Dataset:
    """Normalizes RGB values to be in [0, 1] range and returns standardized dataset"""
    normalization_layer = keras.layers.Rescaling(1.0 / 255)
    normalized_ds = dataset.map(lambda x, y: (normalization_layer(x), y))
    return normalized_ds
