# fathomnet-voxel51

**Voxel51 Customer Success Onboarding Project**

This repo contains the workflow and analysis for the [FathomNet 2025 dataset](https://www.kaggle.com/competitions/fathomnet-2025/) (CVPR-FGVC) using [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html). The project simulates a real-world Customer Success scenario involving scientific data curation, hierarchical taxonomy analysis, and "needle-in-a-haystack" visual search for marine research (MBARI).

## Repo Structure

```text
.
├── data/
│   ├── dataset_test.json            # FathomNet Test annotations (COCO format)
│   └── dataset_train.json           # FathomNet Train annotations (COCO format)
├── fathomnet_voxel51/               # Main Python package
│   ├── __init__.py
│   ├── 00_check_gcp_auth.py        # Verify GCP authentication
│   ├── 01_upload_to_gcs.py         # Stream images from FathomNet URLs to GCS
│   ├── 02_ingest_dataset.py        # Ingest dataset into FiftyOne Enterprise
│   ├── 03_add_primary_label.py     # Add aggregated labels for visualization
│   └── debug_labels.py              # Dataset label debugging utility
├── notebooks/
│   ├── 00_fathomnet-eda.ipynb      # Initial EDA and data exploration
│   ├── 01_upload_to_gcp.ipynb      # Example notebook for uploading data to GCS
│   └── 02_ingest_dataset.ipynb     # Example notebook for FiftyOne ingestion
├── docs/
│   ├── ONBOARDING.md                # Project strategy and workflows
│   ├── tasks.md                     # Project task tracking
│   ├── meeting_notes/               # MBARI sync meeting transcripts
│   └── ...                          # Other documentation files
├── pyproject.toml                   # Project dependencies and configuration
├── .pre-commit-config.yaml          # Pre-commit hooks (Ruff, Prettier)
├── CLAUDE.md                        # Claude Code guidance for this repository
├── GCLOUD.md                        # GCP/gsutil commands reference
└── README.md
```

## Project Overview

**Customer Profile:** Marine Research Institute (MBARI)

**Challenge:** Managing 79 hierarchical categories of marine life, identifying mislabeled samples, and discovering anomalies (trash, ROV equipment) in vast amounts of visual data.

**Dataset:** FathomNet 2025 contains 8,981 training + 325 test images (24.15 GiB) with hierarchical taxonomic annotations spanning family → genus → species levels.

**Key Workflows Implemented:**

1. **Cloud-Backed Ingestion:** Efficiently ingesting COCO datasets where images reside in Google Cloud Storage (GCS) without local duplication.

2. **Embeddings & Visualization:** Using CLIP/ResNet to visualize the taxonomic distance between species.

3. **Similarity Search:** Text-to-Image search to distinguish between sub-species (e.g., Octopus rubescens vs. Octopus cyanea).

4. **Zero-Shot Prediction:** Leveraging the [`@voxel51/zero-shot-prediction`](https://docs.voxel51.com/plugins/plugins_ecosystem/zero_shot_prediction.html) plugin to bootstrap labels for unknown objects (e.g., "plastic bag").

## Data Flow Architecture

The project follows a cloud-native architecture where images remain in GCS and only metadata is stored in FiftyOne:

```text
FathomNet URLs
    ↓
[01_upload_to_gcs.py - Async streaming with aiohttp]
    ↓
Google Cloud Storage (gs://voxel51-test/fathomnet/{train,test}_images/)
    ↓
[COCO JSON annotations + GCS paths]
    ↓
[02_ingest_dataset.py - FiftyOne dataset creation]
    ↓
FiftyOne Enterprise Dataset (fathomnet-2025)
    ↓
[03_add_primary_label.py - Label aggregation (optional)]
    ↓
Analysis & Curation
  - Embeddings Visualization
  - Similarity Search
  - Model Evaluation
  - Zero-Shot Prediction
```

**Design Benefits:**

- Cost efficiency (no data duplication)
- Scalability (cloud-native storage)
- No local disk I/O required
- Async processing (~50 concurrent uploads, ~2 images/sec)

## Setup & Installation

### 1. FiftyOne Enterprise PyPI Access (One-time Setup)

This project uses **FiftyOne Enterprise v2.14.1**, which requires authentication to download from the private PyPI repository.

**Add PyPI credentials to your shell profile (one-time setup):**

```bash
# Add to ~/.zshrc (or ~/.bashrc if using bash)
echo 'export UV_EXTRA_INDEX_URL="https://8c7d1077ed792efe@pypi.fiftyone.ai"' >> ~/.zshrc
source ~/.zshrc
```

This one-time setup allows `uv pip install` to automatically authenticate with the FiftyOne PyPI repository.

**Alternative:** If you prefer not to modify your shell profile, the PyPI URL is also stored in `.env` and can be loaded per-session:

```bash
export $(grep UV_EXTRA_INDEX_URL .env | xargs)
```

### 2. Environment

Ensure you have Python 3.10+ installed. It is recommended to use a virtual environment.

```bash
# Create and activate virtual env
uv venv .venv
source .venv/bin/activate
```

### 3. Dependencies

Install dependencies using `uv`:

```bash
uv pip install -e .
```

> _Note: This project requires FiftyOne Enterprise, google-cloud-storage, and standard data science libraries._

### 4. Credentials

You will need the following credentials set in your environment. The project uses `python-dotenv` to load these from a `.env` file in the project root.

1.  Create a file named `.env` in the root directory: `touch .env`
2.  Add the following variables to it:

```env
# FiftyOne Enterprise
FIFTYONE_API_URI="https://<your-deployment>.fiftyone.ai"
FIFTYONE_API_KEY="<your-api-key>"

# GCP Service Account (optional - only if not using ADC)
# GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/gcp_credentials.json"
```

#### GCP Authentication Options

- **Application Default Credentials (ADC)** _(recommended for local development)_: Run `gcloud auth application-default login`. The GCP project is automatically detected from your active gcloud configuration.
- **Service Account Key**: Set `GOOGLE_APPLICATION_CREDENTIALS` to the path of your service account JSON key file. Useful for CI/CD or production environments.

> _Note: The code automatically detects your GCP project from gcloud authentication - no need to set `GOOGLE_CLOUD_PROJECT` environment variable._

To verify your GCP authentication setup, run:

```bash
python -m fathomnet_voxel51.check_gcp_auth
```

## Usage

### Step 1: Upload Images to GCS

Stream images from FathomNet URLs directly to Google Cloud Storage (no local disk needed):

```bash
# Upload all images (~1 hour)
python -m fathomnet_voxel51.upload_to_gcs

# Or test with a subset first
python -m fathomnet_voxel51.upload_to_gcs --limit 100
```

> _Expected runtime: ~1 hour (train: ~63 min, test: ~3 min) at ~2 images/sec._

### Step 2: Ingest into FiftyOne

Create the FiftyOne dataset with both train and test splits. This step only needs to be run **once** - the dataset persists in FiftyOne Enterprise.

```bash
# Ingest full dataset (run once)
python -m fathomnet_voxel51.ingest_dataset

# Test with a subset first (optional)
python -m fathomnet_voxel51.ingest_dataset --limit 10

# Delete and recreate dataset (if needed)
python -m fathomnet_voxel51.ingest_dataset --recreate
```

> _Note: Running without `--recreate` on an existing dataset will skip ingestion. Use `--recreate` to delete and rebuild the dataset from scratch._

### Exploration

To explore the data or perform EDA, check the notebooks in `notebooks/`.

## GCP Commands Reference

For common `gsutil` commands (listing, copying, deleting data in GCS), see [GCLOUD.md](GCLOUD.md).

## Dataset Info

Source: [FathomNet 2025 - CVPR FGVC Competition](https://www.kaggle.com/competitions/fathomnet-2025/data)

- Type: Object Detection
- Classes: 79 (Marine species + supercategories)
- Format: COCO JSON
- Train images: 8,981
- Test images: 325
- Size: 24.15 GiB
