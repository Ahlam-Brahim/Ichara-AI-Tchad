"""
Path utilities for Ichara AI Tchad.

This module provides centralized paths for project resources.
Keeping paths in one place makes the project easier to maintain
and reduces hard-coded file paths throughout the codebase.
"""

from __future__ import annotations

from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Main directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LANDMARKS_DIR = DATA_DIR / "landmarks"

MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"

# Future experiment directory
EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"


def ensure_directory(path: Path) -> Path:
    """
    Create a directory if it does not already exist.

    Args:
        path: Directory path.

    Returns:
        The same Path object.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_raw_data_path(filename: str) -> Path:
    """
    Return the path of a file in the raw data directory.

    Args:
        filename: Name of the file.

    Returns:
        Full path to the raw data file.
    """
    return RAW_DATA_DIR / filename


def get_processed_data_path(filename: str) -> Path:
    """
    Return the path of a file in the processed data directory.

    Args:
        filename: Name of the file.

    Returns:
        Full path to the processed data file.
    """
    return PROCESSED_DATA_DIR / filename


def get_landmarks_path(filename: str) -> Path:
    """
    Return the path of a file in the landmarks directory.

    Args:
        filename: Name of the file.

    Returns:
        Full path to the landmarks file.
    """
    return LANDMARKS_DIR / filename


def get_model_path(filename: str) -> Path:
    """
    Return the path of a model file.

    Args:
        filename: Name of the model file.

    Returns:
        Full path to the model file.
    """
    return MODELS_DIR / filename


def initialize_project_directories() -> None:
    """
    Create the main project directories when necessary.
    """
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        LANDMARKS_DIR,
        MODELS_DIR,
        NOTEBOOKS_DIR,
        DOCS_DIR,
        TESTS_DIR,
        EXPERIMENTS_DIR,
    ]

    for directory in directories:
        ensure_directory(directory)
