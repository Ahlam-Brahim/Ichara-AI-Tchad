# Evaluation Strategy

## 1. Purpose

The evaluation framework defines how the performance, reliability, robustness, and limitations of Ichara AI Tchad will be measured.

The objective is not only to obtain a high accuracy score, but to determine whether the system can generalize to users and conditions that were not present during training.

All reported results should be based on reproducible experiments.

---

## 2. Evaluation Objectives

The evaluation will investigate:

- Recognition accuracy
- Generalization to unseen participants
- Robustness to environmental variations
- Class-specific performance
- Error patterns
- Inference speed
- Model size
- Computational requirements
- Potential mobile deployment constraints

The evaluation strategy may evolve as the project progresses.

---

## 3. Evaluation Dataset

The final test set should remain separate from the training and validation datasets.

The test set should contain samples that were not used during:

- Training
- Hyperparameter selection
- Model development
- Feature engineering decisions

Whenever possible, the test set should contain participants that were not present in the training set.

This provides a more realistic estimate of how the system may perform with new users.

---

## 4. Primary Metrics

### Accuracy

Accuracy measures the proportion of correctly classified samples.

```text
Accuracy = Correct Predictions / Total Predictions

Accuracy is useful when the classes are reasonably balanced.

5. Precision

Precision measures how many predictions assigned to a particular class are actually correct.

Precision = True Positives / (True Positives + False Positives)

Precision can help identify classes that are frequently predicted incorrectly.

6. Recall

Recall measures how many samples belonging to a class are correctly detected.

Recall = True Positives / (True Positives + False Negatives)

Recall is particularly useful when missing a sign may have practical consequences.

7. F1-Score

The F1-score combines precision and recall.

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Macro F1-score may be particularly useful when the dataset contains multiple classes with different numbers of samples.

8. Confusion Matrix

A confusion matrix will be used to analyze classification errors between sign classes.

Example:

                Predicted
             A    B    C    D

Actual A     ✓    1    0    0
Actual B     0    ✓    2    0
Actual C     1    0    ✓    1
Actual D     0    0    1    ✓

The confusion matrix can reveal signs that are visually similar or frequently confused.

9. Participant-Level Evaluation

Participant-level evaluation is important for this project.

A model that performs well on people already represented in the training dataset may not necessarily generalize to new users.

Therefore, experiments should distinguish between:

Seen participants

Users whose data may have appeared during training.

Unseen participants

Users whose data were not included in training.

Performance on unseen participants should be reported whenever sufficient data are available.

10. Environmental Robustness

The system should eventually be evaluated under different conditions.

Possible variables include:

Lighting
Background
Camera angle
Camera distance
Hand position
Signing speed
Camera quality
Indoor environments
Outdoor environments

The objective is to determine which conditions significantly affect recognition performance.

11. Real-Time Performance

For a future real-time system, evaluation should also consider computational performance.

Relevant measurements include:

Inference time
Frames per second
Model size
Memory usage
CPU usage
Battery consumption when measurable
Time required to produce a prediction

A model with slightly lower accuracy may be preferable if it is significantly faster and more practical on low-resource devices.

12. Mobile Evaluation

When the model is deployed to a mobile device, evaluation should be performed on the target hardware whenever possible.

The evaluation should consider:

Application startup time
Model loading time
Inference latency
Memory consumption
Offline functionality
Device compatibility
Stability during continuous use

The objective is to evaluate not only the model but also the complete user experience.

13. Baseline Models

The project should establish baseline models before experimenting with more complex architectures.

Possible baselines include:

Logistic Regression
Support Vector Machine
Random Forest
K-Nearest Neighbors
Simple neural networks

These baselines provide reference points for evaluating whether more complex approaches actually provide meaningful improvements.

14. Model Comparison

Different models should be compared under comparable experimental conditions.

For each experiment, the project should record:

Model architecture
Input features
Dataset version
Training configuration
Number of classes
Number of samples
Evaluation metrics
Training time
Inference time
Model size
Hardware used

This information will support reproducibility.

15. Error Analysis

Performance metrics alone are not sufficient.

Incorrect predictions should be analyzed to understand why the model fails.

Possible causes include:

Similar hand configurations
Occlusion
Poor lighting
Motion blur
Incorrect landmark detection
Unusual hand orientation
Ambiguous signs
Incorrect annotation
Insufficient training examples
Participant variation

Error analysis will guide future improvements.

16. Ablation Studies

When sufficient data are available, ablation experiments may be conducted.

Examples include comparing:

Raw coordinates vs normalized coordinates
Hand landmarks only vs additional features
Different feature normalization methods
Different model architectures
Different augmentation strategies
Different vocabulary sizes

The purpose is to determine which components actually contribute to model performance.

17. Statistical Considerations

Reported performance should be interpreted in relation to the size and diversity of the test dataset.

When appropriate, the project may report:

Confidence intervals
Standard deviation
Results across multiple runs
Cross-validation results
Per-participant performance

Very small datasets should not be used to make broad claims about real-world performance.

18. Reproducibility

Each reported experiment should be reproducible whenever possible.

The project should record:

Dataset version
Code version
Model version
Random seed
Training parameters
Evaluation parameters
Hardware
Software environment

Experiments should be documented before drawing conclusions from their results.

19. Ethical Evaluation

Technical performance is not the only consideration.

The evaluation should also consider whether the system:

Produces misleading predictions
Performs differently across user groups
Creates unrealistic expectations
Protects user privacy
Clearly communicates its limitations

The system should not be presented as a replacement for human interpreters or professional assistance where such support is required.

20. Limitations

Potential limitations include:

Small datasets
Limited vocabulary
Limited participant diversity
Limited local linguistic resources
Environmental variability
Camera limitations
Landmark detection errors
Dataset bias
Computational constraints

These limitations should be explicitly reported alongside experimental results.

21. Reporting Results

Results should be presented using clear tables and visualizations.

Example:

Model	Accuracy	Precision	Recall	F1-Score	Inference Time
Baseline	TBD	TBD	TBD	TBD	TBD
Model A	TBD	TBD	TBD	TBD	TBD
Model B	TBD	TBD	TBD	TBD	TBD

No performance values should be inserted until they have been experimentally measured.

22. Current Status

The evaluation framework is currently at the planning stage.

Current priorities:

 Define the evaluation protocol
 Establish baseline models
 Prepare the test set
 Implement evaluation metrics
 Generate confusion matrices
 Perform participant-level evaluation
 Analyze classification errors
 Measure inference performance
 Evaluate mobile deployment
 Document experimental results
23. Guiding Principle

The objective is not to maximize a single metric.

The objective is to determine whether the system is:

Accurate
Robust
Generalizable
Efficient
Reproducible
Useful
Appropriate for its intended context

Every performance claim should therefore be supported by experimental evidence.




```text
docs: add evaluation strategy
