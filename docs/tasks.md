# Tasks: FathomNet 2025 @ FiftyOne Enterprise

**Current Phase**: Phase 2A - Model Inference Preparation (In Progress)
**Last Updated**: 2026-02-05

See [ONBOARDING.md](./ONBOARDING.md) for project overview and demo workflow.

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
  - [x] `docs/ONBOARDING.md` with project overview and demo workflow
  - [x] `docs/tasks.md` with task tracking

- [x] 0.4 Bug fixes and improvements
  - [x] Fixed corrupted notebook JSON (`01_upload_to_gcp.ipynb`, `02_ingest_dataset.ipynb`)
  - [x] Fixed argument name: `--name` → `--dataset_name` in ingest_dataset.py
  - [x] Renamed scripts with numbered prefixes (00-03) for natural progression
  - [x] Fixed `.env` loading in GCP authentication scripts
  - [x] Documented FiftyOne Enterprise PyPI setup for permanent installation

**⚠️ Note**: FiftyOne MCP server (`fiftyone-mcp-server`) is not compatible with FiftyOne Enterprise 2.14.1 (requires `fiftyone <2.0`). Removed MCP integration from workflow.

---

## Phase 1: Data Ingestion ✅ COMPLETED

**Goal**: Upload images to GCS and ingest dataset into FiftyOne Enterprise.

### 1.1 Verify GCP Authentication

- [x] Run: `python -m fathomnet_voxel51.check_gcp_auth`
- [x] Confirm authenticated project ID displayed
- [x] Verify access to `voxel51-test` bucket

### 1.2 Upload Images to GCS

- [x] Test with small subset first:
  - [x] Run: `python -m fathomnet_voxel51.upload_to_gcs --limit 100`
  - [x] Verify images uploaded to `gs://voxel51-test/fathomnet/{train,test}_images/`

- [x] Upload full dataset:
  - [x] Run: `python -m fathomnet_voxel51.upload_to_gcs`
  - [x] Expected runtime: ~1 hour (~2 images/sec)
  - [x] Verify completion: ~8,981 train + 325 test images

### 1.3 Ingest into FiftyOne

- [x] Test with small subset:
  - [x] Run: `python -m fathomnet_voxel51.ingest_dataset --limit 10`
  - [x] Verify samples created with `ground_truth` field

- [x] Ingest full dataset:
  - [x] Run: `python -m fathomnet_voxel51.ingest_dataset --dataset_name fathomnet-2025`
  - [x] Verify dataset created with train/test splits
  - [x] Verify ground_truth detections field populated

### 1.4 Add Primary Labels (Optional)

- [x] Run: `python fathomnet_voxel51/03_add_primary_label.py fathomnet-2025`
- [x] Verify `primary_label` field added for embeddings visualization
- [x] Note: Uses most-common-label aggregation logic

**Implementation Notes**:

- Images remain in GCS; FiftyOne stores only metadata
- No local disk I/O required after upload
- Dataset persists in FiftyOne Enterprise (run ingestion once)

---

## Phase 2: Data Exploration ✅ 90% COMPLETED

**Goal**: Use FiftyOne to explore dataset, visualize embeddings, and perform similarity search.

### 2.1 Generate Embeddings

- [x] Research embedding options:
  - [x] Check FiftyOne docs for compute embeddings
  - [x] Options: CLIP (multimodal), DINOv2 (vision-only)
  - [x] Consider GPU compute requirements (internal on-prem for production scale)

- [x] Generate embeddings:
  - [x] Run FiftyOne embeddings computation (CLIP + DINOv2)
  - [x] Successfully computed on both fathomnet-test and fathomnet-2025 datasets
  - [x] Verify embeddings field added to all samples

- [x] Document embedding configuration:
  - [x] Models used: CLIP (multimodal), DINOv2 (vision-only)
  - [x] Successfully computed on patches (bounding boxes)
  - [x] Note: GPU delegated operations setup deferred to post-onboarding

**Implementation Notes:**

- Embeddings computed on patches/bounding boxes (ground_truth.detections)
- CLIP enables text-to-image similarity search
- DINOv2 provides robust visual features for marine imagery

### 2.2 Embeddings Visualization ✅ COMPLETED

- [x] Open FiftyOne App:
  - [x] Load `fathomnet-2025` dataset
  - [x] Open embeddings panel
  - [x] Color by: `ground_truth.detections.label`

- [x] Analyze clustering patterns:
  - [x] Species within same family cluster together (visible in embeddings plot)
  - [x] Taxonomic groups show clear separation
  - [x] Identify outliers (potential mislabels visible in sparse regions)
  - [x] Screenshot captured showing 24,487 patches colored by label

**Key Findings:** Embeddings show excellent taxonomic clustering. Species within same family cluster together. Outliers visible as isolated points (potential annotation errors).

### 2.3 Text-to-Image Similarity Search ✅ COMPLETED

- [x] Test species distinction queries:
  - [x] Natural language search working (e.g., "starfish")
  - [x] Can distinguish between species using descriptive text
  - [x] "tentacles", "bioluminescence" queries functional

- [x] Test family-level queries:
  - [x] "shark", "jellyfish", "octopus" queries working
  - [x] CLIP embeddings enable semantic search

- [x] Test for anomalies:
  - [x] Can search for "plastic bag", "trash", "equipment", "ROV"
  - [x] Useful for data quality checks

**Key Findings:** CLIP-based search enables natural language queries. Useful for finding specific characteristics ("translucent body", "tentacles"), distinguishing similar species, and identifying non-biological objects (trash, equipment).

### 2.4 Image Similarity Search ✅ COMPLETED

- [x] Image-based similarity search working
- [x] "Find similar samples" workflow enabled
- [x] Useful for finding duplicates and near-duplicates

**Phase 2 Status:** Core functionality complete and ready for demo.

---

## Phase 2A: Model Inference Preparation (PACE Cluster) 🔄 IN PROGRESS

**Goal**: Prepare to run FathomNet 2025 competition winner model inference on PACE cluster for model evaluation in FiftyOne.

**Context**: Running on Georgia Tech PACE cluster GPU interactive session. No gsutil access available. Need to download images directly from FathomNet URLs and model checkpoints from Google Drive.

**See**: `docs/model_inference_plan.md` for detailed implementation plan.

### 2A.1 Planning and Setup ✅ COMPLETED

- [x] Create implementation plan for PACE cluster environment
  - [x] Document environment constraints (no gsutil, shared storage)
  - [x] Plan data download strategy (FathomNet URLs → local storage)
  - [x] Plan checkpoint download (Google Drive → shared storage)
  - [x] Create `docs/model_inference_plan.md` with 7-phase plan

- [x] Update plan for PACE cluster specifics
  - [x] Storage location: `~/ps-dsgt_clef2026-0/shared/fathomnet-2025/`
  - [x] Dataset size: 8,981 train + 325 test images (~21GB)
  - [x] Checkpoint size: 16GB from Google Drive
  - [x] Total storage needed: ~37GB

### 2A.2 Create Download Infrastructure ✅ COMPLETED

- [x] Create `fathomnet_voxel51/05_download_images_local.py`
  - [x] Async download from FathomNet URLs (from `coco_url` field)
  - [x] Save to local filesystem instead of GCS
  - [x] Resume capability (skip existing files)
  - [x] Progress tracking with tqdm
  - [x] Configurable concurrency (default: 50)

- [x] Add dependencies
  - [x] Add `aiofiles>=24.1.0` to `pyproject.toml`

### 2A.3 Download Data to PACE Storage 📋 NEXT STEPS

- [ ] Create storage directory structure:
  ```bash
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/train_images
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/test_images
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints
  ```

- [ ] Install aiofiles dependency:
  ```bash
  pip install aiofiles
  ```

- [ ] Test download script with small subset:
  ```bash
  python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
    --limit 10
  ```

- [ ] Run full image download (1-2 hours):
  ```bash
  python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025
  ```
  - Expected: 8,981 train + 325 test images (~21GB total)
  - Time estimate: 1-2 hours (network-dependent)

### 2A.4 Download Model Checkpoint 📋 PENDING

**Source**: https://drive.google.com/drive/u/1/folders/1JF5B51CRUr-J_S2GoC-i5D-UmYCXClDk

- [ ] Download 16GB checkpoint using one of these methods:
  - [ ] **Option 1**: `gdown` (if file is publicly shared)
  - [ ] **Option 2**: `rclone` (if configured on PACE)
  - [ ] **Option 3**: Manual download + `scp` to PACE (most reliable)

- [ ] Verify checkpoint saved to:
  ```bash
  ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt
  ```

### 2A.5 Set Up Competition Repository 📋 PENDING

- [ ] Clone competition repo:
  ```bash
  cd ~/clef
  git clone https://github.com/dhlee-work/fathomnet-cvpr2025-ssl.git
  cd fathomnet-cvpr2025-ssl
  ```

- [ ] Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- [ ] Create symlinks to shared storage:
  ```bash
  mkdir -p dataset/fathomnet-2025

  # Link images
  ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/train_images \
        dataset/fathomnet-2025/train_data/images
  ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/test_images \
        dataset/fathomnet-2025/test_data/images

  # Link JSON annotations
  ln -s ~/clef/fathomnet-voxel51/data/dataset_train.json \
        dataset/fathomnet-2025/dataset_train.json
  ln -s ~/clef/fathomnet-voxel51/data/dataset_test.json \
        dataset/fathomnet-2025/dataset_test.json

  # Link checkpoint
  mkdir -p logs/experiment-final014/Fold-0/
  ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt \
        logs/experiment-final014/Fold-0/last.ckpt
  ```

### 2A.6 Run Preprocessing and Inference 📋 PENDING

- [ ] Run preprocessing (generates category mappings):
  ```bash
  python A0.data_preprocess.py
  ```

- [ ] Run inference (2-4 hours on GPU):
  ```bash
  python C1.TestModel.py --config ./config/experiment-final14.yaml
  ```
  - Output: CSV with columns `annotation_id`, `concept_name`
  - Location: `./results/submission_{project_name}_0526_final.csv`

### 2A.7 Import Predictions to FiftyOne 📋 PENDING

- [ ] Create import script: `fathomnet_voxel51/04_import_predictions.py` (see plan)
- [ ] Run import:
  ```bash
  python -m fathomnet_voxel51.04_import_predictions \
    <path-to-predictions.csv> \
    --dataset_name fathomnet-2025 \
    --field model_predictions
  ```
- [ ] Verify predictions imported to FiftyOne dataset

**Implementation Notes:**
- Running on PACE cluster GPU node (not local machine)
- Using shared project storage for data persistence
- Total setup time estimate: 2-3 hours (downloads)
- Total inference time estimate: 2-4 hours (GPU)
- See `docs/model_inference_plan.md` for complete workflow

---

## Phase 3: Model Evaluation

**Goal**: Run zero-shot prediction and compare to ground truth to identify label errors.

**⚠️ Status Update**: Zero-shot prediction plugin (https://github.com/jacobmarks/zero-shot-prediction-plugin) has compatibility issues with current FiftyOne Enterprise platform. UI errors encountered during execution. This phase will be revisited with custom model evaluation workflow using MBARI's existing classifiers.

### 3.1 Install Zero-Shot Prediction Plugin

- [x] Attempted plugin installation
- [x] Identified compatibility issues with platform
- [ ] **DEFERRED**: Will use custom model predictions instead of zero-shot plugin

### 3.2 Run Zero-Shot Prediction

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

### 3.3 Model Evaluation

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

### 3.4 Document Evaluation Results

- [ ] Create `docs/model_evaluation.md`:
  - [ ] Overall metrics table (precision/recall/F1 per category)
  - [ ] Confusion matrix visualization
  - [ ] Top 10 most confused categories
  - [ ] Examples of true label errors found
  - [ ] Examples of model mistakes
  - [ ] Analysis of where zero-shot struggles

---

## Phase 4: Label Cleanup

**Goal**: Use bulk editing to correct identified label errors.

### 4.1 Install Bulk Editing Plugin

- [ ] Check if bulk editing plugin available in FiftyOne App
- [ ] If not: research alternative batch editing workflows

### 4.2 Create Cleanup Views

- [ ] Create saved view for confirmed errors:
  - [ ] Filter: `tags` contains "label_error"
  - [ ] Group by predicted category

- [ ] Create saved view for review queue:
  - [ ] High-confidence disagreements not yet reviewed
  - [ ] Sort by confidence descending

### 4.3 Batch Corrections

- [ ] Correct labels for confirmed errors:
  - [ ] Use bulk editing or script-based approach
  - [ ] Update `ground_truth` field
  - [ ] Add tag: `label_corrected`
  - [ ] Track changes in correction log

- [ ] Document corrections:
  - [ ] Create `docs/label_corrections.csv`
  - [ ] Columns: sample_id, old_label, new_label, reason

### 4.4 Validate Cleanup

- [ ] Re-run embeddings visualization:
  - [ ] Check if corrected samples now cluster correctly

- [ ] Re-run model evaluation:
  - [ ] Compare metrics before/after cleanup
  - [ ] Document improvement in precision/recall

---

## Phase 5: Model Training (Future Work)

**Goal**: Fine-tune custom model on cleaned dataset.

### 5.1 YOLO v8 Fine-Tuning

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

### 5.2 Custom Model Integration (Research)

- [ ] Research FiftyOne plugin development:
  - [ ] How to integrate non-YOLO models
  - [ ] Plugin API documentation
  - [ ] Example plugins for reference

- [ ] Document custom model workflow:
  - [ ] Create `docs/custom_model_integration.md`
  - [ ] Step-by-step guide
  - [ ] Example code snippets

### 5.3 Hierarchical Classification Exploration

- [ ] Research hierarchical loss functions:
  - [ ] Family → Genus → Species hierarchy
  - [ ] Taxonomic distance metrics

- [ ] Experiment with hierarchical models:
  - [ ] Multi-level classifiers
  - [ ] Compare to flat classification

---

## Phase 6: Documentation and Cleanup

### 6.1 Code Quality

- [ ] Run pre-commit hooks: `pre-commit run --all-files`
- [ ] Fix any Ruff or Prettier issues

### 6.2 Update Documentation

- [ ] Update `README.md` with final results
- [ ] Create `docs/workflow_tutorial.md` with step-by-step guide

### 6.3 Final Release

- [ ] Commit all documentation and analysis results
- [ ] Tag release: `v1.0-onboarding-complete`

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
├── 04_import_predictions.py        📋 planned - Import model predictions CSV to FiftyOne
├── 05_download_images_local.py     ✅ exists - Download images from URLs to local storage (PACE)
└── debug_labels.py                 ✅ exists - Dataset debugging utility
```

### Documentation Files

```
docs/
├── ONBOARDING.md                    ✅ exists - Project overview and demo workflow
├── tasks.md                         ✅ exists - This file (task tracking)
├── model_inference_plan.md          ✅ exists - Competition model inference plan (PACE cluster)
├── embeddings_analysis.md           📋 planned
├── similarity_search_examples.md    📋 planned
└── model_evaluation.md              📋 planned
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

---

## Estimated Timeline

| Phase               | Description             | Time Estimate                   | Status      |
| ------------------- | ----------------------- | ------------------------------- | ----------- |
| Phase 0             | Repository Setup        | ~2-3 hours                      | ✅ Complete |
| Phase 1             | Data Ingestion          | ~1.5 hours (mostly upload time) | ✅ Complete |
| Phase 2             | Data Exploration        | ~4-6 hours + GPU queue          | In Progress |
| Phase 3             | Model Evaluation        | ~4-6 hours + GPU queue          | Pending     |
| Phase 4             | Label Cleanup           | ~2-4 hours                      | Pending     |
| Phase 5             | Model Training          | ~8-12 hours + GPU queue         | Future Work |
| Phase 6             | Documentation & Cleanup | ~2-3 hours                      | Pending     |
| **Total Remaining** |                         | ~16-26 hours + GPU queue        |             |

**Dependencies**:

- FiftyOne Enterprise access (configured via `.env`)
- GCP authentication (ADC or service account)
- GPU compute for embeddings and model evaluation (Modal or internal)

**Priority Order** (workflow sequence):

1. Label review (embeddings visualization, similarity search) - Phase 2
2. Model evaluation (precision/recall/F1, confusion matrices) - Phase 3
3. Model training (YOLO v8, custom models) - Phase 5
