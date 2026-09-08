# Dataset Strategy

## 1. Purpose

The dataset is a central component of Ichara AI Tchad.

The quality, diversity, representativeness, and documentation of the dataset will directly influence the reliability of the sign recognition system.

The initial objective is to build and evaluate a dataset suitable for isolated sign recognition in a controlled research setting.

The project does not assume that a single homogeneous "Chadian Sign Language" exists. The linguistic and community context must be investigated and validated with relevant users, practitioners, and, when possible, sign-language specialists.

---

## 2. Initial Dataset Scope

The first version of the project will focus on a limited vocabulary of isolated signs.

The dataset may progressively include:

- Common everyday signs
- Basic communication signs
- Numbers
- Letters where appropriate
- Administrative vocabulary
- Healthcare-related vocabulary
- Education-related vocabulary
- Emergency-related vocabulary
- Frequently used expressions

The vocabulary will initially remain limited in order to make the research process measurable and reproducible.

The vocabulary can be expanded progressively after validating the first recognition experiments.

---

## 3. Dataset Sources

Potential data sources include:

- Publicly available sign-language datasets
- Research datasets
- Open computer-vision datasets
- Custom data collected specifically for this project
- Community-contributed data, when appropriate and ethically authorized

Each dataset source must be documented before being used.

For every external dataset, the project should record:

- Dataset name
- Source
- URL or reference
- License
- Language or sign-language variety
- Number of classes
- Number of samples
- Collection conditions
- Known limitations
- Date of access

Public datasets will primarily be used for research, experimentation, benchmarking, and methodology development when their characteristics are compatible with the project.

They should not automatically be considered representative of the Chadian context.

---

## 4. Custom Data Collection

A custom dataset may be developed to better represent the Chadian context.

Data collection should consider diversity in:

- Participants
- Hand shapes
- Skin tones
- Age groups
- Gender representation
- Signing styles
- Camera devices
- Lighting conditions
- Backgrounds
- Camera angles
- Distance from the camera
- Hand position
- Signing speed

The objective is to reduce bias and improve the robustness of the future system.

The project will avoid collecting unnecessary personal information.

---

## 5. Ethics and Consent

Any custom dataset involving identifiable participants must be collected with appropriate consent.

Participants should understand:

- The purpose of the research
- How their data will be used
- Whether the data will be publicly released
- Whether their images or videos will be stored
- How long the data may be retained
- Their rights regarding participation

Raw videos or images containing identifiable individuals should not be published publicly on GitHub without appropriate authorization.

Whenever possible, derived representations such as anonymized landmarks may be preferred for experimentation and public release.

---

## 6. Privacy

Privacy is an important principle of Ichara AI Tchad.

The project should avoid storing unnecessary personally identifiable information.

Participant identifiers should be pseudonymous.

For example:

```text
participant_001
participant_002
participant_003

Personal information such as:

Full name
Telephone number
Address
Identification documents
Private contact information

should not be included in the public dataset.

7. Annotation Protocol

Each sample should have a clear and consistent label.

A possible annotation structure is:

sample_id
label
participant_id
source
language_or_variety
capture_condition
device
split

Example:

sample_0001
hello
participant_001
custom
to_be_validated
indoor
smartphone
train

The annotation protocol should be documented before large-scale data collection begins.

Ambiguous or uncertain samples should be flagged rather than arbitrarily assigned to a class.

8. Dataset Structure

The repository will organize data according to the following structure:

data/
├── raw/
│   └── .gitkeep
│
├── processed/
│   └── .gitkeep
│
└── landmarks/
    └── .gitkeep
data/raw/

Contains original research data.

This directory should normally remain outside the public repository when the files contain identifiable participants or have restrictive licenses.

data/processed/

Contains cleaned or transformed data prepared for experiments.

data/landmarks/

Contains extracted hand or body landmark representations used by machine-learning experiments.

9. Train / Validation / Test Split

The dataset should be divided into:

Training set
Validation set
Test set

An example configuration is:

Training:   70%
Validation: 15%
Testing:    15%

These percentages are only an initial reference and may change depending on the final dataset.

Participant-level separation

When multiple samples come from the same participant, samples from the same participant should preferably remain within the same split.

For example:

Participant 001 → Training
Participant 002 → Training
Participant 003 → Validation
Participant 004 → Test

This helps reduce data leakage and provides a more realistic evaluation of generalization to unseen users.

10. Class Balance

The dataset should be monitored for class imbalance.

If one sign has significantly more samples than another, the model may become biased toward the majority class.

Possible strategies include:

Additional data collection
Data augmentation
Class weighting
Controlled sampling
Evaluation using balanced metrics

The final strategy will depend on the characteristics of the dataset.

11. Data Quality Control

Before training, samples should be checked for:

Incorrect labels
Duplicate samples
Corrupted files
Poor image quality
Missing data
Occluded hands
Incorrect framing
Excessive motion blur
Ambiguous signs
Inconsistent annotations

Low-quality or ambiguous samples should be reviewed or removed according to a documented procedure.

12. Diversity and Generalization

A useful dataset should represent realistic operating conditions.

The research should therefore investigate variations such as:

Lighting
Bright environments
Low-light environments
Natural light
Artificial light
Background
Plain backgrounds
Indoor environments
Outdoor environments
Complex backgrounds
Camera
Smartphone cameras
Different resolutions
Different camera positions
Signing conditions
Different distances
Different orientations
Different signing speeds
Different users

These variations are important because the final system is intended to operate beyond a perfectly controlled laboratory environment.

13. Data Augmentation

When appropriate, data augmentation may be used to increase variability during training.

Possible techniques include:

Small rotations
Scaling
Translation
Cropping
Controlled brightness variations
Controlled contrast variations
Horizontal transformations when linguistically valid

Augmentation must be applied carefully.

A transformation should never change the meaning of a sign.

14. Landmark-Based Representation

The project may use hand landmarks extracted with computer-vision tools such as MediaPipe.

A hand representation can contain 21 landmarks, with coordinates such as:

x
y
z

These landmarks can then be normalized and transformed into numerical features for machine-learning experiments.

The landmark representation may provide advantages such as:

Reduced storage requirements
Faster experimentation
Better privacy compared with raw images
Compatibility with lightweight models

However, landmark extraction errors must also be evaluated.

15. Dataset Versioning

Dataset modifications should be traceable.

Example:

Dataset v0.1
Dataset v0.2
Dataset v0.3
Dataset v1.0

Each version should document:

Number of classes
Number of samples
New participants
Removed samples
Label changes
Preprocessing changes
Known limitations

This will make experiments more reproducible.

16. Data Provenance

Every external or custom dataset should have a clear provenance.

The project should be able to answer:

Where did this sample come from?

and:

Under what conditions can this sample be used?

For this reason, dataset documentation should include information about:

Origin
Collection method
License
Consent
Annotation process
Transformation history
17. Scientific Reproducibility

Dataset preparation should be reproducible whenever possible.

The project should document:

Preprocessing procedures
Feature extraction procedures
Dataset splits
Random seeds when applicable
Augmentation techniques
Dataset versions
Experimental configurations

This will allow future experiments to be compared under controlled conditions.

18. Limitations

The dataset may initially have important limitations.

Possible limitations include:

Small number of participants
Limited vocabulary
Limited geographical representation
Limited environmental diversity
Limited availability of locally relevant sign-language resources
Possible linguistic variation
Dataset imbalance
Limited access to high-quality annotated data

These limitations must be explicitly reported rather than hidden.

19. Future Expansion

The dataset may progressively expand toward:

Larger vocabularies
Continuous sign recognition
More participants
More realistic environments
Multimodal recognition
Body and facial landmarks
Video-based temporal modeling
Community-validated sign vocabulary
Mobile-oriented datasets

In the long term, the research may also investigate translation and accessibility support involving French, Arabic, and potentially local Chadian languages.

This multilingual direction is a future research objective and is not considered an implemented feature of the current project.

20. Current Status

The dataset is currently at the research-planning stage.

Current priorities:

 Define the initial vocabulary
 Identify relevant public datasets
 Review dataset licenses
 Define annotation guidelines
 Define ethical and consent procedures
 Design the custom data collection protocol
 Prepare preprocessing procedures
 Establish train/validation/test rules
 Establish dataset versioning
 Conduct initial experiments
 Evaluate dataset limitations

No dataset size or model performance is claimed at this stage.

21. Guiding Principle

The goal is not simply to collect a large amount of data.

The goal is to build a dataset that is:

Relevant
Diverse
Ethically collected
Well documented
Reproducible
Scientifically useful
Representative of the intended users and context

The quality and relevance of the data are considered more important than the raw quantity of samples.


###  Commit

**Commit message :**
```text
docs: add dataset strategy
