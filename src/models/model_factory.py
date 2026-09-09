"""
Model factory for Ichara AI Tchad.

This module centralizes the creation of machine-learning models
used by the sign recognition pipeline.
"""

from __future__ import annotations

from typing import Any

from .baseline import BaselineClassifier
from .neural_network import NeuralNetworkClassifier


def create_model(
    model_name: str,
    **kwargs: Any,
):
    """
    Create a sign-recognition model.

    Args:
        model_name: Name of the model to create.
        **kwargs: Optional model-specific parameters.

    Returns:
        An initialized machine-learning model.

    Raises:
        ValueError: If the requested model is not supported.
    """
    normalized_name = model_name.strip().lower()

    if normalized_name in {
        "random_forest",
        "random-forest",
        "rf",
        "baseline",
    }:
        return BaselineClassifier(**kwargs)

    if normalized_name in {
        "neural_network",
        "neural-network",
        "mlp",
        "ann",
    }:
        return NeuralNetworkClassifier(**kwargs)

    raise ValueError(
        f"Unsupported model: {model_name}. "
        "Available models: random_forest, neural_network."
    )


def available_models() -> list[str]:
    """
    Return the currently available model names.

    Returns:
        List of supported model identifiers.
    """
    return [
        "random_forest",
        "neural_network",
    ]
