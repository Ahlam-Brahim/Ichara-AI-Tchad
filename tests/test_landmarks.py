"""
Tests for landmark feature processing.

Ichara AI Tchad
"""

import numpy as np
import pytest

from src.features.landmarks import (
    flatten_landmarks,
    landmarks_to_array,
    normalize_landmarks,
)


@pytest.fixture
def sample_landmarks():
    """Provide a small set of sample hand landmarks."""
    return [
        (0.50, 0.50, 0.00),
        (0.55, 0.45, 0.01),
        (0.60, 0.40, 0.02),
        (0.65, 0.35, 0.03),
    ]


def test_landmarks_to_array(sample_landmarks):
    """Landmarks should be converted to an (N, 3) array."""
    result = landmarks_to_array(sample_landmarks)

    assert isinstance(result, np.ndarray)
    assert result.shape == (4, 3)
    assert result.dtype == np.float32


def test_empty_landmarks():
    """Empty landmarks should return an empty (0, 3) array."""
    result = landmarks_to_array([])

    assert isinstance(result, np.ndarray)
    assert result.shape == (0, 3)


def test_invalid_landmark_shape():
    """Invalid landmark dimensions should raise ValueError."""
    invalid_landmarks = [
        (0.1, 0.2),
        (0.3, 0.4),
    ]

    with pytest.raises(ValueError):
        landmarks_to_array(invalid_landmarks)


def test_normalize_landmarks(sample_landmarks):
    """Normalization should place the wrist at the origin."""
    result = normalize_landmarks(sample_landmarks)

    assert result.shape == (4, 3)
    assert np.allclose(result[0], [0.0, 0.0, 0.0])


def test_normalize_empty_landmarks():
    """Normalization should support empty input."""
    result = normalize_landmarks([])

    assert result.shape == (0, 3)


def test_flatten_landmarks(sample_landmarks):
    """Flattening should produce a one-dimensional feature vector."""
    result = flatten_landmarks(sample_landmarks)

    assert isinstance(result, np.ndarray)
    assert result.ndim == 1
    assert result.shape == (12,)


def test_flatten_without_normalization(sample_landmarks):
    """Flattening can be performed without normalization."""
    result = flatten_landmarks(
        sample_landmarks,
        normalize=False,
    )

    assert result.shape == (12,)
    assert np.isclose(result[0], 0.50)
