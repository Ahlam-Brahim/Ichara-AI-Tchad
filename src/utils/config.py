"""
Configuration utilities for Ichara AI Tchad.

This module centralizes project-wide configuration values.
The configuration is intentionally simple at this stage and can
later be extended to support environment variables or configuration
files.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Main directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LANDMARKS_DATA_DIR = DATA_DIR / "landmarks"

MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCS_DIR = PROJECT_ROOT / "docs"


@dataclass(frozen=True)
class VisionConfig:
    """Configuration for the computer-vision pipeline."""

    max_num_hands: int = 2
    min_detection_confidence: float = 0.5
    min_tracking_confidence: float = 0.5


@dataclass(frozen=True)
class TrainingConfig:
    """Default configuration for model experiments."""

    random_state: int = 42
    validation_size: float = 0.15
    test_size: float = 0.15


@dataclass(frozen=True)
class ProjectConfig:
    """Global project configuration."""

    name: str = "Ichara AI Tchad"
    version: str = "0.1.0"

    vision: VisionConfig = VisionConfig()
    training: TrainingConfig = TrainingConfig()


CONFIG = ProjectConfig()
