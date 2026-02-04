"""
Delete a brain run from a FiftyOne dataset.

Brain runs store results from operations like compute_visualization, compute_similarity,
compute_uniqueness, etc. Use this script to remove brain runs that failed or are no longer needed.

PREREQUISITES:
    FiftyOne credentials configured in .env:
        MURILO_FIFTYONE_API_URI="https://murilo.dev.fiftyone.ai"
        MURILO_FIFTYONE_API_KEY="<api-key>"
        PRERNA_FIFTYONE_API_URI="https://prerna.dev.fiftyone.ai"
        PRERNA_FIFTYONE_API_KEY="<api-key>"

USAGE:
    # List available brain keys for a dataset:
    $ python -m fathomnet_voxel51.delete_brain_key --dataset_name fathomnet-test --list

    # Delete a specific brain key (Murilo deployment - default):
    $ python -m fathomnet_voxel51.delete_brain_key --dataset_name fathomnet-test --brain_key img_viz

    # Delete from Prerna deployment:
    $ python -m fathomnet_voxel51.delete_brain_key --dataset_name fathomnet-test --brain_key img_viz --deployment prerna

    # Delete all brain runs (use with caution):
    $ python -m fathomnet_voxel51.delete_brain_key --dataset_name fathomnet-test --all
"""

import argparse

from dotenv import load_dotenv

load_dotenv()

from fathomnet_voxel51.setup_fiftyone_credentials import (  # noqa: E402
    setup_fiftyone_credentials,
)

# Set default deployment to Murilo
setup_fiftyone_credentials("murilo")

import fiftyone as fo  # noqa: E402


def list_brain_runs(dataset_name: str):
    """List all brain runs for a dataset."""
    try:
        dataset = fo.load_dataset(dataset_name)
    except Exception as e:
        print(f"Error loading dataset '{dataset_name}': {e}")
        return

    brain_runs = dataset.list_brain_runs()

    if not brain_runs:
        print(f"No brain runs found for dataset '{dataset_name}'")
        return

    print(f"\nBrain runs for dataset '{dataset_name}':")
    print("=" * 60)
    for brain_key in brain_runs:
        info = dataset.get_brain_info(brain_key)
        print(f"\nKey: {brain_key}")
        print(f"  Type: {info.config.method}")
        if hasattr(info.config, "embeddings_field"):
            print(f"  Embeddings field: {info.config.embeddings_field}")
        if hasattr(info.config, "brain_key"):
            print(f"  Brain key: {info.config.brain_key}")
        print(f"  Version: {info.version}")
        print(f"  Timestamp: {info.timestamp}")


def delete_brain_run(dataset_name: str, brain_key: str):
    """Delete a specific brain run from a dataset."""
    try:
        dataset = fo.load_dataset(dataset_name)
    except Exception as e:
        print(f"Error loading dataset '{dataset_name}': {e}")
        return False

    # Check if brain key exists
    if brain_key not in dataset.list_brain_runs():
        print(f"Error: Brain key '{brain_key}' not found in dataset '{dataset_name}'")
        print("\nAvailable brain keys:")
        for key in dataset.list_brain_runs():
            print(f"  - {key}")
        return False

    # Delete the brain run
    try:
        dataset.delete_brain_run(brain_key)
        print(f"✓ Successfully deleted brain run '{brain_key}' from '{dataset_name}'")
        return True
    except Exception as e:
        print(f"Error deleting brain run '{brain_key}': {e}")
        return False


def delete_all_brain_runs(dataset_name: str):
    """Delete all brain runs from a dataset."""
    try:
        dataset = fo.load_dataset(dataset_name)
    except Exception as e:
        print(f"Error loading dataset '{dataset_name}': {e}")
        return

    brain_runs = dataset.list_brain_runs()

    if not brain_runs:
        print(f"No brain runs found for dataset '{dataset_name}'")
        return

    print(f"Deleting {len(brain_runs)} brain run(s) from '{dataset_name}'...")
    for brain_key in brain_runs:
        try:
            dataset.delete_brain_run(brain_key)
            print(f"  ✓ Deleted '{brain_key}'")
        except Exception as e:
            print(f"  ✗ Failed to delete '{brain_key}': {e}")

    print("\n✓ Completed deletion of brain runs")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--deployment",
        type=str,
        choices=["murilo", "prerna"],
        default="murilo",
        help="FiftyOne deployment to use (default: murilo)",
    )
    parser.add_argument(
        "--dataset_name",
        type=str,
        required=True,
        help="Name of the dataset",
    )
    parser.add_argument(
        "--brain_key",
        type=str,
        help="Brain key to delete",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all brain runs for the dataset",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Delete all brain runs (use with caution)",
    )

    args = parser.parse_args()

    # Override deployment if specified
    if args.deployment != "murilo":
        setup_fiftyone_credentials(args.deployment)

    # List mode
    if args.list:
        list_brain_runs(args.dataset_name)
        return

    # Delete all mode
    if args.all:
        confirm = input(
            f"Are you sure you want to delete ALL brain runs from '{args.dataset_name}'? (yes/no): "
        )
        if confirm.lower() == "yes":
            delete_all_brain_runs(args.dataset_name)
        else:
            print("Cancelled.")
        return

    # Delete specific brain key
    if not args.brain_key:
        print("Error: Must specify --brain_key, --list, or --all")
        parser.print_help()
        return

    delete_brain_run(args.dataset_name, args.brain_key)


if __name__ == "__main__":
    main()
