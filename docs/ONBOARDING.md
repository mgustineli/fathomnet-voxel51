# Murilo Gustineli Onboarding Project – FathomNet 2025 @ CVPR-FGVC

**Kaggle Dataset:** https://www.kaggle.com/competitions/fathomnet-2025/

**FathomNet Database:** https://database.fathomnet.org/fathomnet/#/

## Introduction

Consider marine wildlife monitoring in coastal waters near California. Daily video footage analyzed by a standard ML model shows 2 octopuses, 1 shark, and 10 jellyfish - broad taxonomic categories. But species-level identification could reveal crucial details. Is that an Octopus rubescens, commonly found in this area, or is it an Octopus cyanea usually only observed in warm, tropical waters near Hawai'i? Accurate species classification is essential for understanding ocean ecosystems.

Hierarchical classification—architectures that structure data to capture relationships across taxonomic ranks (e.g., from broad categories like families to specific species)—can significantly improve classification accuracy, as demonstrated by [recent advances](https://imageomics.github.io/bioclip/) in machine learning. In the field of marine ecology, accurate taxonomic classification is essential for addressing fundamental questions: What species exist in a particular place? What is the ecosystem biodiversity and how does it change over time? Questions like these motivate the focus of our 2025 FathomNet Competition, aiming to push the boundaries of taxonomic accuracy and inspire innovative solutions in this space.

## Dataset

The dataset is curated data from the broader [FathomNet Database](https://database.fathomnet.org/fathomnet/#/) image set to tackle hierarchical classification. The training set contains 79 categories of marine animals of varying taxonomic ranks (e.g., family, genus, species), wherein 300 example instances of each category are provided for training. The test set contains the same 79 categories, where roughly 10 example instances of each category are provided for evaluation. The challenge is to develop a model that can accurately classify these taxa and ideally leverage their taxonomic information to do so. Developing these solutions for ocean research will enable scientists to process and explore ocean data more efficiently.

## Strategy

I am acting as a Support Engineer for a marine research institute (like MBARI). They are struggling with Hierarchical Classification—confusing similar species across different families. They have 79 categories and need to clean their data before training a model.

### Proposed Workflow:

#### 1. Embedding Visualization & Clustering

- **Goal:** Visualize the "visual distance" between the 79 categories.
- **Why:** Demonstrate if the "families" of marine animals cluster together naturally. Do sharks cluster away from jellyfish?

#### 2. Image & Text Similarity Search

- **Goal:** Solve the "Needle in a Haystack" problem.
- **Why:** Use natural language search to find "red octopus" vs "blue octopus" to help distinguish between specific species like Octopus rubescens and Octopus cyanea.

#### 3. Model Evaluation

- **Goal:** Identify label errors.
- **Why:** Since the dataset relies on contributors, are there mislabeled images? Use a pre-trained model (or Zero-Shot) to find where the model disagrees with the ground truth.

#### 4. Community Plugin: Zero-Shot Prediction

- **Plugin:** @voxel51/zero-shot-prediction (using CLIP/OWL-ViT).
- **Goal:** Attempt to classify the 79 categories without training a custom model.
- **Why:** This is a powerful "Time to Value" demo for customers. It shows how they can get preliminary labels instantly.
