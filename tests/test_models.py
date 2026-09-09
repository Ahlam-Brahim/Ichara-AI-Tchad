"""
Tests for machine-learning models.

Ichara AI Tchad
"""

import numpy as np
import pytest

from src.models.baseline import BaselineClassifier
from src.models.neural_network import NeuralNetworkClassifier
from src.models.model_factory import (
    available_models,
    create_model,
)


@pytest.fixture
def sample_dataset():
    """Create a small synthetic dataset for testing."""
    features = np.array(
        [
            [0.0, 0.0, 0.0, 0.0],
            [0.1, 0.1, 0.1, 0.1],
            [0.2, 0.2, 0.2, 0.2],
            [0.9, 0.9, 0.9, 0.9],
            [1.0, 1.0, 1.0, 1.0],
            [0.8, 0.8, 0.8, 0.8],
        ],
        dtype=np.float32,
    )

    labels = np.array(
        [
            "sign_a",
            "sign_a",
            "sign_a",
            "sign_b",
            "sign_b",
            "sign_b",
        ]
    )

    return features, labels


def test_baseline_classifier_training(sample_dataset):
    """Baseline classifier should train successfully."""
    features, labels = sample_dataset

    model = BaselineClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(features, labels)

    predictions = model.predict(features)

    assert len(predictions) == len(labels)
    assert model.classes() is not None


def test_baseline_classifier_score(sample_dataset):
    """Baseline classifier should return a valid score."""
    features, labels = sample_dataset

    model = BaselineClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(features, labels)

    score = model.score(features, labels)

    assert 0.0 <= score <= 1.0


def test_baseline_predict_proba(sample_dataset):
    """Baseline classifier should return probabilities."""
    features, labels = sample_dataset

    model = BaselineClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(features, labels)

    probabilities = model.predict_proba(features)

    assert probabilities.shape[0] == len(features)
    assert probabilities.shape[1] == len(np.unique(labels))


def test_baseline_requires_training(sample_dataset):
    """Prediction before training should raise an error."""
    features, _ = sample_dataset

    model = BaselineClassifier()

    with pytest.raises(RuntimeError):
        model.predict(features)


def test_neural_network_training(sample_dataset):
    """Neural network should train successfully."""
    features, labels = sample_dataset

    model = NeuralNetworkClassifier(
        hidden_layer_sizes=(16,),
        max_iter=100,
        random_state=42,
    )

    model.fit(features, labels)

    predictions = model.predict(features)

    assert len(predictions) == len(labels)
    assert model.classes() is not None


def test_neural_network_predict_proba(sample_dataset):
    """Neural network should return probabilities."""
    features, labels = sample_dataset

    model = NeuralNetworkClassifier(
        hidden_layer_sizes=(16,),
        max_iter=100,
        random_state=42,
    )

    model.fit(features, labels)

    probabilities = model.predict_proba(features)

    assert probabilities.shape[0] == len(features)
    assert probabilities.shape[1] == len(np.unique(labels))


def test_model_factory_random_forest():
    """Factory should create a Random Forest model."""
    model = create_model(
        "random_forest",
        n_estimators=10,
        random_state=42,
    )

    assert isinstance(model, BaselineClassifier)


def test_model_factory_neural_network():
    """Factory should create a neural network model."""
    model = create_model(
        "neural_network",
        hidden_layer_sizes=(16,),
        max_iter=100,
        random_state=42,
    )

    assert isinstance(model, NeuralNetworkClassifier)


def test_model_factory_aliases():
    """Factory should support model aliases."""
    random_forest = create_model(
        "rf",
        n_estimators=10,
    )

    neural_network = create_model(
        "mlp",
        hidden_layer_sizes=(16,),
        max_iter=100,
    )

    assert isinstance(random_forest, BaselineClassifier)
    assert isinstance(neural_network, NeuralNetworkClassifier)


def test_model_factory_invalid_model():
    """Unknown model names should raise ValueError."""
    with pytest.raises(ValueError):
        create_model("unknown_model")


def test_available_models():
    """Factory should expose the available model types."""
    models = available_models()

    assert "random_forest" in models
    assert "neural_network" in models
