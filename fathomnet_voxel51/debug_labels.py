"""
Debug script to check ground_truth labels in FiftyOne dataset.

This script helps diagnose why the embeddings panel may not show
a color-by-label option.
"""

import fiftyone as fo
from dotenv import load_dotenv

DATASET_NAME = "fathomnet-2025"


def debug_dataset():
    """Check if ground_truth labels are properly configured."""
    if not fo.dataset_exists(DATASET_NAME):
        print(f"ERROR: Dataset '{DATASET_NAME}' not found.")
        return

    dataset = fo.load_dataset(DATASET_NAME)

    print(f"Dataset: {DATASET_NAME}")
    print(f"Total samples: {len(dataset)}")
    print()

    # Check schema
    print("=== Dataset Schema ===")
    print(dataset.schema)
    print()

    # Check if ground_truth field exists
    if "ground_truth" not in dataset.get_field_schema():
        print("ERROR: 'ground_truth' field not found in dataset!")
        return

    print("=== Ground Truth Field Info ===")
    print(f"Field type: {dataset.get_field('ground_truth')}")
    print()

    # Sample a few samples to inspect
    print("=== Sample Inspection (first 5 samples) ===")
    for i, sample in enumerate(dataset.limit(5)):
        print(f"\nSample {i + 1}: {sample.filepath}")
        print(f"  Split: {sample.split}")
        print(f"  Ground truth detections: {len(sample.ground_truth.detections)}")
        if sample.ground_truth.detections:
            labels = [det.label for det in sample.ground_truth.detections]
            print(f"  Labels: {labels[:5]}...")  # Show first 5 labels
        else:
            print("  WARNING: No detections found!")

    # Check label distribution
    print("\n=== Label Distribution ===")
    print("Counting unique labels across all detections...")

    # Count samples with/without detections
    samples_with_detections = sum(
        1 for s in dataset if len(s.ground_truth.detections) > 0
    )
    samples_without = len(dataset) - samples_with_detections

    print(f"Samples with detections: {samples_with_detections}")
    print(f"Samples without detections: {samples_without}")
    print()

    # Get label counts
    label_counts = dataset.count_values("ground_truth.detections.label")
    print(f"Unique labels found: {len(label_counts)}")
    if label_counts:
        print("\nTop 10 labels:")
        for label, count in sorted(
            label_counts.items(), key=lambda x: x[1], reverse=True
        )[:10]:
            print(f"  {label}: {count}")
    else:
        print("ERROR: No labels found in ground_truth.detections.label!")

    print("\n=== Recommendations ===")
    if samples_without > 0:
        print(
            f"⚠️  {samples_without} samples have no detections - this is normal for some datasets"
        )

    if not label_counts:
        print("❌ No labels found - the ground_truth field may be empty!")
        print("   → Check that ingest_dataset.py ran successfully")
        print("   → Verify COCO JSON files have annotations")
    else:
        print("✅ Labels found in ground_truth field")
        print("\nFor embeddings visualization:")
        print("   1. In FOE, ensure embeddings are computed on image samples")
        print("   2. Try coloring by: 'ground_truth.detections.label'")
        print(
            "   3. If that doesn't work, you may need to create a flattened label field"
        )
        print(
            "      (e.g., a Classification field with the most common label per image)"
        )


if __name__ == "__main__":
    load_dotenv()
    debug_dataset()
