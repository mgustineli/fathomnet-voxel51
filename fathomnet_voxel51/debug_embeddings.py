"""
Debug embeddings visualization mismatches.

This script helps diagnose why embeddings visualization shows mismatches
between the current view and the embeddings index.

USAGE:
    $ python -m fathomnet_voxel51.debug_embeddings --dataset_name fathomnet-2025 --brain_key dinov2_emb_patch
"""

import argparse

from dotenv import load_dotenv

load_dotenv()

from fathomnet_voxel51.setup_fiftyone_credentials import (  # noqa: E402
    setup_fiftyone_credentials,
)

setup_fiftyone_credentials("murilo")

import fiftyone as fo  # noqa: E402


def debug_embeddings(dataset_name: str, brain_key: str):
    """Debug embeddings mismatch."""
    dataset = fo.load_dataset(dataset_name)
    print(f"Dataset: {dataset_name}")
    print(f"Total samples: {len(dataset)}")

    # Get brain run info
    info = dataset.get_brain_info(brain_key)
    print(f"\nBrain run: {brain_key}")
    print(f"Method: {info.config.method}")

    # Check if it's a patch embeddings
    if hasattr(info.config, "patches_field"):
        patches_field = info.config.patches_field
        print(f"Patches field: {patches_field}")

        # Count current patches
        total_patches = sum(
            len(sample[patches_field].detections) if sample[patches_field] else 0
            for sample in dataset.select_fields([patches_field])
        )
        print(f"Total patches in dataset: {total_patches}")

        # Load the view that was used for embeddings
        try:
            brain_view = dataset.load_brain_view(brain_key)
            print(f"\nBrain view samples: {len(brain_view)}")

            brain_patches = sum(
                len(sample[patches_field].detections) if sample[patches_field] else 0
                for sample in brain_view.select_fields([patches_field])
            )
            print(f"Brain view patches: {brain_patches}")

            # Compare
            if len(brain_view) == len(dataset):
                print("\n✓ View matches: Same number of samples")
            else:
                print(
                    f"\n✗ View mismatch: Dataset has {len(dataset)} samples, "
                    f"brain view has {len(brain_view)}"
                )

            if brain_patches == total_patches:
                print("✓ Patches match: Same number of patches")
            else:
                print(
                    f"✗ Patches mismatch: Dataset has {total_patches} patches, "
                    f"brain view has {brain_patches}"
                )

                # Find differences
                dataset_ids = set(dataset.values("id"))
                brain_ids = set(brain_view.values("id"))

                only_in_dataset = dataset_ids - brain_ids
                only_in_brain = brain_ids - dataset_ids

                if only_in_dataset:
                    print(
                        f"\nSamples in dataset but not in brain view: {len(only_in_dataset)}"
                    )
                if only_in_brain:
                    print(
                        f"Samples in brain view but not in dataset: {len(only_in_brain)}"
                    )

        except Exception as e:
            print(f"\nError loading brain view: {e}")

    # Check embeddings field
    if hasattr(info.config, "embeddings_field"):
        embeddings_field = info.config.embeddings_field
        if embeddings_field:
            print(f"\nEmbeddings field: {embeddings_field}")

            # Check if field exists
            if embeddings_field in dataset.get_field_schema():
                # Count samples with embeddings
                with_embeddings = len(dataset.exists(embeddings_field))
                print(f"Samples with embeddings: {with_embeddings}/{len(dataset)}")
            else:
                print(f"⚠ Embeddings field '{embeddings_field}' not found in dataset")

    print("\n" + "=" * 60)
    print("SOLUTION:")
    print("=" * 60)
    print(
        """
The embeddings were computed on a specific view of the dataset.
To visualize them correctly, you need to:

1. In the FiftyOne App, load the brain view:
   - Press ` (backtick) to open operators
   - Search for "load_brain_view"
   - Select the brain key: """
        + brain_key
        + """
   - This will load the exact view used for embeddings

2. Then try visualizing the embeddings again

Alternatively, recompute embeddings on the full dataset without any filters.
"""
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset_name", required=True)
    parser.add_argument("--brain_key", required=True)
    parser.add_argument(
        "--deployment",
        choices=["murilo", "prerna"],
        default="murilo",
    )
    args = parser.parse_args()

    if args.deployment != "murilo":
        setup_fiftyone_credentials(args.deployment)

    debug_embeddings(args.dataset_name, args.brain_key)


if __name__ == "__main__":
    main()
