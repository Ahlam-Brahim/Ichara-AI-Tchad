"""
Tests for geometric feature extraction.

Ichara AI Tchad
"""

import numpy as np
import pytest

from src.features.geometry import (
    angle_between,
    euclidean_distance,
    landmark_distances,
    selected_angles,
    selected_distances,
)


@pytest.fixture
def sample_landmarks():
    """Provide sample landmarks for geometric tests."""
    return [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
    ]


def test_euclidean_distance():
    """Distance between (0, 0) and (3, 4) should be 5."""
    result = euclidean_distance(
        (0.0, 0.0),
        (3.0, 4.0),
    )

    assert np.isclose(result, 5.0)


def test_euclidean_distance_3d():
    """Distance should also work with 3D points."""
    result = euclidean_distance(
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 1.0),
    )

    assert np.isclose(result, np.sqrt(3))


def test_angle_between():
    """The angle ABC should be 90 degrees."""
    result = angle_between(
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
    )

    assert np.isclose(result, 90.0)


def test_angle_between_straight_line():
    """The angle should be 180 degrees."""
    result = angle_between(
        (-1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    )

    assert np.isclose(result, 180.0)


def test_zero_length_angle():
    """A zero-length vector should return 0 degrees."""
    result = angle_between(
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    )

    assert result == 0.0


def test_landmark_distances(sample_landmarks):
    """Distances should be calculated relative to the wrist."""
    result = landmark_distances(sample_landmarks)

    assert isinstance(result, np.ndarray)
    assert result.shape == (4,)
    assert np.isclose(result[0], 0.0)
    assert np.isclose(result[1], 1.0)
    assert np.isclose(result[2], np.sqrt(2))


def test_empty_landmark_distances():
    """Empty landmarks should return an empty array."""
    result = landmark_distances([])

    assert isinstance(result, np.ndarray)
    assert result.shape == (0,)


def test_selected_distances(sample_landmarks):
    """Selected landmark pairs should return expected distances."""
    pairs = [
        (0, 1),
        (0, 2),
        (1, 2),
    ]

    result = selected_distances(
        sample_landmarks,
        pairs,
    )

    assert result.shape == (3,)
    assert np.isclose(result[0], 1.0)
    assert np.isclose(result[1], np.sqrt(2))
    assert np.isclose(result[2], 1.0)


def test_invalid_distance_index(sample_landmarks):
    """Invalid landmark indices should raise IndexError."""
    with pytest.raises(IndexError):
        selected_distances(
            sample_landmarks,
            [(0, 10)],
        )


def test_selected_angles(sample_landmarks):
    """Selected landmark triplets should return expected angles."""
    triplets = [
        (1, 0, 3),
    ]

    result = selected_angles(
        sample_landmarks,
        triplets,
    )

    assert result.shape == (1,)
    assert np.isclose(result[0], 90.0)


def test_invalid_angle_index(sample_landmarks):
    """Invalid landmark indices should raise IndexError."""
    with pytest.raises(IndexError):
        selected_angles(
            sample_landmarks,
            [(0, 1, 10)],
        )
