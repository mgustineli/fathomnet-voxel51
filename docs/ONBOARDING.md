# FathomNet 2025 @ FiftyOne Enterprise

> Onboarding project demonstrating FiftyOne Enterprise capabilities for marine species classification

**Links:**

- [Kaggle Competition](https://www.kaggle.com/competitions/fathomnet-2025/)
- [FathomNet Database](https://database.fathomnet.org/fathomnet/#/)

## Project Overview

This repository demonstrates FiftyOne Enterprise capabilities for analyzing the FathomNet 2025 dataset (CVPR-FGVC marine species competition). The project simulates a Customer Success scenario with a marine research organization tackling hierarchical classification, data curation, and anomaly detection in underwater imagery.

| Metric          | Value                                    |
| --------------- | ---------------------------------------- |
| Training Images | 8,981                                    |
| Test Images     | 325                                      |
| Total Size      | 24.15 GiB                                |
| Categories      | 79 (family → genus → species)            |
| Architecture    | Cloud-native (GCS + FiftyOne Enterprise) |

**Core Challenges:**

- Distinguishing visually similar species across taxonomic ranks
- Identifying mislabeled samples at scale
- Discovering anomalies (trash, ROV equipment) in vast underwater footage

---

## Problem Context

Marine wildlife monitoring produces vast amounts of underwater footage. A standard ML model might identify "2 octopuses, 1 shark, 10 jellyfish"—but species-level identification reveals crucial ecological details. Is that an _Octopus rubescens_ (common locally) or an _Octopus cyanea_ (typically found in tropical waters near Hawai'i)?

**Why This Matters:**

- Accurate taxonomic classification answers fundamental questions: What species exist here? How does biodiversity change over time?
- [Hierarchical classification](https://imageomics.github.io/bioclip/) leverages taxonomic relationships to improve accuracy
- Data quality (label review) is the primary bottleneck—not model training

---

## Demo Workflow

### 1. Embeddings Visualization ✅

**Goal:** Visualize taxonomic distance between 79 marine species categories

- Embeddings computed with CLIP + DINOv2 on 24,487 patches (bounding boxes)
- Interactive lasso selection for exploring clusters
- Species within same family cluster together naturally
- Outliers visible as isolated points (potential mislabels)

**Value:** Visual exploration reveals annotation errors at a glance

### 2. Text-to-Image Similarity Search ✅

**Goal:** Find specific samples using natural language queries

Example queries:

- Species distinction: "red octopus" vs "blue octopus"
- Feature-based: "tentacles", "bioluminescence", "translucent body"
- Anomaly detection: "plastic bag", "trash", "ROV equipment"

**Value:** Natural language search helps experts find needles in haystacks

### 3. Image Similarity Search ✅

**Goal:** Find visually similar samples for deduplication and rare class discovery

- Select a sample, find top-N similar samples
- Identify duplicates/near-duplicates across deployments
- Discover more examples of rare species

**Value:** Accelerates discovery and data quality assessment

### 4. Bulk Label Editing ✅

**Goal:** Efficiently review and correct thousands of labels

- Custom plugin with lasso selection in embeddings view
- Two modes: change selected samples OR change view excluding selections
- Single operation replaces 5+ clicks per manual change
- Snapshot feature for version control

**Value:** Reduces label review from hours to minutes

### 5. Model Evaluation (Future)

**Goal:** Identify label errors using model predictions vs ground truth

- Interactive confusion matrices
- Precision/recall/F1 metrics per category
- Scenario analysis (performance by collection, season, depth)
- High-confidence disagreement detection

**Status:** Will use custom model predictions (zero-shot plugin has compatibility issues)

### 6. Complete Pipeline (Roadmap)

```
Data Ingestion → Embeddings → Label Review → Model Training → Evaluation → Iteration
```

Future work: GPU compute integration, YOLO v8 trainer, model lineage/traceability

---

## Technical Notes

**Zero-Shot Prediction Plugin:** The community plugin ([jacobmarks/zero-shot-prediction-plugin](https://github.com/jacobmarks/zero-shot-prediction-plugin)) has compatibility issues with the current FiftyOne Enterprise platform. Model evaluation will use custom classifiers instead.
