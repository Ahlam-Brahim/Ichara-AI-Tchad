"""
Geometric feature extraction for Ichara AI Tchad.

This module provides utilities for calculating distances and angles
between hand landmarks.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np


def _to_array(
    landmarks: Iterable[tuple[float, float, float]],
) -> np.ndarray:
    """Convert landmarks to a NumPy array."""
    points = np.asarray(list(landmarks), dtype=np.float32)

    if points.size == 0:
        return np.empty((0, 3), dtype=np.float32)

    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("Landmarks must have the shape (N, 3).")

    return points


def euclidean_distance(
    point_a: Iterable[float],
    point_b: Iterable[float],
) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        point_a: First point.
        point_b: Second point.

    Returns:
        Euclidean distance.
    """
    a = np.asarray(list(point_a), dtype=np.float32)
    b = np.asarray(list(point_b), dtype=np.float32)

    if a.shape != b.shape:
        raise ValueError("Points must have the same dimensions.")

    return float(np.linalg.norm(a - b))


def angle_between(
    point_a: Iterable[float],
    point_b: Iterable[float],
    point_c: Iterable[float],
) -> float:
    """
    Calculate the angle ABC in degrees.

    Point B is the vertex of the angle.

    Args:
        point_a: First point.
        point_b: Vertex point.
        point_c: Third point.

    Returns:
        Angle in degrees.
    """
    a = np.asarray(list(point_a), dtype=np.float32)
    b = np.asarray(list(point_b), dtype=np.float32)
    c = np.asarray(list(point_c), dtype=np.float32)

    vector_ba = a - b
    vector_bc = c - b

    norm_ba = np.linalg.norm(vector_ba)
    norm_bc = np.linalg.norm(vector_bc)

    if norm_ba == 0 or norm_bc == 0:
        return 0.0

    cosine = np.dot(vector_ba, vector_bc) / (
        norm_ba * norm_bc
    )

    cosine = np.clip(cosine, -1.0, 1.0)

    return float(np.degrees(np.arccos(cosine)))


def landmark_distances(
    landmarks: Iterable[tuple[float, float, float]],
) -> np.ndarray:
    """
    Calculate distances from the wrist to every landmark.

    The first landmark is assumed to represent the wrist.

    Args:
        landmarks: Hand landmarks.

    Returns:
        One-dimensional array of distances.
    """
    points = _to_array(landmarks)

    if len(points) == 0:
        return np.empty(0, dtype=np.float32)

    wrist = points[0]

    distances = np.linalg.norm(points - wrist, axis=1)

    return distances.astype(np.float32)


def selected_distances(
    landmarks: Iterable[tuple[float, float, float]],
    pairs: Iterable[tuple[int, int]],
) -> np.ndarray:
    """
    Calculate distances for selected landmark pairs.

    Args:
        landmarks: Hand landmarks.
        pairs: Pairs of landmark indices.

    Returns:
        Array containing the requested distances.
    """
    points = _to_array(landmarks)

    if len(points) == 0:
        return np.empty(0, dtype=np.float32)

    distances = []

    for index_a, index_b in pairs:
        if not (
            0 <= index_a < len(points)
            and 0 <= index_b < len(points)
        ):
            raise IndexError("Landmark index is out of range.")

        distances.append(
            euclidean_distance(
                points[index_a],
                points[index_b],
            )
        )

    return np.asarray(distances, dtype=np.float32)


def selected_angles(
    landmarks: Iterable[tuple[float, float, float]],
    triplets: Iterable[tuple[int, int, int]],
) -> np.ndarray:
    """
    Calculate angles for selected landmark triplets.

    Each triplet is represented as (A, B, C), where B is
    the vertex of the angle ABC.

    Args:
        landmarks: Hand landmarks.
        triplets: Landmark triplets.

    Returns:
        Array containing the requested angles in degrees.
    """
    points = _to_array(landmarks)

    if len(points) == 0:
        return np.empty(0, dtype=np.float32)

    angles = []

    for index_a, index_b, index_c in triplets:
        if not (
            0 <= index_a < len(points)
            and 0 <= index_b < len(points)
            and 0 <= index_c < len(points)
        ):
            raise IndexError("Landmark index is out of range.")

        angles.append(
            angle_between(
                points[index_a],
                points[index_b],
                points[index_c],
            )
        )

    return np.asarray(angles, dtype=np.float32)
