"""
Common model interface for Ichara AI Tchad.

This module defines the expected interface for machine-learning
models used by the sign recognition pipeline.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class SignRecognitionModel(ABC):
    """
    Abstract interface for sign recognition models.

    All recognition models should implement the same basic operations:
    training, prediction, probability estimation, and evaluation.
    """

    @abstractmethod
    def fit(
        self,
        features: np.ndarray,
        labels: np.ndarray,
    ) -> None:
        """
        Train the model.

        Args:
            features: Training feature matrix.
            labels: Training labels.
        """
        raise NotImplementedError

    @abstractmethod
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
        raise NotImplementedError

    @abstractmethod
    def predict_proba(
        self,
        features: np.ndarray,
    ) -> np.ndarray:
        """
        Estimate prediction probabilities.

        Args:
            features: Feature matrix.

        Returns:
            Probability matrix for the predicted classes.
        """
        raise NotImplementedError

    @abstractmethod
    def score(
        self,
        features: np.ndarray,
        labels: np.ndarray,
    ) -> float:
        """
        Evaluate the model.

        Args:
            features: Evaluation feature matrix.
            labels: True labels.

        Returns:
            Evaluation score.
        """
        raise NotImplementedError
