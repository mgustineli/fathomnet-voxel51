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

### 5. Model Inference (PACE Cluster) ✅

**Goal:** Run competition winner model on test set and import predictions into FiftyOne

- Ran [FathomNet 2025 competition winner](https://github.com/dhlee-work/fathomnet-cvpr2025-ssl) on Georgia Tech PACE cluster (RTX 6000 GPU)
- Downloaded 9,210 images + 16GB checkpoint to shared cluster storage
- Inference pipeline in `inference/` directory with SLURM job scripts
- **Result:** 788 predictions across 79 categories in ~1.5 min inference time
- Predictions imported into FiftyOne as `model_predictions` field on test samples
- Enables side-by-side comparison of `ground_truth` vs `model_predictions`

**Value:** Enables model evaluation with `dataset.evaluate_detections()` for precision/recall/F1

### 6. Model Evaluation (Next Up)

**Goal:** Identify label errors using model predictions vs ground truth

- Interactive confusion matrices
- Precision/recall/F1 metrics per category
- High-confidence disagreement detection (model vs ground truth)
- Create saved views for potential label errors

### 7. Complete Pipeline (Roadmap)

```
Data Ingestion → Embeddings → Label Review → Model Inference → Evaluation → Iteration
```

Future work: YOLO v8 trainer, model lineage/traceability, hierarchical classification

---

## Technical Notes

**Model Inference:** The zero-shot prediction plugin ([jacobmarks/zero-shot-prediction-plugin](https://github.com/jacobmarks/zero-shot-prediction-plugin)) had compatibility issues with FiftyOne Enterprise. We replaced it with the actual competition winner model running on the PACE GPU cluster, which provides higher-quality predictions for evaluation.
