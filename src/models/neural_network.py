"""
Neural network model for Ichara AI Tchad.

This module provides a simple Multi-Layer Perceptron (MLP)
for isolated sign recognition experiments.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from sklearn.neural_network import MLPClassifier


class NeuralNetworkClassifier:
    """
    Multi-Layer Perceptron classifier.

    This model is intended for experimentation and comparison
    with the baseline classifier.
    """

    def __init__(
        self,
        hidden_layer_sizes: tuple[int, ...] = (128, 64),
        learning_rate_init: float = 0.001,
        max_iter: int = 300,
        random_state: int = 42,
    ) -> None:
        """
        Initialize the neural network.

        Args:
            hidden_layer_sizes: Number of neurons in each hidden layer.
            learning_rate_init: Initial learning rate.
            max_iter: Maximum number of training iterations.
            random_state: Seed for reproducibility.
        """
        self.model = MLPClassifier(
            hidden_layer_sizes=hidden_layer_sizes,
            activation="relu",
            solver="adam",
            learning_rate_init=learning_rate_init,
            max_iter=max_iter,
            random_state=random_state,
            early_stopping=True,
            validation_fraction=0.15,
        )

        self._is_trained = False

    def fit(
        self,
        features: np.ndarray,
        labels: np.ndarray,
    ) -> None:
        """
        Train the neural network.

        Args:
            features: Training feature matrix.
            labels: Training labels.
        """
        features = np.asarray(features)
        labels = np.asarray(labels)

        if features.ndim != 2:
            raise ValueError(
                "Features must be a 2-dimensional array."
            )

        if len(features) != len(labels):
            raise ValueError(
                "Features and labels must have the same number of samples."
            )

        if len(features) == 0:
            raise ValueError(
                "Training data cannot be empty."
            )

        self.model.fit(features, labels)
        self._is_trained = True

    def predict(
        self,
        features: np.ndarray,
    ) -> np.ndarray:
        """
        Predict sign classes.

        Args:
            features: Feature matrix.

        Returns:
            Predicted class labels.
        """
        self._check_trained()

        features = np.asarray(features)

        if features.ndim != 2:
            raise ValueError(
                "Features must be a 2-dimensional array."
            )

        return self.model.predict(features)

    def predict_proba(
        self,
        features: np.ndarray,
    ) -> np.ndarray:
        """
        Estimate prediction probabilities.

        Args:
            features: Feature matrix.

        Returns:
            Probability matrix.
        """
        self._check_trained()

        features = np.asarray(features)

        if features.ndim != 2:
            raise ValueError(
                "Features must be a 2-dimensional array."
            )

        return self.model.predict_proba(features)

    def score(
        self,
        features: np.ndarray,
        labels: np.ndarray,
    ) -> float:
        """
        Calculate classification accuracy.

        Args:
            features: Feature matrix.
            labels: True labels.

        Returns:
            Accuracy score.
        """
        self._check_trained()

        features = np.asarray(features)
        labels = np.asarray(labels)

        return float(self.model.score(features, labels))

    def classes(self) -> Optional[np.ndarray]:
        """
        Return the classes learned by the model.

        Returns:
            Array of class labels or None before training.
        """
        if not self._is_trained:
            return None

        return self.model.classes_

    def _check_trained(self) -> None:
        """Ensure the model has been trained."""
        if not self._is_trained:
            raise RuntimeError(
                "The neural network must be trained before prediction."
            )
