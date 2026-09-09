"""
Prepare landmark data for machine-learning experiments.

Ichara AI Tchad

This script reads extracted landmarks from a CSV file, converts them
into numerical features, validates the data, and creates a dataset
that can be used by machine-learning experiments.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

from src.utils.logger import get_logger
from src.utils.paths import LANDMARKS_DIR, PROCESSED_DATA_DIR


logger = get_logger(__name__)

INPUT_FILE = LANDMARKS_DIR / "landmarks.csv"
OUTPUT_FEATURES = PROCESSED_DATA_DIR / "features.npy"
OUTPUT_LABELS = PROCESSED_DATA_DIR / "labels.npy"


def parse_landmarks(value: str) -> np.ndarray:
    """
    Convert a serialized landmark string into a numerical array.

    Args:
        value: Space-separated landmark coordinates.

    Returns:
        NumPy array of float32 values.
    """
    if not value.strip():
        raise ValueError("Empty landmark value.")

    values = np.fromstring(
        value,
        sep=" ",
        dtype=np.float32,
    )

    if values.size == 0:
        raise ValueError("Invalid landmark data.")

    if values.size % 3 != 0:
        raise ValueError(
            "Landmark data must contain groups of x, y, z values."
        )

    return values


def load_landmark_dataset(
    input_file: Path,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Load landmarks and labels from a CSV file.

    Args:
        input_file: Path to the landmark CSV.

    Returns:
        Tuple containing features and labels.
    """
    if not input_file.exists():
        raise FileNotFoundError(
            f"Landmark file not found: {input_file}"
        )

    features = []
    labels = []

    with input_file.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        required_columns = {
            "label",
            "landmarks",
        }

        if not required_columns.issubset(
            reader.fieldnames or []
        ):
            raise ValueError(
                "Input CSV must contain 'label' and 'landmarks' columns."
            )

        for row_number, row in enumerate(
            reader,
            start=2,
        ):
            try:
                landmark_values = parse_landmarks(
                    row["landmarks"]
                )

                features.append(landmark_values)
                labels.append(row["label"])

            except (ValueError, KeyError) as error:
                logger.warning(
                    "Skipping row %d: %s",
                    row_number,
                    error,
                )

    if not features:
        return (
            np.empty((0, 0), dtype=np.float32),
            np.empty((0,), dtype=str),
        )

    feature_lengths = {
        len(feature)
        for feature in features
    }

    if len(feature_lengths) != 1:
        raise ValueError(
            "All samples must contain the same number of features."
        )

    feature_array = np.asarray(
        features,
        dtype=np.float32,
    )

    label_array = np.asarray(
        labels,
        dtype=str,
    )

    return feature_array, label_array


def validate_dataset(
    features: np.ndarray,
    labels: np.ndarray,
) -> None:
    """
    Validate the prepared dataset.

    Args:
        features: Feature matrix.
        labels: Label array.

    Raises:
        ValueError: If the dataset is invalid.
    """
    if features.ndim != 2:
        raise ValueError(
            "Features must be a 2-dimensional array."
        )

    if labels.ndim != 1:
        raise ValueError(
            "Labels must be a 1-dimensional array."
        )

    if len(features) != len(labels):
        raise ValueError(
            "Features and labels must contain the same number of samples."
        )

    if len(features) == 0:
        raise ValueError(
            "Dataset is empty."
        )

    if not np.isfinite(features).all():
        raise ValueError(
            "Features contain NaN or infinite values."
        )


def save_dataset(
    features: np.ndarray,
    labels: np.ndarray,
    features_path: Path = OUTPUT_FEATURES,
    labels_path: Path = OUTPUT_LABELS,
) -> None:
    """
    Save prepared features and labels.

    Args:
        features: Feature matrix.
        labels: Label array.
        features_path: Destination for features.
        labels_path: Destination for labels.
    """
    features_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    np.save(features_path, features)
    np.save(labels_path, labels)

    logger.info(
        "Features saved to: %s",
        features_path,
    )

    logger.info(
        "Labels saved to: %s",
        labels_path,
    )


def prepare_dataset(
    input_file: Path = INPUT_FILE,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Prepare the landmark dataset.

    Args:
        input_file: Path to the landmark CSV file.

    Returns:
        Prepared features and labels.
    """
    logger.info(
        "Loading landmark dataset: %s",
        input_file,
    )

    features, labels = load_landmark_dataset(
        input_file
    )

    validate_dataset(
        features,
        labels,
    )

    logger.info(
        "Dataset contains %d samples.",
        len(labels),
    )

    logger.info(
        "Number of features: %d",
        features.shape[1],
    )

    logger.info(
        "Number of classes: %d",
        len(np.unique(labels)),
    )

    save_dataset(
        features,
        labels,
    )

    return features, labels


if __name__ == "__main__":
    prepare_dataset()
