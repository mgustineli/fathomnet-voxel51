# Plan: FathomNet Competition Model Predictions Integration

## Goal

Run inference using the FathomNet 2025 competition winner model externally, then import predictions into FiftyOne Enterprise for model evaluation.

## Approach

**External inference → CSV → FiftyOne import** (simplest path)

**Competition Repo:** https://github.com/dhlee-work/fathomnet-cvpr2025-ssl
**Checkpoint:** 16GB model file on Google Drive: https://drive.google.com/drive/u/1/folders/1JF5B51CRUr-J_S2GoC-i5D-UmYCXClDk

## Environment

**Running on:** Georgia Tech PACE cluster (GPU interactive session)
**Storage:** `~/ps-dsgt_clef2026-0/shared/fathomnet-2025/` (shared project directory)
**Limitations:** No gsutil access (must download images directly from FathomNet URLs)

**Dataset Size:**
- Train: 8,981 images (~20GB)
- Test: 325 images (~1GB)
- Total: ~21GB + 16GB checkpoint = ~37GB

---

## Phase 1: Set Up Storage Structure

### 1.1 Create directory structure in shared project space

```bash
# Create directories for images and checkpoints
mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/train_images
mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/test_images
mkdir -p ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints
```

---

## Phase 2: Download Model Checkpoint from Google Drive

**Source:** https://drive.google.com/drive/u/1/folders/1JF5B51CRUr-J_S2GoC-i5D-UmYCXClDk

**Options:**

1. **Using gdown (if file is publicly shared):**
   ```bash
   pip install gdown
   gdown --id <file_id> -O ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt
   ```

2. **Using rclone (if configured):**
   ```bash
   rclone copy gdrive:/path/to/last-002.ckpt ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/
   ```

3. **Manual transfer (most reliable):**
   ```bash
   # On local machine: download from Google Drive, then:
   scp last-002.ckpt user@pace-login.pace.gatech.edu:~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/
   ```

---

## Phase 3: Download Images from FathomNet URLs

### 3.1 Create download script

**New file:** `fathomnet_voxel51/05_download_images_local.py`

Downloads images directly from FathomNet URLs (from `coco_url` field in JSON) to local storage.

```bash
# Download all images
python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
    --train_json data/dataset_train.json \
    --test_json data/dataset_test.json

# Test with limited images first
python -m fathomnet_voxel51.05_download_images_local \
    --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
    --limit 100
```

**Time estimate:** 1-2 hours for all 9,306 images (network-dependent)

---

## Phase 4: Clone and Configure Competition Repo

### 4.1 Clone repo

```bash
cd ~/clef
git clone https://github.com/dhlee-work/fathomnet-cvpr2025-ssl.git
cd fathomnet-cvpr2025-ssl
```

### 4.2 Install dependencies

```bash
pip install -r requirements.txt
# Key deps: pytorch-lightning, transformers, omegaconf
```

### 4.3 Set up directory structure with symlinks

The competition script expects:

```
fathomnet-cvpr2025-ssl/
├── dataset/fathomnet-2025/
│   ├── train_data/images/    # Symlink to shared storage
│   ├── test_data/images/     # Symlink to shared storage
│   ├── dataset_train.json    # Symlink to our JSON
│   └── dataset_test.json     # Symlink to our JSON
├── logs/experiment-final014/Fold-0/last.ckpt  # Symlink to checkpoint
└── results/                  # Output directory (auto-created)
```

**Create symlinks:**

```bash
# Create dataset directory
mkdir -p dataset/fathomnet-2025

# Symlink images from shared storage
ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/train_images dataset/fathomnet-2025/train_data/images
ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/test_images dataset/fathomnet-2025/test_data/images

# Symlink annotation JSON files
ln -s ~/clef/fathomnet-voxel51/data/dataset_train.json dataset/fathomnet-2025/dataset_train.json
ln -s ~/clef/fathomnet-voxel51/data/dataset_test.json dataset/fathomnet-2025/dataset_test.json

# Symlink checkpoint
mkdir -p logs/experiment-final014/Fold-0/
ln -s ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt logs/experiment-final014/Fold-0/last.ckpt
```

### 4.4 Run preprocessing (generates category mappings)

```bash
python A0.data_preprocess.py
# Creates: results/dist_categories_debug.csv, results/hierarchical_label.csv, etc.
```

---

## Phase 5: Run Inference

### 2.1 Modify C1.TestModel.py for training set predictions (optional)

By default, the script runs on test data. To get predictions on training data:

- Change `test_anno_path` to `'./dataset/fathomnet-2025/dataset_train.json'`
- Change image path in `datautils.py` `__getitem__` to use train_data

### 2.2 Run inference

```bash
python C1.TestModel.py --config ./config/experiment-final14.yaml
```

### 2.3 Output

Creates CSV at `./results/submission_{project_name}_0526_final.csv` with columns:
| Column | Description |
|--------|-------------|
| `annotation_id` | Links to COCO annotation ID |
| `concept_name` | Predicted species label |

---

## Phase 6: Import Predictions into FiftyOne

### 3.1 Create import script

**New file:** `fathomnet_voxel51/04_import_predictions.py`

```python
"""
Import model predictions from CSV into FiftyOne dataset.

USAGE:
    python -m fathomnet_voxel51.04_import_predictions predictions.csv
    python -m fathomnet_voxel51.04_import_predictions predictions.csv --field model_predictions
"""
import argparse
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from fathomnet_voxel51.setup_fiftyone_credentials import setup_fiftyone_credentials
setup_fiftyone_credentials("murilo")

import fiftyone as fo
from tqdm import tqdm

def import_predictions(
    csv_path: str,
    dataset_name: str = "fathomnet-2025",
    prediction_field: str = "model_predictions",
):
    # Load predictions CSV
    df = pd.read_csv(csv_path)
    predictions = dict(zip(df['annotation_id'], df['concept_name']))
    print(f"Loaded {len(predictions)} predictions from {csv_path}")

    # Load dataset
    dataset = fo.load_dataset(dataset_name)
    print(f"Loaded dataset '{dataset_name}' with {len(dataset)} samples")

    # Import predictions
    matched = 0
    for sample in tqdm(dataset, desc="Importing predictions"):
        if not sample.ground_truth or not sample.ground_truth.detections:
            continue

        new_detections = []
        for det in sample.ground_truth.detections:
            ann_id = det.get("annotation_id")
            if ann_id in predictions:
                new_det = fo.Detection(
                    label=predictions[ann_id],
                    bounding_box=det.bounding_box,
                )
                new_det["annotation_id"] = ann_id
                new_detections.append(new_det)
                matched += 1

        if new_detections:
            sample[prediction_field] = fo.Detections(detections=new_detections)
            sample.save()

    print(f"Imported {matched} predictions to '{prediction_field}' field")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Path to predictions CSV")
    parser.add_argument("--dataset_name", default="fathomnet-2025")
    parser.add_argument("--field", default="model_predictions")
    parser.add_argument("--deployment", choices=["murilo", "prerna"], default="murilo")
    args = parser.parse_args()

    if args.deployment != "murilo":
        setup_fiftyone_credentials(args.deployment)

    import_predictions(args.csv_path, args.dataset_name, args.field)

if __name__ == "__main__":
    main()
```

---

## Phase 7: Verification & Model Evaluation

### 4.1 Verify import

```python
import fiftyone as fo

dataset = fo.load_dataset("fathomnet-2025")

# Check field exists
print(dataset.count_values("model_predictions.detections.label"))

# Visual inspection
session = fo.launch_app(dataset)
```

### 4.2 Run model evaluation

```python
# Compare predictions to ground truth
results = dataset.evaluate_detections(
    "model_predictions",
    gt_field="ground_truth",
    eval_key="model_eval",
)

# Print metrics
results.print_report()

# View confusion matrix in App
plot = results.plot_confusion_matrix()
plot.show()
```

---

## Summary

### Time Estimates (PACE Cluster)

| Phase | Action                              | Size/Count       | Time Estimate        |
| ----- | ----------------------------------- | ---------------- | -------------------- |
| 1     | Create directory structure          | -                | 1 min                |
| 2     | Download checkpoint from GDrive     | 16GB             | 30-60 min            |
| 3     | Download images from FathomNet URLs | 9,306 images     | 1-2 hours            |
| 4     | Clone repo + install deps           | -                | 10-15 min            |
| 5     | Run inference                       | -                | 2-4 hours (GPU)      |
| 6     | Import to FiftyOne                  | -                | 5-10 min             |
| 7     | Evaluation                          | -                | 10-15 min            |
| **TOTAL** | **Setup + Inference**           | **~37GB total**  | **4-8 hours**        |

### Key Bottlenecks

1. **Checkpoint download** (16GB from Google Drive) - 30-60 min
2. **Image download** (9,306 images from FathomNet) - 1-2 hours
3. **GPU inference** - 2-4 hours

## Key Files

| File                                          | Purpose                              |
| --------------------------------------------- | ------------------------------------ |
| `fathomnet_voxel51/05_download_images_local.py` | Downloads images from FathomNet URLs |
| Competition's `C1.TestModel.py`               | Runs inference, generates CSV        |
| `fathomnet_voxel51/04_import_predictions.py`  | Imports CSV to FiftyOne              |

## Requirements

- **Storage:** ~37GB total (21GB images + 16GB checkpoint)
- **Location:** PACE cluster shared storage (`~/ps-dsgt_clef2026-0/shared/`)
- **GPU:** 16GB+ VRAM (for DINOv2-large model)
- **Network:** Stable connection for downloading checkpoint and images
