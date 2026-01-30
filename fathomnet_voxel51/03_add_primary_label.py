"""
Add a primary_label field for embeddings visualization.

This creates a flat string field at the sample level containing the most
common label from ground_truth detections. This field will appear in the
embeddings panel's "color by" dropdown.

USAGE:
    # Add to test dataset (Murilo deployment by default):
    $ python -m fathomnet_voxel51.03_add_primary_label fathomnet-test

    # Use Prerna deployment:
    $ python -m fathomnet_voxel51.03_add_primary_label fathomnet-test --deployment prerna

    # Add to full dataset:
    $ python -m fathomnet_voxel51.03_add_primary_label fathomnet-2025
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
from tqdm import tqdm  # noqa: E402


def add_primary_labels(dataset_name: str):
    """Add primary_label field based on most frequent detection per image."""
    if not fo.dataset_exists(dataset_name):
        print(f"ERROR: Dataset '{dataset_name}' not found.")
        print(f"Available datasets: {fo.list_datasets()}")
        return

    dataset = fo.load_dataset(dataset_name)

    print(f"Adding primary_label field to '{dataset_name}' ({len(dataset)} samples)...")
    print("Using the most common label from ground_truth detections.\n")

    # Count statistics
    multi_label_count = 0
    no_label_count = 0

    for sample in tqdm(dataset, desc="Processing samples"):
        if sample.ground_truth.detections:
            # Get all labels from detections
            labels = [det.label for det in sample.ground_truth.detections]

            # Use most common label (or first if tie)
            label_counts = Counter(labels)
            primary_label = label_counts.most_common(1)[0][0]

            # Track multi-label images
            if len(set(labels)) > 1:
                multi_label_count += 1

            sample["primary_label"] = primary_label
        else:
            # No detections
            sample["primary_label"] = None
            no_label_count += 1

        sample.save()

    print("\n✅ Successfully added primary_label field!")
    print(f"   - Samples with labels: {len(dataset) - no_label_count}")
    print(f"   - Samples without labels: {no_label_count}")
    print(f"   - Samples with multiple different labels: {multi_label_count}")

    # Show label distribution
    print("\n=== Primary Label Distribution ===")
    label_counts = dataset.count_values("primary_label")
    print(f"Unique primary labels: {len(label_counts)}")
    if label_counts:
        print("\nTop 10 primary labels:")
        for label, count in sorted(
            label_counts.items(), key=lambda x: x[1], reverse=True
        )[:10]:
            print(f"  {label}: {count}")

    print("\n=== Next Steps ===")
    print("1. Refresh your FiftyOne Enterprise browser tab")
    print("2. Navigate to the Embeddings panel")
    print("3. In the 'Color by' dropdown, select 'primary_label'")
    print("4. Your embeddings will now be colored by species labels! 🎨")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dataset_name",
        type=str,
        help="Name of the FiftyOne dataset to add primary_label field to",
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

    add_primary_labels(args.dataset_name)


if __name__ == "__main__":
    main()
