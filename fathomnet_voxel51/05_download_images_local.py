"""
Download FathomNet images from URLs to local storage.

This script downloads images from their COCO URLs directly to local filesystem,
adapted for PACE cluster usage where gsutil is not available.

PREREQUISITES:
    1. Have the dataset JSON files in the data/ directory:
        - data/dataset_train.json
        - data/dataset_test.json

    2. Ensure output directory exists (will be created if not)

USAGE:
    # Download all images to shared project storage:
        $ python -m fathomnet_voxel51.05_download_images_local \
            --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025

    # Test with subset of 100 images:
        $ python -m fathomnet_voxel51.05_download_images_local \
            --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
            --limit 100

    # Download only train split:
        $ python -m fathomnet_voxel51.05_download_images_local \
            --output_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \
            --train_json data/dataset_train.json \
            --test_json ""

ARGUMENTS:
    --output_dir : Base directory for storing images (required)
    --train_json : Path to training dataset JSON (default: data/dataset_train.json)
    --test_json  : Path to test dataset JSON (default: data/dataset_test.json)
    --limit      : Number of images to process per split (default: None = all images)
    --concurrent : Number of concurrent downloads (default: 50)
"""

import json
import asyncio
import aiohttp
import aiofiles
import argparse
import os
from pathlib import Path
from tqdm.asyncio import tqdm_asyncio


async def download_image(session, url, output_path, semaphore):
    """Download a single image from URL to local filesystem."""
    async with semaphore:
        # Skip if already exists
        if output_path.exists():
            return "skipped"

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()

                    # Create parent directory if needed
                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    # Write to file asynchronously
                    async with aiofiles.open(output_path, "wb") as f:
                        await f.write(content)

                    return "downloaded"
                else:
                    return f"error_status_{response.status}"
        except Exception as e:
            return f"error_{str(e)}"


def check_existing_files(directory):
    """Check which files already exist in the directory."""
    if not directory.exists():
        return set()

    existing = {f.name for f in directory.iterdir() if f.is_file()}
    return existing


async def process_split(json_path, split_name, output_dir, limit=None, concurrent=50):
    """Process a dataset split: download images to local storage."""
    # Define output directory based on split
    output_subdir = Path(output_dir) / f"{split_name}_images"

    # 1. Check existing files
    print(f"Checking existing files in {output_subdir}...")
    existing_files = check_existing_files(output_subdir)
    print(f"Found {len(existing_files)} existing files.")

    # 2. Load JSON
    print(f"Loading {json_path} for split '{split_name}'...")
    with open(json_path, "r") as f:
        data = json.load(f)

    images = data["images"]
    if limit:
        images = images[:limit]
        print(f"Limiting to first {limit} images.")

    # 3. Filter out already downloaded images
    images_to_download = [
        img for img in images if img["file_name"] not in existing_files
    ]
    skipped_count = len(images) - len(images_to_download)
    if skipped_count > 0:
        print(f"Skipping {skipped_count} already downloaded images.")

    if not images_to_download:
        print(f"Split '{split_name}' complete: 0 downloaded, {skipped_count} skipped.")
        return

    # 4. Async download with progress bar
    semaphore = asyncio.Semaphore(concurrent)
    print(f"Downloading {len(images_to_download)} images to {output_subdir}...")

    async with aiohttp.ClientSession() as session:
        tasks = []
        for img in images_to_download:
            fname = img["file_name"]
            output_path = output_subdir / fname
            url = img["coco_url"]

            tasks.append(download_image(session, url, output_path, semaphore))

        results = await tqdm_asyncio.gather(*tasks)

    # 5. Report
    downloaded = results.count("downloaded")
    errors = len([r for r in results if r.startswith("error")])
    print(
        f"Split '{split_name}' complete: {downloaded} downloaded, {skipped_count} skipped, {errors} errors."
    )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Base directory for storing images (e.g., ~/ps-dsgt_clef2026-0/shared/fathomnet-2025)",
    )
    parser.add_argument("--train_json", type=str, default="data/dataset_train.json")
    parser.add_argument("--test_json", type=str, default="data/dataset_test.json")
    parser.add_argument(
        "--limit", type=int, default=None, help="Process N images per split for testing"
    )
    parser.add_argument(
        "--concurrent",
        type=int,
        default=50,
        help="Number of concurrent downloads (default: 50)",
    )
    args = parser.parse_args()

    # Expand user home directory
    output_dir = os.path.expanduser(args.output_dir)

    # Create base output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    print(f"Using output directory: {output_dir}")

    # Run for Train
    if args.train_json:
        asyncio.run(
            process_split(args.train_json, "train", output_dir, args.limit, args.concurrent)
        )

    # Run for Test
    if args.test_json:
        asyncio.run(
            process_split(args.test_json, "test", output_dir, args.limit, args.concurrent)
        )


if __name__ == "__main__":
    main()
