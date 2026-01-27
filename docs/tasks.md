# Tasks: FathomNet 2025 @ FiftyOne Enterprise

**Status**: Repository setup complete, MCP integration pending
**Current Phase**: Testing MCP integration and data exploration
**Last Updated**: 2026-01-27

---

## Overview

This project demonstrates FiftyOne Enterprise capabilities for analyzing the FathomNet 2025 dataset (CVPR-FGVC marine species competition). We're simulating a real-world Customer Success scenario with MBARI, tackling hierarchical classification, data curation, and anomaly detection in underwater imagery.

**Key Workflows**:

1. **Embeddings Visualization & Clustering** - Visualize taxonomic distance between 79 marine species categories
2. **Image & Text Similarity Search** - Text-to-image search to distinguish similar species (e.g., Octopus rubescens vs Octopus cyanea)
3. **Model Evaluation** - Identify label errors using zero-shot prediction compared to ground truth
4. **Zero-Shot Prediction** - Use `@voxel51/zero-shot-prediction` plugin for rapid prototyping

**Dataset**: 8,981 training + 325 test images (24.15 GiB), 79 hierarchical taxonomic categories
**Architecture**: Cloud-native (images in GCS, metadata in FiftyOne Enterprise)

---

## Phase 0: Repository Setup ✅ COMPLETED

- [x] 0.1 Create repository structure and initial scripts
  - [x] `fathomnet_voxel51/00_check_gcp_auth.py` - GCP authentication verification
  - [x] `fathomnet_voxel51/01_upload_to_gcs.py` - Async image uploader to GCS
  - [x] `fathomnet_voxel51/02_ingest_dataset.py` - FiftyOne dataset ingestion
  - [x] `fathomnet_voxel51/03_add_primary_label.py` - Label aggregation for visualization
  - [x] `fathomnet_voxel51/debug_labels.py` - Dataset debugging utility

- [x] 0.2 Configure development environment
  - [x] `pyproject.toml` with all dependencies (FiftyOne 2.14.1, GCS, async libs)
  - [x] `.pre-commit-config.yaml` with Ruff and Prettier hooks
  - [x] `CLAUDE.md` guidance for Claude Code
  - [x] `GCLOUD.md` GCP commands reference

- [x] 0.3 Documentation
  - [x] `README.md` with setup instructions and data flow architecture
  - [x] `docs/ONBOARDING.md` with project strategy and workflows
  - [x] `docs/meeting_notes/` with 6 MBARI sync meeting transcripts
  - [x] `docs/tasks.md` with checkbox-based task tracking

- [x] 0.4 Bug fixes and improvements
  - [x] Fixed corrupted notebook JSON (`01_upload_to_gcp.ipynb`, `02_ingest_dataset.ipynb`)
  - [x] Fixed argument name: `--name` → `--dataset_name` in ingest_dataset.py
  - [x] Renamed scripts with numbered prefixes (00-03) for natural progression

- [x] 0.5 MCP Server Setup
  - [x] Installed `fiftyone-mcp-server==0.1.2`
  - [x] Upgraded FiftyOne Enterprise to 2.14.1
  - [x] Created `update_claude_mcp_config.py` script
  - [x] Updated `~/.claude/claude_desktop_config.json` with credentials

**⚠️ Version Conflict Note**: MCP server requires `fiftyone <2.0` but we have `2.14.1`. Module imports successfully despite mismatch - monitoring for compatibility issues.

---

## Phase 1: MCP Integration Testing

**Goal**: Verify FiftyOne MCP server is properly configured and functional.

### 1.1 Test MCP Server Basic Functionality

- [ ] Test dataset listing
  - [ ] Ask: "List my FiftyOne datasets"
  - [ ] Verify response includes `fathomnet-2025` (if already ingested)

- [ ] Test operator enumeration
  - [ ] Ask: "What FiftyOne operators are available?"
  - [ ] Verify 80+ built-in operators listed

- [ ] Test dataset inspection (if dataset exists)
  - [ ] Ask: "Show me the schema of fathomnet-2025 dataset"
  - [ ] Verify fields: `ground_truth`, `primary_label`, metadata fields

### 1.2 Document MCP Testing Results

- [ ] Create `docs/mcp_testing.md` with:
  - [ ] Test commands executed
  - [ ] Responses received
  - [ ] Any errors or issues encountered
  - [ ] Workarounds for version conflict (if needed)

### 1.3 Resolve Outstanding Items

- [ ] Decision on `docs/README.md` (currently empty and untracked)
  - Option A: Populate with documentation index
  - Option B: Remove (project already has main README.md)

---

## Phase 2: Data Ingestion ✅ COMPLETED (if already done)

**Goal**: Upload images to GCS and ingest dataset into FiftyOne Enterprise.

### 2.1 Verify GCP Authentication

- [ ] Run: `python -m fathomnet_voxel51.check_gcp_auth`
- [ ] Confirm authenticated project ID displayed
- [ ] Verify access to `voxel51-test` bucket

### 2.2 Upload Images to GCS

- [ ] Test with small subset first:
  - [ ] Run: `python -m fathomnet_voxel51.upload_to_gcs --limit 100`
  - [ ] Verify images uploaded to `gs://voxel51-test/fathomnet/{train,test}_images/`

- [ ] Upload full dataset:
  - [ ] Run: `python -m fathomnet_voxel51.upload_to_gcs`
  - [ ] Expected runtime: ~1 hour (~2 images/sec)
  - [ ] Verify completion: ~8,981 train + 325 test images

### 2.3 Ingest into FiftyOne

- [ ] Test with small subset:
  - [ ] Run: `python -m fathomnet_voxel51.ingest_dataset --limit 10`
  - [ ] Verify samples created with `ground_truth` field

- [ ] Ingest full dataset:
  - [ ] Run: `python -m fathomnet_voxel51.ingest_dataset --dataset_name fathomnet-2025`
  - [ ] Verify dataset created with train/test splits
  - [ ] Verify ground_truth detections field populated

### 2.4 Add Primary Labels (Optional)

- [ ] Run: `python fathomnet_voxel51/03_add_primary_label.py fathomnet-2025`
- [ ] Verify `primary_label` field added for embeddings visualization
- [ ] Note: Uses most-common-label aggregation logic

**Implementation Notes**:

- Images remain in GCS; FiftyOne stores only metadata
- No local disk I/O required after upload
- Dataset persists in FiftyOne Enterprise (run ingestion once)

---

## Phase 3: Data Exploration

**Goal**: Use FiftyOne to explore dataset, visualize embeddings, and perform similarity search.

### 3.1 Generate Embeddings

- [ ] Research embedding options:
  - [ ] Check FiftyOne docs for compute embeddings
  - [ ] Options: CLIP (multimodal), ResNet (vision-only)
  - [ ] Consider GPU compute requirements (Modal: $0.10-$0.50/hr)

- [ ] Generate embeddings:
  - [ ] Run FiftyOne embeddings computation
  - [ ] Wait for completion (GPU job)
  - [ ] Verify embeddings field added to all samples

- [ ] Document embedding configuration:
  - [ ] Model used (CLIP vs ResNet)
  - [ ] Embedding dimensions
  - [ ] Compute time and cost

### 3.2 Embeddings Visualization

- [ ] Open FiftyOne App:
  - [ ] Load `fathomnet-2025` dataset
  - [ ] Open embeddings panel
  - [ ] Color by: `primary_label`

- [ ] Analyze clustering patterns:
  - [ ] Do species within same family cluster together?
  - [ ] Are sharks separated from jellyfish?
  - [ ] Identify outliers (potential mislabels)
  - [ ] Screenshot interesting clusters

- [ ] Document findings:
  - [ ] Create `docs/embeddings_analysis.md`
  - [ ] Include screenshots of embeddings visualization
  - [ ] Note taxonomic clustering observations
  - [ ] List outlier samples for review

### 3.3 Text-to-Image Similarity Search

- [ ] Test species distinction queries:
  - [ ] "red octopus" vs "blue octopus"
  - [ ] "tentacles"
  - [ ] "bioluminescence"
  - [ ] "translucent body"

- [ ] Test family-level queries:
  - [ ] "shark"
  - [ ] "jellyfish"
  - [ ] "octopus"

- [ ] Test for anomalies:
  - [ ] "plastic bag"
  - [ ] "trash"
  - [ ] "equipment"
  - [ ] "ROV"

- [ ] Document successful query patterns:
  - [ ] Create `docs/similarity_search_examples.md`
  - [ ] Include query text and top results
  - [ ] Note which queries work well vs poorly
  - [ ] Screenshot interesting results

---

## Phase 4: Model Evaluation

**Goal**: Run zero-shot prediction and compare to ground truth to identify label errors.

### 4.1 Install Zero-Shot Prediction Plugin

- [ ] Install plugin:
  ```bash
  fiftyone plugins download https://github.com/voxel51/zero-shot-prediction-plugin
  ```
- [ ] Verify installation: check available plugins in FiftyOne App

### 4.2 Run Zero-Shot Prediction

- [ ] Configure plugin:
  - [ ] Select model: CLIP or OWL-ViT
  - [ ] Specify 79 FathomNet categories as classes
  - [ ] Choose confidence threshold

- [ ] Run predictions:
  - [ ] Process full dataset (or subset for testing)
  - [ ] Save predictions to new field: `zero_shot_predictions`
  - [ ] Wait for completion (GPU job)

- [ ] Document configuration:
  - [ ] Model used
  - [ ] Class list provided
  - [ ] Confidence threshold
  - [ ] Compute time and cost

### 4.3 Model Evaluation

- [ ] Compute evaluation metrics:
  - [ ] Use FiftyOne's evaluation module
  - [ ] Compare `zero_shot_predictions` vs `ground_truth`
  - [ ] Metrics: precision, recall, F1 (per category and overall)
  - [ ] Generate confusion matrix

- [ ] Identify high-confidence disagreements:
  - [ ] Filter for samples where model != ground truth
  - [ ] Sort by prediction confidence
  - [ ] Create saved view: "potential_label_errors"

- [ ] Manual review:
  - [ ] Review top 50 disagreements
  - [ ] Categorize: true errors, model mistakes, ambiguous cases
  - [ ] Tag confirmed errors with `label_error` tag

### 4.4 Document Evaluation Results

- [ ] Create `docs/model_evaluation.md`:
  - [ ] Overall metrics table (precision/recall/F1 per category)
  - [ ] Confusion matrix visualization
  - [ ] Top 10 most confused categories
  - [ ] Examples of true label errors found
  - [ ] Examples of model mistakes
  - [ ] Analysis of where zero-shot struggles

---

## Phase 5: Label Cleanup

**Goal**: Use bulk editing to correct identified label errors.

### 5.1 Install Bulk Editing Plugin

- [ ] Check if bulk editing plugin available in FiftyOne App
- [ ] If not: research alternative batch editing workflows

### 5.2 Create Cleanup Views

- [ ] Create saved view for confirmed errors:
  - [ ] Filter: `tags` contains "label_error"
  - [ ] Group by predicted category

- [ ] Create saved view for review queue:
  - [ ] High-confidence disagreements not yet reviewed
  - [ ] Sort by confidence descending

### 5.3 Batch Corrections

- [ ] Correct labels for confirmed errors:
  - [ ] Use bulk editing or script-based approach
  - [ ] Update `ground_truth` field
  - [ ] Add tag: `label_corrected`
  - [ ] Track changes in correction log

- [ ] Document corrections:
  - [ ] Create `docs/label_corrections.csv`
  - [ ] Columns: sample_id, old_label, new_label, reason

### 5.4 Validate Cleanup

- [ ] Re-run embeddings visualization:
  - [ ] Check if corrected samples now cluster correctly

- [ ] Re-run model evaluation:
  - [ ] Compare metrics before/after cleanup
  - [ ] Document improvement in precision/recall

---

## Phase 6: Model Training (Future Work)

**Goal**: Fine-tune custom model on cleaned dataset.

### 6.1 YOLO v8 Fine-Tuning

- [ ] Install YOLO v8 trainer plugin
- [ ] Configure training:
  - [ ] Dataset: cleaned `fathomnet-2025`
  - [ ] Train/val split
  - [ ] Hyperparameters
  - [ ] GPU compute (Modal)

- [ ] Run training job:
  - [ ] Monitor training metrics
  - [ ] Track model lineage
  - [ ] Save checkpoints

- [ ] Evaluate on test set:
  - [ ] Compare to zero-shot baseline
  - [ ] Compare to BirdSet-style baselines
  - [ ] Confusion matrix analysis

### 6.2 Custom Model Integration (Research)

- [ ] Research FiftyOne plugin development:
  - [ ] How to integrate non-YOLO models
  - [ ] Plugin API documentation
  - [ ] Example plugins for reference

- [ ] Document custom model workflow:
  - [ ] Create `docs/custom_model_integration.md`
  - [ ] Step-by-step guide
  - [ ] Example code snippets

### 6.3 Hierarchical Classification Exploration

- [ ] Research hierarchical loss functions:
  - [ ] Family → Genus → Species hierarchy
  - [ ] Taxonomic distance metrics

- [ ] Experiment with hierarchical models:
  - [ ] Multi-level classifiers
  - [ ] Compare to flat classification

---

## Phase 7: Documentation and Cleanup

### 7.1 Code Quality

- [ ] Run pre-commit hooks:
  ```bash
  pre-commit run --all-files
  ```
- [ ] Fix any Ruff or Prettier issues
- [ ] Add docstrings to new functions

### 7.2 Update Documentation

- [ ] Update `README.md` with final results
- [ ] Update `docs/ONBOARDING.md` with completed workflows
- [ ] Create `docs/workflow_tutorial.md` with step-by-step guide
- [ ] Consolidate all analysis docs in `docs/`

### 7.3 Meeting Notes Index

- [ ] Create `docs/meeting_notes/README.md`:
  - [ ] Summary of each meeting
  - [ ] Key takeaways and action items
  - [ ] Cross-references to implemented features

### 7.4 Final Commits

- [ ] Commit all documentation and analysis results
- [ ] Tag release: `v1.0-onboarding-complete`
- [ ] Push to repository

---

## Appendix: File Inventory

### Python Package Structure

```
fathomnet_voxel51/
├── __init__.py                     ✅ exists
├── 00_check_gcp_auth.py            ✅ exists - GCP authentication verification
├── 01_upload_to_gcs.py             ✅ exists - Async image uploader (URLs → GCS)
├── 02_ingest_dataset.py            ✅ exists - FiftyOne dataset ingestion
├── 03_add_primary_label.py         ✅ exists - Label aggregation for visualization
└── debug_labels.py                 ✅ exists - Dataset debugging utility
```

### Documentation Files

```
docs/
├── ONBOARDING.md                    ✅ exists - Project strategy and workflows
├── tasks.md                         ✅ exists - This file (checkbox task tracking)
├── README.md                        ⚠️  exists but empty (needs decision)
├── mcp_testing.md                   (new - MCP integration test results)
├── embeddings_analysis.md           (new - Embeddings visualization findings)
├── similarity_search_examples.md    (new - Text-to-image search queries)
├── model_evaluation.md              (new - Zero-shot evaluation results)
├── label_corrections.csv            (new - Correction log)
├── workflow_tutorial.md             (new - Step-by-step guide)
└── meeting_notes/
    ├── README.md                    (new - Meeting notes index)
    ├── 20251205-mbari-success-criteria.md      ✅ exists
    ├── 20251215-mbari-success-criteria-2.md    ✅ exists
    ├── 20251218-mbari-sync.md                  ✅ exists
    ├── 20260108-mbari-sync.md                  ✅ exists
    ├── 20260115-mbari-sync.md                  ✅ exists
    └── 20260122-mbari-sync.md                  ✅ exists
```

### Configuration Files

```
.
├── pyproject.toml                   ✅ exists - Dependencies and metadata
├── .pre-commit-config.yaml          ✅ exists - Ruff + Prettier hooks
├── .env                             (user-created - FiftyOne + GCP credentials)
├── CLAUDE.md                        ✅ exists - Claude Code guidance
├── GCLOUD.md                        ✅ exists - GCP commands reference
└── README.md                        ✅ exists - Main project documentation
```

### Notebooks

```
notebooks/
├── 00_fathomnet-eda.ipynb          ✅ exists - Exploratory Data Analysis
├── 01_upload_to_gcp.ipynb          ✅ exists - Upload workflow example
└── 02_ingest_dataset.ipynb         ✅ exists - Ingestion workflow example
```

### Data Files

```
data/
├── dataset_train.json               ✅ exists - COCO train annotations (8.5 MB)
└── dataset_test.json                ✅ exists - COCO test annotations (299 KB)
```

---

## Quick Reference

**Check GCP authentication**:

```bash
python -m fathomnet_voxel51.check_gcp_auth
```

**Upload images (test with limit)**:

```bash
python -m fathomnet_voxel51.upload_to_gcs --limit 100
```

**Upload full dataset**:

```bash
python -m fathomnet_voxel51.upload_to_gcs
```

**Ingest dataset (test)**:

```bash
python -m fathomnet_voxel51.ingest_dataset --dataset_name fathomnet-2025 --limit 10
```

**Ingest full dataset**:

```bash
python -m fathomnet_voxel51.ingest_dataset --dataset_name fathomnet-2025
```

**Recreate dataset from scratch**:

```bash
python -m fathomnet_voxel51.ingest_dataset --dataset_name fathomnet-2025 --recreate
```

**Add primary labels**:

```bash
python fathomnet_voxel51/03_add_primary_label.py fathomnet-2025
```

**Debug dataset labels**:

```bash
python fathomnet_voxel51/debug_labels.py fathomnet-2025
```

**Run pre-commit hooks**:

```bash
pre-commit run --all-files
```

**Update MCP configuration**:

```bash
python update_claude_mcp_config.py
```

---

## Estimated Timeline

| Phase               | Description             | Time Estimate                   | Status      |
| ------------------- | ----------------------- | ------------------------------- | ----------- |
| Phase 0             | Repository Setup        | ~2-3 hours                      | ✅ Complete |
| Phase 1             | MCP Integration Testing | ~30 minutes                     | Pending     |
| Phase 2             | Data Ingestion          | ~1.5 hours (mostly upload time) | Pending     |
| Phase 3             | Data Exploration        | ~4-6 hours + GPU queue          | Pending     |
| Phase 4             | Model Evaluation        | ~4-6 hours + GPU queue          | Pending     |
| Phase 5             | Label Cleanup           | ~2-4 hours                      | Pending     |
| Phase 6             | Model Training          | ~8-12 hours + GPU queue         | Future Work |
| Phase 7             | Documentation & Cleanup | ~2-3 hours                      | Pending     |
| **Total Remaining** |                         | ~18-28 hours + GPU queue        |             |

**Dependencies**:

- FiftyOne Enterprise access (configured via `.env`)
- GCP authentication (ADC or service account)
- GPU compute for embeddings and model evaluation (Modal or internal)
- FiftyOne MCP server compatibility with 2.14.1 (monitoring)

**Customer Priorities (from meeting notes)**:

1. Label review (embeddings visualization, similarity search) - Phase 3
2. Model evaluation (precision/recall/F1, confusion matrices) - Phase 4
3. Model training (YOLO v8, custom models) - Phase 6

**GPU Compute Pricing (Modal)**:

- Embeddings generation: ~$0.10-$0.50/hr
- Zero-shot prediction: ~$0.10-$0.50/hr
- Model training: varies by model size and epochs
