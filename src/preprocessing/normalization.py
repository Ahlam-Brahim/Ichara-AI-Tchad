"""
Normalization utilities for Ichara AI Tchad.

This module provides reusable functions for preparing numerical
features before machine-learning experiments.
"""

from __future__ import annotations

import numpy as np


def min_max_normalize(
    values: np.ndarray,
    feature_min: float = 0.0,
    feature_max: float = 1.0,
) -> np.ndarray:
    """
    Scale values to a specified range.

    Args:
        values: Input numerical array.
        feature_min: Lower bound of the target range.
        feature_max: Upper bound of the target range.

    Returns:
        Normalized NumPy array.
    """
    values = np.asarray(values, dtype=np.float32)

    if feature_min >= feature_max:
        raise ValueError(
            "feature_min must be smaller than feature_max."
        )

    if values.size == 0:
        return values.copy()

    value_min = np.min(values)
    value_max = np.max(values)

    if value_max == value_min:
        return np.full_like(
            values,
            feature_min,
            dtype=np.float32,
        )

    normalized = (
        (values - value_min)
        / (value_max - value_min)
    )

    return (
        normalized * (feature_max - feature_min)
        + feature_min
    ).astype(np.float32)


def standardize(values: np.ndarray) -> np.ndarray:
    """
    Standardize values using mean and standard deviation.

    Formula:

        z = (x - mean) / standard_deviation

    Args:
        values: Input numerical array.

    Returns:
        Standardized NumPy array.
    """
    values = np.asarray(values, dtype=np.float32)

    if values.size == 0:
        return values.copy()

    mean = np.mean(values)
    std = np.std(values)

    if std == 0:
        return np.zeros_like(values, dtype=np.float32)

    return ((values - mean) / std).astype(np.float32)
