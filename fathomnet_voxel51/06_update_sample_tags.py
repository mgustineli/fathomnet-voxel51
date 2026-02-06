"""
Update sample tags to create train/val splits for YOLO training.

Splits the current "train" tagged samples into "train" and "val" using
stratified sampling on primary_label to ensure every class is represented
in both splits. Existing "test" tagged samples remain unchanged.

PREREQUISITES:
    1. Dataset must have samples tagged with "train" and optionally "test"
    2. Samples must have a "primary_label" field (run 03_add_primary_label.py first)

USAGE:
    # Default 80/20 split on fathomnet-2025:
    $ python -m fathomnet_voxel51.06_update_sample_tags --dataset fathomnet-2025

    # Custom split ratio (e.g., 90/10):
    $ python -m fathomnet_voxel51.06_update_sample_tags --dataset fathomnet-2025 --val_ratio 0.1

    # Run on test dataset:
    $ python -m fathomnet_voxel51.06_update_sample_tags --dataset fathomnet-test

    # Dry run (preview without modifying):
    $ python -m fathomnet_voxel51.06_update_sample_tags --dataset fathomnet-2025 --dry_run
"""

import argparse
from collections import Counter

from dotenv import load_dotenv

load_dotenv()

from fathomnet_voxel51.setup_fiftyone_credentials import (  # noqa: E402
    setup_fiftyone_credentials,
)

# Set default deployment to Murilo
setup_fiftyone_credentials("murilo")

import fiftyone as fo  # noqa: E402
from sklearn.model_selection import StratifiedShuffleSplit  # noqa: E402


def update_sample_tags(
    dataset_name: str,
    val_ratio: float = 0.2,
    seed: int = 42,
    dry_run: bool = False,
):
    """
    Split "train" tagged samples into "train" and "val" using stratified sampling.

    Args:
        dataset_name: Name of the FiftyOne dataset
        val_ratio: Fraction of train samples to use for validation (default: 0.2)
        seed: Random seed for reproducibility
        dry_run: If True, print plan without modifying the dataset
    """
    if not fo.dataset_exists(dataset_name):
        print(f"ERROR: Dataset '{dataset_name}' not found.")
        print(f"Available datasets: {fo.list_datasets()}")
        return

    dataset = fo.load_dataset(dataset_name)
    print(f"Loaded dataset '{dataset_name}' with {len(dataset)} samples")

    # Show current tag distribution
    tag_counts = dataset.count_values("tags")
    print(f"\nCurrent tag distribution: {dict(tag_counts)}")

    # Get train samples
    train_view = dataset.match_tags("train")
    num_train = len(train_view)
    if num_train == 0:
        print("ERROR: No samples with 'train' tag found.")
        return

    # Verify primary_label exists
    sample = train_view.first()
    if not hasattr(sample, "primary_label") or sample.primary_label is None:
        print("ERROR: Samples missing 'primary_label' field.")
        print("Run 03_add_primary_label.py first.")
        return

    # Collect sample IDs and labels for stratification
    sample_ids = []
    labels = []
    for s in train_view:
        sample_ids.append(s.id)
        labels.append(s.primary_label if s.primary_label else "unknown")

    # Show class distribution
    label_counts = Counter(labels)
    print(f"\nTrain samples: {num_train}")
    print(f"Unique classes: {len(label_counts)}")

    # Check for classes with too few samples for stratified split
    min_count = min(label_counts.values())
    if min_count < 2:
        rare_classes = [label for label, c in label_counts.items() if c < 2]
        print(f"\nWARNING: {len(rare_classes)} classes have only 1 sample.")
        print("These will be assigned to the train split.")

    # Compute split sizes
    num_val = int(num_train * val_ratio)
    num_new_train = num_train - num_val
    print(f"\nPlanned split (val_ratio={val_ratio}):")
    print(f"  train: {num_train} → {num_new_train} train + {num_val} val")

    test_view = dataset.match_tags("test")
    print(f"  test:  {len(test_view)} (unchanged)")

    if dry_run:
        print("\n[DRY RUN] No changes made.")
        return

    # Stratified split
    splitter = StratifiedShuffleSplit(
        n_splits=1, test_size=val_ratio, random_state=seed
    )
    train_idx, val_idx = next(splitter.split(sample_ids, labels))

    val_sample_ids = [sample_ids[i] for i in val_idx]

    # Update tags: remove "train" from val samples, add "val"
    print("\nUpdating tags...")
    val_samples = dataset.select(val_sample_ids)
    val_samples.untag_samples("train")
    val_samples.tag_samples("val")

    # Verify the split
    new_tag_counts = dataset.count_values("tags")
    print(f"\nUpdated tag distribution: {dict(new_tag_counts)}")

    # Verify class coverage
    new_train_view = dataset.match_tags("train")
    new_val_view = dataset.match_tags("val")

    train_classes = set(new_train_view.distinct("primary_label"))
    val_classes = set(new_val_view.distinct("primary_label"))

    train_only = train_classes - val_classes
    val_only = val_classes - train_classes

    print("\nClass coverage:")
    print(f"  Classes in train: {len(train_classes)}")
    print(f"  Classes in val:   {len(val_classes)}")
    if train_only:
        print(f"  Classes only in train: {train_only}")
    if val_only:
        print(f"  Classes only in val: {val_only}")
    if not train_only and not val_only:
        print("  All classes present in both splits!")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        dest="dataset_name",
        help="FiftyOne dataset name",
    )
    parser.add_argument(
        "--val_ratio",
        type=float,
        default=0.2,
        help="Fraction of train samples for validation (default: 0.2)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Preview split without modifying dataset",
    )
    parser.add_argument(
        "--deployment",
        type=str,
        choices=["murilo", "prerna"],
        default="murilo",
        help="FiftyOne deployment to use (default: murilo)",
    )
    args = parser.parse_args()

    if args.deployment != "murilo":
        setup_fiftyone_credentials(args.deployment)

    update_sample_tags(
        dataset_name=args.dataset_name,
        val_ratio=args.val_ratio,
        seed=args.seed,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
