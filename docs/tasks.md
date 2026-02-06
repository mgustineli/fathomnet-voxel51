# Tasks: FathomNet 2025 @ FiftyOne Enterprise

**Current Phase**: Phase 2A.7 - Import Predictions to FiftyOne (Next Up)
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

## Phase 2A: Model Inference (PACE Cluster) ✅ 95% COMPLETED

**Goal**: Run FathomNet 2025 competition winner model inference on PACE cluster for model evaluation in FiftyOne.

**Context**: Running on Georgia Tech PACE cluster GPU nodes via SLURM. Images and checkpoint stored in shared project storage. Inference pipeline lives in `inference/` directory.

**See**: `docs/model_inference_plan.md` for detailed implementation plan.

**Current Status (2026-02-05)**:
- ✅ All data downloaded (9,210 images + 16GB checkpoint)
- ✅ Inference pipeline created (`inference/` directory with pyproject.toml, run_inference.py, sbatch scripts)
- ✅ Tokenizers/transformers dependency issue resolved (UV_LINK_MODE=copy + --no-cache)
- ✅ Inference completed successfully: **788 predictions, ~1.5 min on RTX 6000**
- ✅ Results saved: `inference/results/submission_experiment-final014.csv`
- 📋 **NEXT**: Import predictions to FiftyOne Enterprise (Task 2A.7)

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

### 2A.3 Download Data to PACE Storage ✅ COMPLETED

- [x] Create storage directory structure:
  ```bash
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/train_images
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/test_images
  mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints
  ```

- [x] Install aiofiles dependency:
  ```bash
  uv pip install -e .  # Installs aiofiles from pyproject.toml
  ```

- [x] Test download script with small subset:
  ```bash
  python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
    --limit 5
  ```
  - Result: Successfully downloaded 5 train + 5 test images

- [x] Run full image download:
  ```bash
  python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025
  ```
  - **Result: 8,885 train images (24GB) + 325 test images (885MB)**
  - **Missing: 96 train images (unavailable on FathomNet servers - 404 errors)**
  - **Success rate: 98.9% (8,885/8,981 train), 100% (325/325 test)**
  - Total: 9,210 images (~25GB)

### 2A.4 Download Model Checkpoint ✅ COMPLETED

**Source**: https://drive.google.com/file/d/1dr0BQJm2G9edhJNRu9vaUCdA4lMNeeRo/view

- [x] Install gdown:
  ```bash
  uv pip install gdown
  ```

- [x] Download 16GB checkpoint using gdown:
  ```bash
  gdown 1dr0BQJm2G9edhJNRu9vaUCdA4lMNeeRo \
    -O ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt
  ```
  - **Result: Successfully downloaded 16GB checkpoint**

- [x] Verify checkpoint saved:
  ```bash
  ls -lh ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt
  # Output: -rw-r--r--. 1 mgustineli3 pace-ps-dsgt_clef2026 16G
  ```

### 2A.5 Set Up Competition Repository ✅ COMPLETED

- [x] Clone competition repo:
  ```bash
  cd ~/clef
  git clone https://github.com/dhlee-work/fathomnet-cvpr2025-ssl.git
  cd fathomnet-cvpr2025-ssl
  ```

- [x] Install dependencies:
  ```bash
  source /tmp/fathomnet-venv/bin/activate
  uv pip install -r requirements.txt
  uv pip install fathomnet  # Additional dependency not in requirements.txt
  ```
  - **Result: 45 packages installed in ~6 minutes (includes PyTorch + CUDA)**

- [x] Create directory structure and symlinks:
  ```bash
  # Create directories
  mkdir -p dataset/fathomnet-2025/train_data
  mkdir -p dataset/fathomnet-2025/test_data
  mkdir -p logs/experiment-final014/Fold-0/
  mkdir -p results

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
  ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt \
        logs/experiment-final014/Fold-0/last.ckpt
  ```
  - **Result: All symlinks created successfully**

### 2A.6 Create Inference Pipeline and Run Inference ✅ COMPLETED

- [x] Created inference pipeline (`inference/` directory):
  - [x] `inference/run_inference.py` - Main inference script wrapping competition code
    - Clones competition repo, applies patches (UUID filename fix, checkpoint path fix)
    - Configurable paths via CLI args (data, annotations, checkpoint, output)
    - Credits original repo: `dhlee-work/fathomnet-cvpr2025-ssl`
  - [x] `inference/pyproject.toml` - Dependencies for uv (PyTorch installed separately with CUDA)
  - [x] `inference/sbatch/_job.sh` - SLURM job script (follows birdclef-2026 pattern)
    - Per-job venv in `$TMPDIR`, `UV_LINK_MODE=copy`, PyTorch CUDA from cu121 index
    - Tokenizers workaround: `--reinstall --no-cache` to avoid corrupted cache
    - Import verification step before running inference
  - [x] `inference/sbatch/run.sh` - Launcher with `--dry-run` support

- [x] Resolved tokenizers dependency issue:
  - **Root cause**: `UV_LINK_MODE` hardlink failure on PACE cluster (cross-filesystem storage)
  - **Symptoms**: `ImportError: cannot import name 'Tokenizer' from 'tokenizers' (unknown location)` - package directory exists but `.so` files are empty
  - **Fix**: `export UV_LINK_MODE=copy` globally + `uv pip install --reinstall --no-cache tokenizers==0.21.4`

- [x] Resolved additional issues discovered during testing:
  - Missing `torchvision` dependency (not in competition requirements.txt)
  - Hardcoded checkpoint path: `~/Project/cvprcom/logs/` → `./logs/`
  - Image filename mismatch: numeric IDs (`1.png`) vs UUID filenames (`000b8e39-...png`)

- [x] Copied preprocessing artifacts to shared storage:
  ```
  ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/preprocessing/
  ├── dist_categories.csv
  ├── dist_categories_debug.csv
  ├── hierarchical_label.csv
  └── hierachical_labelencoder.pkl
  ```

- [x] Run inference on PACE cluster:
  ```bash
  cd inference
  bash sbatch/run.sh
  ```
  - **Result: 788 predictions in ~1.5 min inference time (3:48 total wall time)**
  - GPU: RTX 6000, 8 CPUs, 64GB RAM
  - Output: `inference/results/submission_experiment-final014.csv`
  - Columns: `annotation_id`, `concept_name` (79 categories)

### 2A.7 Import Predictions to FiftyOne 📋 NEXT UP

- [x] Import script already exists: `fathomnet_voxel51/04_import_predictions.py`
- [ ] Run import (requires FiftyOne Enterprise access - local machine or login node with `.env`):
  ```bash
  python -m fathomnet_voxel51.04_import_predictions \
    inference/results/submission_experiment-final014.csv \
    --dataset fathomnet-2025 \
    --field model_predictions
  ```
- [ ] Verify in FiftyOne App:
  - [ ] `model_predictions` field appears in dataset schema
  - [ ] 788 predictions matched to test set annotations
  - [ ] Predictions visible as overlays alongside `ground_truth`

**How it works:**
- CSV has `annotation_id` + `concept_name` (predicted species)
- Script matches each prediction to a ground truth detection by `annotation_id`
- Creates a parallel `model_predictions` Detections field with same bounding boxes but model's labels
- Enables visual comparison and `dataset.evaluate_detections()` for precision/recall/F1

**Implementation Notes:**
- Inference pipeline: `inference/` directory (run_inference.py + sbatch scripts)
- Actual inference time: ~1.5 min on RTX 6000 (~3:48 total including setup)
- Preprocessing artifacts stored in shared PACE storage for reproducibility

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

### Inference Pipeline

```
inference/
├── pyproject.toml                   ✅ exists - Dependencies for uv (PyTorch installed separately)
├── run_inference.py                 ✅ exists - Main inference script (wraps competition code)
├── results/
│   └── submission_experiment-final014.csv  ✅ exists - 788 predictions on test set
└── sbatch/
    ├── _job.sh                      ✅ exists - SLURM job script (RTX 6000, 4hr, 64GB)
    └── run.sh                       ✅ exists - Launcher with --dry-run support
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
