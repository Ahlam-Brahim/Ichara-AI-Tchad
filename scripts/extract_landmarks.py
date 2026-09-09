"""
Extract hand landmarks from image datasets.

Ichara AI Tchad

This script provides a first data-processing utility for extracting
MediaPipe hand landmarks from images.

Expected input structure:

data/raw/
├── sign_a/
│   ├── image_001.jpg
│   └── image_002.jpg
├── sign_b/
│   ├── image_001.jpg
│   └── image_002.jpg
└── ...

Output:

data/landmarks/landmarks.csv
"""

from __future__ import annotations

import csv
from pathlib import Path

import cv2

from src.utils.logger import get_logger
from src.utils.paths import LANDMARKS_DIR, RAW_DATA_DIR
from src.vision.hand_detector import HandDetector


logger = get_logger(__name__)

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}


def find_images(input_directory: Path) -> list[Path]:
    """
    Find supported image files recursively.

    Args:
        input_directory: Root directory containing the dataset.

    Returns:
        List of image paths.
    """
    if not input_directory.exists():
        logger.warning(
            "Input directory does not exist: %s",
            input_directory,
        )
        return []

    return sorted(
        path
        for path in input_directory.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def extract_landmarks_from_image(
    image_path: Path,
    detector: HandDetector,
) -> list:
    """
    Detect hands and extract their landmarks from one image.

    Args:
        image_path: Path to the image.
        detector: Initialized hand detector.

    Returns:
        List of detected HandLandmarks objects.
    """
    image = cv2.imread(str(image_path))

    if image is None:
        logger.warning(
            "Unable to read image: %s",
            image_path,
        )
        return []

    return detector.detect(image)


def save_landmarks(
    rows: list[dict],
    output_path: Path,
) -> None:
    """
    Save extracted landmarks to a CSV file.

    Args:
        rows: Landmark records.
        output_path: Destination CSV file.
    """
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fieldnames = [
        "sample_id",
        "image_path",
        "label",
        "hand_index",
        "handedness",
        "landmarks",
    ]

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)


def process_dataset(
    input_directory: Path = RAW_DATA_DIR,
    output_path: Path = LANDMARKS_DIR / "landmarks.csv",
) -> int:
    """
    Process an image dataset and extract hand landmarks.

    The parent directory of each image is used as its label.

    Args:
        input_directory: Dataset root directory.
        output_path: CSV output path.

    Returns:
        Number of detected hands.
    """
    image_paths = find_images(input_directory)

    if not image_paths:
        logger.warning(
            "No supported images found in: %s",
            input_directory,
        )
        return 0

    detector = HandDetector()
    rows = []
    detected_hands = 0

    try:
        for sample_id, image_path in enumerate(
            image_paths,
            start=1,
        ):
            label = image_path.parent.name

            hands = extract_landmarks_from_image(
                image_path,
                detector,
            )

            if not hands:
                logger.info(
                    "No hand detected: %s",
                    image_path,
                )
                continue

            for hand_index, hand in enumerate(hands):
                landmark_values = []

                for x, y, z in hand.points:
                    landmark_values.extend(
                        [x, y, z]
                    )

                rows.append(
                    {
                        "sample_id": sample_id,
                        "image_path": str(image_path),
                        "label": label,
                        "hand_index": hand_index,
                        "handedness": hand.handedness,
                        "landmarks": " ".join(
                            map(str, landmark_values)
                        ),
                    }
                )

                detected_hands += 1

    finally:
        detector.close()

    save_landmarks(rows, output_path)

    logger.info(
        "Processed %d images.",
        len(image_paths),
    )

    logger.info(
        "Detected %d hands.",
        detected_hands,
    )

    logger.info(
        "Landmarks saved to: %s",
        output_path,
    )

    return detected_hands


if __name__ == "__main__":
    process_dataset()
