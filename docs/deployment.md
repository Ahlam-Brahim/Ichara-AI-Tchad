# Deployment Strategy

## 1. Purpose

This document describes the strategy for transitioning Ichara AI Tchad from a research prototype to a practical application.

The deployment strategy focuses on:

- Mobile deployment
- Efficient inference
- Offline operation
- Model optimization
- Privacy
- Device compatibility
- Reliability
- User experience

The deployment architecture will evolve progressively as the machine-learning model becomes more mature.

---

## 2. Deployment Vision

The long-term objective is to make the recognition system accessible through a mobile application.

A simplified architecture is:

```text
Camera
   ↓
Image / Video Input
   ↓
Computer Vision
   ↓
Hand Detection
   ↓
Landmark Extraction
   ↓
Preprocessing
   ↓
Machine Learning Model
   ↓
Sign Recognition
   ↓
Text
   ↓
Optional Speech Output

The mobile application should eventually provide a simple interface allowing users to interact with the recognition system in real time.

3. Mobile Platform

Flutter is considered as the main framework for the future mobile application.

The mobile project may support:

Android
iOS

Additional platforms may be considered later if they provide meaningful value.

Android may be prioritized during the initial deployment phase because of its relevance to low-cost and widely available smartphones in many African contexts.

4. Model Conversion

A trained research model may need to be converted into a mobile-compatible format.

TensorFlow Lite may be evaluated for this purpose.

The general process is:

Research Model
      ↓
Validation
      ↓
Model Conversion
      ↓
TensorFlow Lite
      ↓
Optimization
      ↓
Mobile Integration
      ↓
Device Testing

Conversion should only be performed after the research model has been sufficiently validated.

5. Model Optimization

Mobile devices have more limited computational resources than research computers.

Optimization techniques may therefore include:

Quantization
Model compression
Pruning
Reduced input size
Lightweight architectures
Feature optimization

The impact of each optimization should be experimentally evaluated.

Optimization should not significantly reduce recognition quality without a justified trade-off.

6. Offline-First Architecture

Offline functionality is an important long-term objective of Ichara AI Tchad.

The recognition pipeline should ideally operate locally on the device.

A possible architecture is:

                 Mobile Device
                       │
        ┌──────────────┴──────────────┐
        │                             │
     Camera                      Local Storage
        │                             │
        ↓                             │
 Computer Vision                       │
        ↓                             │
 Landmarks                              │
        ↓                             │
 Local ML Model                         │
        ↓                             │
 Recognition                            │
        ↓                             │
 Text / Speech                          │
        └──────────────┬──────────────┘
                       ↓
                 User Interface

An internet connection should not be considered mandatory for the core recognition function if offline inference can be achieved reliably.

7. Privacy

Local processing can reduce the need to transmit camera data to external servers.

The application should avoid sending images or videos to a remote server unless this is explicitly required and appropriately authorized.

Privacy principles include:

Local processing where possible
Minimal data collection
No unnecessary personal information
Secure local storage
Transparent data policies
Explicit consent when data collection is required
8. Real-Time Recognition

The future application may support real-time recognition from the device camera.

A simplified real-time pipeline is:

Camera Frame
     ↓
Frame Processing
     ↓
Hand Detection
     ↓
Landmark Extraction
     ↓
Feature Processing
     ↓
Model Inference
     ↓
Prediction
     ↓
Text Display

The pipeline should be optimized to provide acceptable latency without unnecessarily consuming device resources.

9. Temporal Recognition

The initial research focuses on isolated signs.

However, many real-world sign-language interactions involve sequences of movements.

Future versions may therefore investigate temporal recognition.

Possible approaches include:

Recurrent Neural Networks
LSTM
GRU
Temporal Convolutional Networks
Transformer-based architectures

A possible future pipeline is:

Video Sequence
      ↓
Frame-Level Features
      ↓
Temporal Modeling
      ↓
Sequence Recognition
      ↓
Sentence / Text

This is considered a future research direction and is not part of the initial MVP.

10. Text-to-Speech

After recognition, the resulting text may optionally be converted into speech.

Example:

Sign
 ↓
Recognition
 ↓
Text
 ↓
Text-to-Speech
 ↓
Audio

The speech component should be evaluated separately from the recognition model.

The first implementation may focus on text output before introducing speech synthesis.

11. Mobile User Interface

The future application should prioritize simplicity and accessibility.

Possible screens include:

Home
 ├── Start Recognition
 ├── History
 ├── Settings
 └── Help

The recognition interface may provide:

Camera preview
Recognition status
Detected sign
Text output
Optional audio output
Error or uncertainty indication

The interface should avoid unnecessary complexity.

12. Confidence and Uncertainty

The application should avoid presenting uncertain predictions as guaranteed results.

Where technically appropriate, the interface may display:

Prediction: HELLO
Confidence: 92%

or:

Prediction uncertain
Please try again

Confidence values should only be displayed if they are properly calibrated and experimentally justified.

13. Device Compatibility

The application should eventually be tested across different device categories.

Possible variables include:

RAM
CPU performance
Camera quality
Android version
Screen resolution
Available storage
Battery capacity

Testing on low-resource devices is particularly relevant to the project's accessibility objectives.

14. Performance Evaluation

Deployment performance should be measured using practical metrics.

Possible measurements include:

Model size
Inference latency
Frames per second
Memory consumption
CPU usage
Battery consumption
Application startup time
Model loading time

These measurements should be documented for each tested device.

15. Security

The application should follow basic security principles.

Potential measures include:

Secure local storage
Minimal permissions
No unnecessary network communication
Secure dependency management
Regular dependency updates
Protection against unauthorized data access

Camera permissions should be requested only when required by the application.

16. Deployment Pipeline

A future deployment workflow may follow:

Research
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Optimization
   ↓
Model Conversion
   ↓
Mobile Integration
   ↓
Device Testing
   ↓
User Testing
   ↓
Release

Each stage should have validation criteria before moving to the next stage.

17. Testing Before Release

Before any public release, the application should be tested for:

Functional correctness
Camera operation
Recognition
Text display
Optional speech
Navigation
Offline behavior
Performance
Inference speed
Memory consumption
Battery usage
Robustness
Different lighting conditions
Different backgrounds
Different users
Different devices
Privacy
Permission handling
Data storage
Network behavior
18. Versioning

The application and model should use clear version numbers.

Example:

Application v0.1.0
Model v0.1
Dataset v0.1

Each release should document important changes.

Example:

v0.2.0
- Improved recognition model
- Added new signs
- Improved offline inference
- Fixed camera processing issue
19. Deployment Environments

Different environments should be distinguished.

Development

Used for active development and debugging.

Testing

Used for controlled testing and validation.

Production

Used for a stable public release.

The production version should only contain validated components.

20. Monitoring and Feedback

After deployment, user feedback may provide valuable information about real-world limitations.

Possible feedback areas include:

Recognition errors
Difficult signs
Camera problems
Performance issues
Accessibility issues
Device compatibility
User experience

Any future data collection from users must follow appropriate ethical and privacy procedures.

21. Limitations

Potential deployment limitations include:

Limited mobile processing power
Camera quality differences
Battery consumption
Model size
Recognition errors
Environmental conditions
Limited device compatibility
Dataset limitations

These limitations should be documented rather than hidden.

22. Future Expansion

Future deployment research may investigate:

Continuous sign recognition
More advanced temporal models
Multimodal recognition
Body and facial landmarks
Improved speech output
Broader device compatibility
Community-based validation
More locally relevant sign-language resources

The project may also investigate multilingual accessibility involving French, Arabic, and potentially local Chadian languages.

This multilingual direction is a future research objective and is not considered an implemented feature of the current system.

23. Current Status

Deployment is currently considered a future stage of the project.

Current priorities:

 Validate the recognition model
 Establish a stable inference pipeline
 Evaluate TensorFlow Lite
 Optimize the model
 Integrate the model with Flutter
 Test offline inference
 Test on Android devices
 Evaluate performance
 Conduct usability testing
 Prepare a first mobile prototype
24. Guiding Principle

Deployment should not begin with the assumption that a research model is automatically ready for real-world use.

The transition from research to application should be progressive:

Research
   ↓
Validation
   ↓
Optimization
   ↓
Prototype
   ↓
Testing
   ↓
User Validation
   ↓
Deployment

The objective is to build a system that is not only technically functional, but also accessible, efficient, private, reliable, and appropriate for its intended context.
