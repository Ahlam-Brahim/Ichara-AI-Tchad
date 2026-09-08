#  Ichara AI Tchad — Research Methodology

## 1. Purpose

This document describes the proposed research methodology for the development of Ichara AI Tchad.

The project aims to investigate whether Artificial Intelligence and Computer Vision can be used to recognize sign language gestures and transform them into accessible communication outputs such as text and, later, speech.

The methodology will evolve as the project progresses and experimental results become available.

---

## 2. Research Approach

The project will follow an iterative experimental approach:

```text
Research
   ↓
Data Collection
   ↓
Data Preparation
   ↓
Feature Extraction
   ↓
Model Development
   ↓
Training
   ↓
Evaluation
   ↓
Optimization
   ↓
Prototype
   ↓
Real-World Testing

Each stage will be documented so that the development process remains reproducible and scientifically transparent.

3. Phase 1 — Literature Review

The first stage will consist of reviewing existing research related to:

Sign language recognition
Hand gesture recognition
Computer Vision
Hand landmark detection
Human pose estimation
Deep Learning
Multimodal AI
Edge AI
Mobile Machine Learning
Accessibility technologies

The literature review will help identify:

Existing approaches
Common datasets
Model architectures
Evaluation methods
Technical limitations
Research gaps

The objective is to avoid unnecessarily reproducing existing work and to identify opportunities for meaningful experimentation.

4. Phase 2 — Problem Definition

The initial problem will be deliberately limited to isolated sign recognition.

The first system will attempt to answer:

Can a Machine Learning model recognize a predefined set of sign language gestures from visual input?

The initial pipeline will therefore be:

Visual Input
     ↓
Hand Detection
     ↓
Landmark Extraction
     ↓
Feature Processing
     ↓
Classification
     ↓
Predicted Sign

The vocabulary will initially remain small to allow reliable experimentation.

5. Phase 3 — Dataset Design

A suitable dataset is essential for the success of the project.

The project may use existing public datasets for experimentation and comparison, while also exploring the creation of locally relevant data.

The initial dataset should contain:

Sign class
Hand landmarks or image/video information
Sample identifier
Optional metadata
Dataset split

Example:

sample_001 → bonjour
sample_002 → merci
sample_003 → oui
sample_004 → non
6. Data Collection

If a custom dataset is created, data collection will follow a predefined protocol.

The protocol should consider:

Number of participants
Number of samples per sign
Camera position
Lighting conditions
Background variation
Hand orientation
Distance from camera
Gesture speed
Recording device

The objective is to capture enough variation for the model to generalize to users and environments that were not present during training.

7. Ethics and Consent

When collecting data from people, participation must be voluntary and based on informed consent.

Participants should be informed about:

The purpose of the project
How recordings will be used
How data will be stored
Whether data may be shared
The possibility of withdrawing where applicable

Personally identifiable information should be minimized.

Raw recordings should not be published publicly without appropriate authorization.

The detailed ethical framework will be documented separately in:

docs/ethics.md
8. Phase 4 — Data Preprocessing

Raw data will be processed before being used for Machine Learning.

Possible preprocessing operations include:

Data cleaning
Label verification
Removal of corrupted samples
Coordinate normalization
Scaling
Noise reduction
Feature normalization
Duplicate detection

For landmark-based recognition, the data may be transformed into normalized feature vectors.

Example:

Raw Hand
    ↓
21 Landmarks
    ↓
Coordinates
    ↓
Normalization
    ↓
Feature Vector
9. Phase 5 — Feature Extraction

The initial approach may use hand landmarks as the primary representation.

A hand-tracking system such as MediaPipe can provide a set of landmark coordinates.

For each detected hand:

21 landmarks × coordinates

may be transformed into a numerical representation suitable for Machine Learning.

Possible features include:

Relative landmark positions
Distances between landmarks
Angles between joints
Normalized coordinates
Temporal changes for moving gestures

The final feature representation will be determined experimentally.

10. Phase 6 — Dataset Splitting

The dataset will be divided into separate subsets:

Dataset
   │
   ├── Training Set
   │
   ├── Validation Set
   │
   └── Test Set

A typical initial strategy may use:

Training: 70%
Validation: 15%
Testing: 15%

However, the exact proportions may change depending on dataset size and experimental requirements.

Where possible, samples from the same participant should be handled carefully to avoid data leakage.

For realistic evaluation, experiments should include testing on users or recording conditions that were not used during training.

11. Phase 7 — Baseline Model

Before experimenting with complex architectures, a baseline model will be developed.

Possible baseline algorithms include:

Logistic Regression
Support Vector Machine
Random Forest
K-Nearest Neighbors
Simple Neural Network

The baseline provides a reference point for evaluating more advanced approaches.

12. Phase 8 — Deep Learning Experiments

After establishing a baseline, more advanced Machine Learning approaches may be investigated.

Possible architectures include:

Multi-Layer Perceptrons
Convolutional Neural Networks
Recurrent Neural Networks
LSTM
GRU
Transformer-based architectures

The choice of architecture will depend on the type of data and the recognition problem.

For isolated signs, a simpler model may be sufficient.

For continuous sign recognition, temporal models may become more appropriate.

13. Phase 9 — Training

The training process will involve:

Training Data
     ↓
Model
     ↓
Prediction
     ↓
Loss Calculation
     ↓
Parameter Update
     ↓
Next Iteration

Training experiments will record relevant parameters such as:

Model architecture
Number of epochs
Batch size
Learning rate
Optimizer
Loss function
Dataset version
Random seed

This information will help make experiments reproducible.

14. Phase 10 — Model Evaluation

The trained model will be evaluated on data that was not used during training.

Potential metrics include:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

For real-time applications, additional metrics will be considered:

Inference time
Frames per second
Model size
Memory consumption
CPU usage
Battery impact
15. Participant-Level Evaluation

A major concern in sign-language recognition is whether a model can generalize to people it has never seen before.

Therefore, evaluation should distinguish between:

Same-user evaluation
        vs
Unseen-user evaluation

A model that performs well only on people represented in its training data may not be suitable for real-world deployment.

Where the dataset allows it, participant-level splits will therefore be considered.

16. Error Analysis

Model errors will not simply be counted.

They will be analyzed to understand why the system fails.

Possible causes include:

Similar hand configurations
Poor lighting
Occlusion
Incorrect landmark detection
Unusual hand orientation
Fast movements
Background interference
Insufficient training examples
Ambiguous gestures

The results of error analysis will guide subsequent improvements.

17. Model Optimization

Once a sufficiently accurate model has been identified, optimization may be investigated.

Possible techniques include:

Model simplification
Quantization
Pruning
Reduced precision
Feature reduction
Efficient architectures

The objective will be to obtain a practical balance between:

Accuracy
    ↕
Speed
    ↕
Model Size
    ↕
Device Resources
18. Mobile Deployment

A future stage will involve deploying the trained model on a mobile device.

The proposed pipeline is:

Trained Model
      ↓
Model Optimization
      ↓
TensorFlow Lite
      ↓
Flutter Integration
      ↓
Mobile Application

The first target will likely be Android, while keeping the architecture compatible with future cross-platform development.

19. Real-Time Recognition

After successful model deployment, the system may process camera frames continuously.

Conceptually:

Camera Frame
     ↓
Hand Detection
     ↓
Landmarks
     ↓
Preprocessing
     ↓
Model Inference
     ↓
Prediction
     ↓
Text

Temporal smoothing or prediction filtering may later be used to reduce unstable predictions.

20. Offline-First Investigation

The project will investigate whether recognition can be performed directly on the device without requiring a permanent Internet connection.

Potential advantages include:

Lower latency
Better privacy
Reduced connectivity requirements
Greater accessibility in low-connectivity environments

Offline capability will be evaluated according to:

Model size
Device performance
Inference speed
Accuracy
Memory consumption

Offline deployment remains a development objective and will be validated experimentally.

21. Progressive Development

The project will not attempt to recognize complete conversations from the beginning.

Development will proceed progressively:

Stage 1
5 isolated signs
       ↓
Stage 2
10+ signs
       ↓
Stage 3
Larger vocabulary
       ↓
Stage 4
Real-time recognition
       ↓
Stage 5
Sequences of signs
       ↓
Stage 6
Continuous sign recognition

Each stage should be evaluated before moving to the next.

22. Future Multilingual Research

The initial research will focus on sign recognition and text output.

In the long term, the project may explore multilingual translation involving:

French
Arabic
Potentially local Chadian languages

This is a future research direction, not part of the initial implementation.

Such a system would require:

Reliable linguistic resources
Native speakers
Linguistic expertise
Community participation
Appropriate translation models
Human validation

The project will avoid making assumptions about local languages or sign-language varieties without appropriate research and validation.

23. Reproducibility

To improve reproducibility, experiments should document:

Dataset version
Preprocessing method
Model architecture
Hyperparameters
Training configuration
Software versions
Hardware configuration
Evaluation metrics
Random seeds where relevant

Experimental notebooks and scripts should be organized within:

notebooks/
src/
24. Experiment Tracking

Each significant experiment should be documented.

Example:

Experiment ID: EXP-001

Dataset:
Version 0.1

Model:
Baseline Classifier

Classes:
5

Training:
70%

Validation:
15%

Testing:
15%

Results:
To be determined

Results will only be added after the corresponding experiment has actually been performed.

25. Research Integrity

Ichara AI Tchad will distinguish clearly between:

Proposed methods
Experiments in progress
Validated results
Limitations
Future hypotheses

No accuracy, dataset size, performance or deployment claim should be presented as a result before experimental validation.

26. Current Methodology Status
Research
 Initial research direction defined
 Literature review
 Related-work analysis
Dataset
 Dataset strategy
 Vocabulary definition
 Data collection protocol
 Data collection
 Annotation
 Validation
Machine Learning
 Baseline model
 Training
 Evaluation
 Error analysis
 Optimization
Deployment
 Model conversion
 Mobile integration
 Real-time inference
 Offline testing
Evaluation
 Unseen-user testing
 Real-world testing
 User feedback
 Final evaluation
27. Methodology Evolution

This methodology is a living document.

It will be updated as new evidence, experiments and research findings become available.

The objective is to maintain a transparent record of how Ichara AI Tchad evolves from an initial concept into a validated prototype.


### Dans GitHub

**Nom du fichier :**
```text
docs/methodology.md
