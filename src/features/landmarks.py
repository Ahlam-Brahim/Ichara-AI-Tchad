"""
Landmark feature processing for Ichara AI Tchad.

This module contains utilities for transforming hand landmarks
into machine-learning-ready numerical features.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np


def landmarks_to_array(
    landmarks: Iterable[tuple[float, float, float]],
) -> np.ndarray:
    """
    Convert hand landmarks into a NumPy array.

    Args:
        landmarks: Iterable containing (x, y, z) coordinates.

    Returns:
        NumPy array with shape (N, 3).
    """
    array = np.asarray(list(landmarks), dtype=np.float32)

    if array.size == 0:
        return np.empty((0, 3), dtype=np.float32)

    if array.ndim != 2 or array.shape[1] != 3:
        raise ValueError(
            "Landmarks must have the shape (N, 3)."
        )

    return array


def normalize_landmarks(
    landmarks: Iterable[tuple[float, float, float]],
) -> np.ndarray:
    """
    Normalize hand landmarks relative to the wrist.

    The wrist is assumed to be the first landmark.

    The normalization reduces the influence of the absolute
    position of the hand in the camera frame.

    Args:
        landmarks: Iterable containing (x, y, z) coordinates.

    Returns:
        Normalized landmarks as a NumPy array.
    """
    points = landmarks_to_array(landmarks)

    if len(points) == 0:
        return points

    wrist = points[0].copy()

    normalized = points - wrist

    scale = np.max(np.linalg.norm(normalized[:, :2], axis=1))

    if scale > 0:
        normalized = normalized / scale

    return normalized.astype(np.float32)


def flatten_landmarks(
    landmarks: Iterable[tuple[float, float, float]],
    normalize: bool = True,
) -> np.ndarray:
    """
    Convert landmarks into a one-dimensional feature vector.

    Args:
        landmarks: Iterable containing (x, y, z) coordinates.
        normalize: Whether to normalize the landmarks first.

    Returns:
        One-dimensional NumPy feature vector.
    """
    if normalize:
        points = normalize_landmarks(landmarks)
    else:
        points = landmarks_to_array(landmarks)

    return points.flatten().astype(np.float32)
