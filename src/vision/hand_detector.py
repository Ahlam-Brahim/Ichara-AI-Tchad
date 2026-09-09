"""
Hand detection module for Ichara AI Tchad.

This module provides a lightweight wrapper around MediaPipe Hands.
It is designed to serve as the computer-vision entry point of the
sign-language recognition pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import cv2
import mediapipe as mp


@dataclass
class HandLandmarks:
    """Container for the landmarks detected on one hand."""

    points: List[tuple[float, float, float]]
    handedness: Optional[str] = None


class HandDetector:
    """
    Detect hands and extract their landmarks from an image.

    The detector is intentionally kept modular so that the computer
    vision pipeline can evolve independently from the machine-learning
    models.
    """

    def __init__(
        self,
        static_image_mode: bool = False,
        max_num_hands: int = 2,
        min_detection_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
    ) -> None:
        """
        Initialize the MediaPipe hand detector.

        Args:
            static_image_mode: Whether each image should be treated
                independently.
            max_num_hands: Maximum number of hands to detect.
            min_detection_confidence: Minimum detection confidence.
            min_tracking_confidence: Minimum tracking confidence.
        """
        self._mp_hands = mp.solutions.hands

        self._hands = self._mp_hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def detect(self, image) -> List[HandLandmarks]:
        """
        Detect hands in an image.

        Args:
            image: OpenCV image in BGR format.

        Returns:
            A list containing the landmarks of each detected hand.
        """
        if image is None:
            raise ValueError("Input image cannot be None.")

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self._hands.process(rgb_image)

        if not results.multi_hand_landmarks:
            return []

        detected_hands: List[HandLandmarks] = []

        handedness_results = results.multi_handedness or []

        for index, hand_landmarks in enumerate(results.multi_hand_landmarks):
            points = [
                (landmark.x, landmark.y, landmark.z)
                for landmark in hand_landmarks.landmark
            ]

            handedness = None

            if index < len(handedness_results):
                handedness = (
                    handedness_results[index]
                    .classification[0]
                    .label
                )

            detected_hands.append(
                HandLandmarks(
                    points=points,
                    handedness=handedness,
                )
            )

        return detected_hands

    def close(self) -> None:
        """Release MediaPipe resources."""
        self._hands.close()
