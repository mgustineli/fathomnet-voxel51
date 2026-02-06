"""
Import model predictions from CSV into FiftyOne dataset.

This script reads a predictions CSV file (from the competition model) and
creates a new detections field in FiftyOne that matches predictions to
ground truth annotations by annotation_id.

CSV FORMAT:
    The CSV must have columns:
    - annotation_id: The COCO annotation ID (matches detection["annotation_id"] in FiftyOne)
    - concept_name: The predicted species label

USAGE:
    # Import predictions to default field "model_predictions":
    $ python -m fathomnet_voxel51.05_import_predictions predictions.csv

    # Import to a custom field name:
    $ python -m fathomnet_voxel51.05_import_predictions predictions.csv --field dinov2_predictions

    # Specify dataset and deployment:
    $ python -m fathomnet_voxel51.05_import_predictions predictions.csv --dataset fathomnet-2025 --deployment murilo
"""

import argparse
import csv
from collections import Counter

from dotenv import load_dotenv

load_dotenv()

from fathomnet_voxel51.setup_fiftyone_credentials import (  # noqa: E402
    setup_fiftyone_credentials,
)

# Set default deployment to Murilo
setup_fiftyone_credentials("murilo")

import fiftyone as fo  # noqa: E402
from tqdm import tqdm  # noqa: E402

# Default configuration
DEFAULT_DATASET_NAME = "fathomnet-2025"
DEFAULT_FIELD_NAME = "model_predictions"


def load_predictions_csv(csv_path: str) -> dict[int, str]:
    """
    Load predictions from CSV file.

    Args:
        csv_path: Path to the predictions CSV

    Returns:
        Dictionary mapping annotation_id (int) to predicted label (str)
    """
    predictions = {}

    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)

        # Validate columns
        if "annotation_id" not in reader.fieldnames:
            raise ValueError("CSV must have 'annotation_id' column")
        if "concept_name" not in reader.fieldnames:
            raise ValueError("CSV must have 'concept_name' column")

        for row in reader:
            ann_id = int(row["annotation_id"])
            label = row["concept_name"]
            predictions[ann_id] = label

    return predictions


def import_predictions(
    csv_path: str,
    dataset_name: str = DEFAULT_DATASET_NAME,
    field_name: str = DEFAULT_FIELD_NAME,
):
    """
    Import predictions from CSV into FiftyOne dataset.

    For each sample, this creates a new Detections field that mirrors the
    ground_truth detections but uses predicted labels instead.

    Args:
        csv_path: Path to the predictions CSV
        dataset_name: Name of the FiftyOne dataset
        field_name: Name of the field to store predictions
    """
    # Load dataset
    if not fo.dataset_exists(dataset_name):
        print(f"ERROR: Dataset '{dataset_name}' not found.")
        print(f"Available datasets: {fo.list_datasets()}")
        return

    dataset = fo.load_dataset(dataset_name)
    print(f"Loaded dataset '{dataset_name}' with {len(dataset)} samples")

    # Load predictions
    print(f"\nLoading predictions from {csv_path}...")
    predictions = load_predictions_csv(csv_path)
    print(f"Loaded {len(predictions)} predictions")

    # Filter to test split only (predictions are only for test images)
    test_view = dataset.match_tags("test")
    print(f"Filtered to {len(test_view)} test samples")

    # Track statistics
    matched_count = 0
    unmatched_count = 0
    samples_with_predictions = 0
    prediction_labels = Counter()

    print(f"\nImporting predictions to field '{field_name}'...")
    for sample in tqdm(test_view, desc="Processing samples"):
        if not sample.ground_truth or not sample.ground_truth.detections:
            continue

        pred_detections = []
        sample_had_match = False

        for gt_det in sample.ground_truth.detections:
            ann_id = gt_det.annotation_id
            if ann_id is None:
                continue

            if ann_id in predictions:
                # Create prediction detection with same bbox, different label
                pred_label = predictions[ann_id]
                pred_det = fo.Detection(
                    label=pred_label,
                    bounding_box=gt_det.bounding_box,
                )
                # Copy annotation_id for reference
                pred_det["annotation_id"] = ann_id
                pred_detections.append(pred_det)

                matched_count += 1
                sample_had_match = True
                prediction_labels[pred_label] += 1
            else:
                unmatched_count += 1

        if sample_had_match:
            samples_with_predictions += 1

        # Store predictions (even if empty list)
        sample[field_name] = fo.Detections(detections=pred_detections)
        sample.save()

    # Print summary
    print("\n" + "=" * 50)
    print("IMPORT SUMMARY")
    print("=" * 50)
    print(f"Predictions matched: {matched_count}")
    print(f"Ground truth annotations without prediction: {unmatched_count}")
    print(f"Samples with at least one prediction: {samples_with_predictions}")
    print(f"Unique predicted labels: {len(prediction_labels)}")

    # Print label distribution
    print("\n=== Prediction Label Distribution (Top 20) ===")
    for label, count in prediction_labels.most_common(20):
        print(f"  {label}: {count}")

    if len(prediction_labels) > 20:
        print(f"  ... and {len(prediction_labels) - 20} more labels")

    # Verification instructions
    print("\n=== Verification Steps ===")
    print(f"1. Open FiftyOne App and load dataset '{dataset_name}'")
    print(f"2. Check that '{field_name}' field appears in the schema")
    print(f"3. Compare ground_truth vs {field_name} visually")
    print("\n=== Model Evaluation ===")
    print("To evaluate predictions, run:")
    print(f"""
import fiftyone as fo
dataset = fo.load_dataset("{dataset_name}")
results = dataset.evaluate_detections(
    "{field_name}",
    gt_field="ground_truth",
    eval_key="{field_name.replace("_predictions", "_eval")}"
)
results.print_report()
""")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "csv_path",
        type=str,
        help="Path to the predictions CSV file",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default=DEFAULT_DATASET_NAME,
        dest="dataset_name",
        help=f"FiftyOne dataset name (default: {DEFAULT_DATASET_NAME})",
    )
    parser.add_argument(
        "--field",
        type=str,
        default=DEFAULT_FIELD_NAME,
        dest="field_name",
        help=f"Field name to store predictions (default: {DEFAULT_FIELD_NAME})",
    )
    parser.add_argument(
        "--deployment",
        type=str,
        choices=["murilo", "prerna"],
        default="murilo",
        help="FiftyOne deployment to use (default: murilo)",
    )
    args = parser.parse_args()

    # Override deployment if specified
    if args.deployment != "murilo":
        setup_fiftyone_credentials(args.deployment)

    import_predictions(
        csv_path=args.csv_path,
        dataset_name=args.dataset_name,
        field_name=args.field_name,
    )


if __name__ == "__main__":
    main()
