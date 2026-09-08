# Experimental Framework

## 1. Purpose

This document defines the experimental framework for Ichara AI Tchad.

The objective is to ensure that machine-learning experiments are:

- Structured
- Reproducible
- Comparable
- Documented
- Scientifically interpretable

Each experiment should answer a specific research question rather than simply attempting to improve a performance score.

---

## 2. Research Questions

The experiments may investigate questions such as:

- Which representation is most effective for isolated sign recognition?
- Do normalized hand landmarks improve classification?
- Which machine-learning model performs best on the available data?
- How well does the model generalize to unseen participants?
- Which environmental conditions affect recognition?
- What is the trade-off between accuracy and computational efficiency?
- Can the model operate efficiently on mobile hardware?

The research questions may evolve as new results are obtained.

---

## 3. Experimental Pipeline

A typical experiment follows this process:

```text
Dataset
   ↓
Data Validation
   ↓
Preprocessing
   ↓
Feature Extraction
   ↓
Train / Validation / Test Split
   ↓
Model Training
   ↓
Validation
   ↓
Testing
   ↓
Metrics
   ↓
Error Analysis
   ↓
Documentation

Each stage should be documented sufficiently to allow the experiment to be reproduced.

4. Experiment Identification

Each experiment should have a unique identifier.

Example:

EXP-001
EXP-002
EXP-003

A simple naming convention can also be used:

EXP-001-baseline
EXP-002-normalized-landmarks
EXP-003-random-forest
EXP-004-neural-network

The naming convention may evolve as the project grows.

5. Experiment Record

Each experiment should document at least:

Experiment ID:
Date:
Objective:
Research Question:
Dataset Version:
Number of Classes:
Number of Samples:
Feature Representation:
Model:
Training Configuration:
Evaluation Protocol:
Results:
Observations:
Limitations:
Next Step:

This structure provides a consistent record for future comparison.

6. Baseline Experiments

The first experiments should establish baseline performance.

Possible baseline models include:

Logistic Regression
K-Nearest Neighbors
Random Forest
Support Vector Machine
Simple neural network

The baseline provides a reference point for evaluating more advanced models.

A more complex model should only be considered an improvement if the experimental evidence supports that conclusion.

7. Feature Experiments

Different feature representations may be tested.

Examples include:

Raw landmarks

Using the original landmark coordinates.

Normalized landmarks

Coordinates normalized relative to the hand position and scale.

Relative distances

Distances between selected landmarks.

Angles

Geometric angles between fingers or joints.

Combined features

A combination of coordinates, distances, and angles.

Each representation should be evaluated under comparable conditions.

8. Model Experiments

Different model families may be compared.

Possible approaches include:

Traditional Machine Learning
        ↓
Logistic Regression
Random Forest
SVM
KNN

Deep Learning
        ↓
Dense Neural Network
CNN
Temporal Models

The selected models should depend on the characteristics of the dataset and the research objectives.

9. Training Configuration

Important training parameters should be recorded.

Examples include:

Learning rate
Batch size
Number of epochs
Optimizer
Loss function
Dropout
Regularization
Early stopping
Data augmentation
Random seed

Example:

Learning rate: TBD
Batch size: TBD
Epochs: TBD
Optimizer: TBD
Loss: TBD
Random seed: TBD

Values should only be recorded after they have actually been used.

10. Controlled Experiments

Experiments should change one important factor at a time whenever possible.

For example:

Experiment A
Model: Random Forest
Features: Raw landmarks

Experiment B
Model: Random Forest
Features: Normalized landmarks

This makes it easier to determine whether the change in performance is actually related to the feature representation.

11. Dataset Experiments

The effect of dataset characteristics may also be studied.

Possible experiments include:

Different vocabulary sizes
Different numbers of participants
Balanced vs imbalanced datasets
Different train/test configurations
Different environmental conditions
Different augmentation strategies

These experiments can help identify the limitations of the dataset.

12. Participant Generalization

A key research objective is evaluating performance on unseen participants.

Experiments should therefore distinguish between:

Training Participants
        ↓
Model Training
        ↓
Unseen Participants
        ↓
Final Evaluation

This is important because the model should not simply memorize the characteristics of the people represented in the training data.

13. Robustness Experiments

The system should eventually be tested under different conditions.

Examples include:

Bright lighting
Low lighting
Different backgrounds
Different camera distances
Different camera angles
Different signing speeds
Different smartphones

The purpose is to determine how environmental changes affect recognition.

14. Error Analysis Experiments

Incorrect predictions should be analyzed systematically.

For each important error, researchers may record:

Expected class:
Predicted class:
Participant:
Environment:
Image / video condition:
Possible cause:
Potential solution:

Possible causes include:

Similar signs
Occlusion
Poor landmark detection
Motion blur
Lighting
Annotation errors
Insufficient training data
User variation

Error analysis should guide subsequent experiments.

15. Ablation Experiments

Ablation studies can be used to determine the contribution of individual components.

Examples:

Model + raw landmarks

Model + normalized landmarks

Model + normalized landmarks + distances

Model + normalized landmarks + distances + angles

The results can show whether additional features provide meaningful improvements.

16. Repeated Experiments

When appropriate, experiments should be repeated to evaluate the stability of the results.

Possible sources of variation include:

Random initialization
Dataset shuffling
Training/test split
Hyperparameter changes

When multiple runs are performed, the project may report:

Mean performance
Standard deviation
Best performance
Worst performance
17. Experiment Tracking

Experiment information should be stored in a structured way.

A future experiment log may use:

experiments/
├── README.md
├── results.csv
└── logs/

For each experiment, the project may record:

Experiment ID
Dataset version
Model version
Parameters
Metrics
Hardware
Software environment
Notes
18. Reproducibility

An experiment should be reproducible whenever reasonably possible.

The following should be recorded:

Code version
Dataset version
Model configuration
Random seed
Dependencies
Hardware
Operating environment
Training parameters

This is particularly important for scientific research and future publication.

19. Hardware and Environment

Computational conditions should be documented.

Example:

Operating System: TBD
CPU: TBD
GPU: TBD
RAM: TBD
Python Version: TBD
TensorFlow Version: TBD
OpenCV Version: TBD
MediaPipe Version: TBD

This information can help explain differences between experiments performed on different machines.

20. Result Reporting

Results should be reported using consistent metrics.

Possible metrics include:

Accuracy
Precision
Recall
F1-score
Macro F1-score
Confusion matrix
Inference time
Model size

Example:

Experiment	Model	Features	Accuracy	F1-Score	Inference Time
EXP-001	TBD	TBD	TBD	TBD	TBD
EXP-002	TBD	TBD	TBD	TBD	TBD
EXP-003	TBD	TBD	TBD	TBD	TBD

No results should be fabricated or entered before experimental measurement.

21. Model Selection

The final model should not be selected solely according to accuracy.

Selection should consider:

Accuracy
Generalization
Robustness
Inference speed
Model size
Memory requirements
Mobile compatibility
Offline capability
Stability
Reproducibility

The best model is therefore the model that provides the most appropriate balance for the intended application.

22. Mobile Experiments

When the project reaches the deployment stage, additional experiments should evaluate the model on mobile devices.

Possible measurements include:

Inference latency
Memory usage
Battery impact
Application responsiveness
Model loading time
Offline operation
Device compatibility

TensorFlow Lite or another suitable mobile inference framework may be evaluated at this stage.

23. Experiment Limitations

Every experiment should document its limitations.

Examples include:

Small dataset
Limited participants
Limited vocabulary
Controlled environment
Hardware limitations
Dataset bias
Measurement uncertainty

Experimental conclusions should remain proportional to the available evidence.

24. Experiment Lifecycle

The research process can follow an iterative cycle:

Research Question
       ↓
Hypothesis
       ↓
Experiment Design
       ↓
Implementation
       ↓
Training
       ↓
Evaluation
       ↓
Error Analysis
       ↓
Interpretation
       ↓
Next Experiment

This cycle allows the project to progressively improve its methodology.

25. Current Status

The experimental framework is currently at the planning stage.

Current priorities:

 Define initial research questions
 Establish baseline experiments
 Prepare experiment records
 Implement baseline models
 Define reproducible evaluation procedures
 Record experimental configurations
 Analyze initial results
 Compare different approaches
 Document limitations
 Prepare future mobile experiments
26. Guiding Principle

Every experiment should have a clear purpose.

The objective is not to produce impressive numbers without context.

The objective is to generate reliable evidence that helps answer scientific questions and progressively improve Ichara AI Tchad.
