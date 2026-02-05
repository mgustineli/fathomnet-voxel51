# Plan: FathomNet Competition Model Predictions Integration

## Goal

Run inference using the FathomNet 2025 competition winner model externally, then import predictions into FiftyOne Enterprise for model evaluation.

## Approach

**External inference → CSV → FiftyOne import** (simplest path)

**Competition Repo:** https://github.com/dhlee-work/fathomnet-cvpr2025-ssl
**Checkpoint:** `~/Downloads/last-002.ckpt` (16GB)

---

## Phase 1: Set Up Competition Repo for Inference

### 1.1 Clone and configure the competition repo

```bash
cd ~/github
git clone https://github.com/dhlee-work/fathomnet-cvpr2025-ssl.git
cd fathomnet-cvpr2025-ssl
```

### 1.2 Install dependencies

```bash
pip install -r requirements.txt
# Key deps: pytorch-lightning, transformers, omegaconf
```

### 1.3 Set up data structure

The competition script expects:

```
fathomnet-cvpr2025-ssl/
├── dataset/fathomnet-2025/
│   ├── train_data/images/    # Download train images here
│   ├── test_data/images/     # Download test images here
│   └── dataset_test.json     # Symlink to our data/dataset_test.json
├── logs/{project_name}/Fold-0/last.ckpt  # Move checkpoint here
└── results/                  # Output directory (auto-created)
```

### 1.4 Download images from GCS

```bash
# Download from GCS to local (~24GB total)
mkdir -p dataset/fathomnet-2025/train_data/images
mkdir -p dataset/fathomnet-2025/test_data/images

gsutil -m cp -r gs://voxel51-test/fathomnet/train_images/* ./dataset/fathomnet-2025/train_data/images/
gsutil -m cp -r gs://voxel51-test/fathomnet/test_images/* ./dataset/fathomnet-2025/test_data/images/
```

### 1.5 Link annotation files

```bash
# Link our COCO JSON files
ln -s /Users/mgustineli/github/fathomnet-voxel51/data/dataset_train.json ./dataset/fathomnet-2025/dataset_train.json
ln -s /Users/mgustineli/github/fathomnet-voxel51/data/dataset_test.json ./dataset/fathomnet-2025/dataset_test.json
```

### 1.6 Move checkpoint to expected location

```bash
mkdir -p logs/experiment-final014/Fold-0/
cp ~/Downloads/last-002.ckpt logs/experiment-final014/Fold-0/last.ckpt
```

### 1.7 Run preprocessing (generates category mappings)

```bash
python A0.data_preprocess.py
# Creates: results/dist_categories_debug.csv, results/hierarchical_label.csv, etc.
```

---

## Phase 2: Run Inference

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

## Phase 3: Import Predictions into FiftyOne

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

## Phase 4: Verification & Model Evaluation

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

| Phase | Action                       | Time Estimate        |
| ----- | ---------------------------- | -------------------- |
| 1     | Setup repo + download images | 30-60 min (download) |
| 2     | Run inference                | 2-4 hours (GPU)      |
| 3     | Import to FiftyOne           | 5-10 min             |
| 4     | Evaluation                   | 10-15 min            |

## Key Files

| File                                         | Purpose                       |
| -------------------------------------------- | ----------------------------- |
| Competition's `C1.TestModel.py`              | Runs inference, generates CSV |
| `fathomnet_voxel51/04_import_predictions.py` | Imports CSV to FiftyOne       |

## Requirements

- ~24GB disk space for images
- GPU with 16GB+ VRAM (for DINOv2-large model)
- GCS access for image download
