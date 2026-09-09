"""
Baseline machine-learning model for Ichara AI Tchad.

This module provides a simple Random Forest classifier that can be
used as a baseline for isolated sign recognition experiments.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from sklearn.ensemble import RandomForestClassifier


class BaselineClassifier:
    """
    Random Forest baseline classifier.

    This model is intended for initial experiments and benchmarking.
    It is not considered the final recognition model.
    """

    def __init__(
        self,
        n_estimators: int = 100,
        random_state: int = 42,
    ) -> None:
        """
        Initialize the baseline classifier.

        Args:
            n_estimators: Number of trees in the forest.
            random_state: Seed used for reproducibility.
        """
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=random_state,
            n_jobs=-1,
        )

        self._is_trained = False

    def fit(
        self,
        features: np.ndarray,
        labels: np.ndarray,
    ) -> None:
        """
        Train the classifier.

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

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Predict sign classes.

        Args:
            features: Feature matrix.

        Returns:
            Predicted class labels.
        """
        if not self._is_trained:
            raise RuntimeError(
                "The classifier must be trained before prediction."
            )

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
        Return class probabilities.

        Args:
            features: Feature matrix.

        Returns:
            Probability matrix for each class.
        """
        if not self._is_trained:
            raise RuntimeError(
                "The classifier must be trained before prediction."
            )

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
        if not self._is_trained:
            raise RuntimeError(
                "The classifier must be trained before evaluation."
            )

        features = np.asarray(features)
        labels = np.asarray(labels)

        return float(self.model.score(features, labels))

    def classes(self) -> Optional[np.ndarray]:
        """
        Return the classes learned by the classifier.

        Returns:
            Array of class labels, or None if the model is not trained.
        """
        if not self._is_trained:
            return None

        return self.model.classes_
