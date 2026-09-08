#  Ichara AI Tchad — System Architecture

## 1. Overview

Ichara AI Tchad is a research and development project exploring the use of Artificial Intelligence and Computer Vision to recognize sign language gestures and facilitate communication.

The initial system is designed around a simple pipeline:

```text
Camera
   ↓
Visual Input
   ↓
Hand Detection
   ↓
Landmark Extraction
   ↓
Feature Processing
   ↓
AI Model
   ↓
Sign Classification
   ↓
Text
   ↓
Speech

The architecture is intentionally modular so that individual components can be improved independently as the project evolves.

2. High-Level Architecture
                         ┌───────────────────┐
                         │      Camera       │
                         │  Image / Video    │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Computer Vision  │
                         │   Hand Detection  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Landmark Extraction│
                         │  Hand Coordinates  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Feature Processing│
                         │ Normalization etc.│
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    AI Model       │
                         │ Classification    │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Sign Recognition  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │       Text        │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Text-to-Speech  │
                         └───────────────────┘
3. Input Layer

The system will initially receive visual information through a camera.

Possible input sources include:

Smartphone camera
Computer webcam
Recorded video

The initial prototype will focus primarily on real-time camera input.

4. Computer Vision Layer

The Computer Vision component will be responsible for detecting the relevant visual elements required for sign recognition.

The first version will primarily focus on the hands.

Potential technologies include:

OpenCV
MediaPipe

The exact implementation will be evaluated experimentally.

5. Hand Landmark Extraction

Instead of relying only on raw images, the system may represent a detected hand using a set of landmark points.

A typical hand-tracking system can provide:

21 landmarks

Each landmark can be represented by coordinates such as:

(x, y, z)

This representation can significantly reduce the amount of information that the Machine Learning model needs to process compared with using complete images.

Example:

Hand
 ↓
21 landmarks
 ↓
Coordinates
 ↓
Feature vector
6. Feature Processing

Before sending the extracted landmarks to the Machine Learning model, the data may require preprocessing.

Possible operations include:

Coordinate normalization
Scaling
Translation normalization
Rotation normalization
Feature selection
Noise reduction

The objective is to make the model less sensitive to differences in:

Hand position
Distance from the camera
Camera angle
User position

The final preprocessing pipeline will be determined through experimentation.

7. Machine Learning Layer

The processed features will be provided to a Machine Learning model responsible for classifying the sign.

The first prototype will focus on isolated sign recognition.

Example:

Input:
Hand landmarks

        ↓

AI Model

        ↓

Prediction:
"Bonjour"

Possible model families may include:

Classical Machine Learning classifiers
Feed-forward neural networks
Convolutional Neural Networks
Recurrent Neural Networks
Transformer-based architectures

The first model will serve as a baseline. More advanced architectures may be evaluated later.

8. Sign Classification

The classification layer converts the model's prediction into a predefined sign class.

Example:

Class 0 → Bonjour
Class 1 → Merci
Class 2 → Oui
Class 3 → Non
Class 4 → Aide

The initial vocabulary will remain intentionally small.

It will be expanded only after the baseline system has been properly evaluated.

9. Text Layer

Once a sign has been recognized, the predicted class can be mapped to text.

Example:

Detected sign
      ↓
Class: merci
      ↓
Text: "Merci"

The text layer could later become a foundation for more advanced language-processing components.

10. Speech Layer

A future component may convert recognized text into speech.

Sign
 ↓
Recognition
 ↓
Text
 ↓
Text-to-Speech
 ↓
🔊 Audio

This component is not part of the first recognition experiment and will be introduced progressively.

11. Mobile Architecture

The long-term objective is to integrate the recognition model into a mobile application developed with Flutter.

A simplified architecture could be:

┌──────────────────────────────┐
│       Flutter Application    │
│                              │
│   ┌──────────────────────┐   │
│   │      Camera UI       │   │
│   └──────────┬───────────┘   │
│              ↓               │
│   ┌──────────────────────┐   │
│   │  AI Inference Layer  │   │
│   └──────────┬───────────┘   │
│              ↓               │
│   ┌──────────────────────┐   │
│   │  Sign Recognition    │   │
│   └──────────┬───────────┘   │
│              ↓               │
│       Text / Speech          │
│                              │
└──────────────────────────────┘

TensorFlow Lite may be considered for on-device inference.

12. Offline-First Direction

Because connectivity can be limited in some environments, the project will investigate the possibility of performing inference directly on the device.

The long-term concept is:

Camera
   ↓
Local AI Model
   ↓
Recognition
   ↓
Text / Speech

without requiring a permanent Internet connection.

This is a future technical objective and will depend on model size, device capabilities and experimental results.

13. Future Multimodal Architecture

The initial system will focus mainly on hand gestures.

Future research may investigate additional information sources:

             ┌──────────────┐
             │     Hands    │
             └──────┬───────┘
                    │
             ┌──────▼───────┐
             │     Body     │
             │    Pose      │
             └──────┬───────┘
                    │
             ┌──────▼───────┐
             │     Face     │
             │  Expressions │
             └──────┬───────┘
                    │
                    ▼
             Multimodal AI
                    │
                    ▼
              Sign Meaning

This could become important for continuous sign-language recognition because meaning may depend on movement, body position and facial expressions.

14. Long-Term Multilingual Direction

The initial implementation will focus on sign recognition and text output.

In the future, the system may explore multilingual translation:

              Sign Language
                    ↓
                   AI
                    ↓
        ┌───────────┼───────────┐
        ↓           ↓           ↓
     French       Arabic    Local Languages

Support for local Chadian languages is a long-term research direction, not part of the initial implementation.

Such an extension would require appropriate linguistic resources, native speakers, experts and community validation.

15. Architecture Principles

The project will follow several principles:

Accessibility

The system should aim to remain usable on reasonably accessible mobile devices.

Modularity

Each component should be replaceable without redesigning the entire system.

Privacy

Personal recordings and sensitive participant information should be handled responsibly.

Local Relevance

The system should be developed with consideration for the Chadian context.

Scientific Validation

Technical decisions should be supported by experiments and measurable results.

Transparency

The project should clearly distinguish between:

Planned features
Experimental features
Validated features
Future research directions
16. Current Architecture Status

The architecture described in this document represents the proposed system design.

The individual components will be implemented and validated progressively.

Current status:

 Initial architecture designed
 Recognition pipeline defined
 Hand detection implementation
 Landmark extraction implementation
 Dataset preparation
 Feature preprocessing
 Baseline model
 Model evaluation
 Mobile integration
 Text-to-speech integration
 Real-world testing
17. Evolution Strategy

The architecture is expected to evolve as research progresses.

Version 0.1
Isolated Sign Recognition
        ↓
Version 0.2
More Sign Classes
        ↓
Version 0.3
Mobile Prototype
        ↓
Version 0.4
Real-Time Recognition
        ↓
Version 0.5
Continuous Sign Recognition
        ↓
Future
Multimodal & Multilingual AI

The architecture will be updated whenever experimental findings require significant changes.


**Nom du fichier :**
`docs/architecture.md`

**Message du commit :**
```text
docs: add system architecture
