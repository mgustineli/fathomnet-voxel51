"""
Add a primary_label field for embeddings visualization.

This creates a flat string field at the sample level containing the most
common label from ground_truth detections. This field will appear in the
embeddings panel's "color by" dropdown.

USAGE:
    # Add to test dataset:
    $ python add_primary_label.py fathomnet-test

    # Add to full dataset:
    $ python add_primary_label.py fathomnet-2025
"""

import sys
from collections import Counter

import fiftyone as fo
from dotenv import load_dotenv
from tqdm import tqdm


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
    load_dotenv()

    if len(sys.argv) != 2:
        print(__doc__)
        print(f"\nAvailable datasets: {fo.list_datasets()}")
        sys.exit(1)

    dataset_name = sys.argv[1]
    add_primary_labels(dataset_name)


if __name__ == "__main__":
    main()
