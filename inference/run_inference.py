#!/usr/bin/env python
"""FathomNet 2025 Competition Model Inference Runner.

This script runs inference using the winning model from the FathomNet 2025
Fine-Grained Visual Categorization (FGVC) competition at CVPR 2025.

Original competition repository:
    https://github.com/dhlee-work/fathomnet-cvpr2025-ssl
    Author: Donghyeon Lee (dhlee-work)
    License: See original repository for license terms

The original model uses a DINOv2-Large Vision Transformer with:
    - Multi-scale environmental context encoding (crop scales: 3, 5, full)
    - Intra-environment attention between object and context features
    - Hierarchical classification loss (taxonomic hierarchy)
    - 79 marine species categories from the FathomNet dataset

This wrapper script adapts the competition code for deployment on the
Georgia Tech PACE cluster, handling:
    1. Cloning and patching the competition repository
    2. Setting up data directory structure (symlinks to shared storage)
    3. Copying preprocessing artifacts (taxonomy/category mappings)
    4. Executing model inference on the test set
    5. Saving predictions to CSV for import into FiftyOne Enterprise

Usage:
    python run_inference.py \\
        --data_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \\
        --annotations_dir ~/clef/fathomnet-voxel51/data \\
        --checkpoint ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt \\
        --preprocessing_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/preprocessing \\
        --output_dir ./results

Environment:
    - PACE cluster GPU node (RTX 6000 or similar, 16GB+ VRAM)
    - Python 3.11+ with PyTorch CUDA support
    - Virtual environment created per-job in $TMPDIR
"""

import argparse
import json
import os
import random
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import tqdm as tqdm_module
from omegaconf import OmegaConf
from torch.utils.data import DataLoader

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COMPETITION_REPO_URL = "https://github.com/dhlee-work/fathomnet-cvpr2025-ssl.git"
CONFIG_NAME = "experiment-final14.yaml"
PROJECT_NAME = "experiment-final014"
SEED = 1234

PREPROCESSING_ARTIFACTS = [
    "dist_categories_debug.csv",
    "hierarchical_label.csv",
    "hierachical_labelencoder.pkl",
]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args():
    parser = argparse.ArgumentParser(
        description="FathomNet 2025 Competition Model Inference",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full run on PACE cluster (called from _job.sh)
  python run_inference.py \\
      --data_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025 \\
      --annotations_dir ~/clef/fathomnet-voxel51/data \\
      --checkpoint ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/checkpoints/last-002.ckpt \\
      --preprocessing_dir ~/ps-dsgt_clef2026-0/shared/fathomnet-2025/preprocessing \\
      --output_dir ./results

  # Resume from existing work directory (skip re-cloning)
  python run_inference.py \\
      --data_dir ... --annotations_dir ... --checkpoint ... \\
      --work_dir /tmp/fathomnet-inference --skip_clone
""",
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        required=True,
        help="Directory containing train_images/ and test_images/",
    )
    parser.add_argument(
        "--annotations_dir",
        type=str,
        required=True,
        help="Directory containing dataset_train.json and dataset_test.json",
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        required=True,
        help="Path to model checkpoint (.ckpt file)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./results",
        help="Directory to save prediction CSV (default: ./results)",
    )
    parser.add_argument(
        "--work_dir",
        type=str,
        default=None,
        help="Working directory for repo clone (default: $TMPDIR/fathomnet-inference)",
    )
    parser.add_argument(
        "--preprocessing_dir",
        type=str,
        default=None,
        help="Directory with existing preprocessing artifacts to copy",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=2,
        help="Inference batch size (default: 2)",
    )
    parser.add_argument(
        "--num_workers",
        type=int,
        default=6,
        help="DataLoader num workers (default: 6)",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        choices=["cuda", "cpu"],
        help="Device for inference (default: cuda)",
    )
    parser.add_argument(
        "--skip_clone",
        action="store_true",
        help="Skip cloning repo if work_dir already has the code",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def init_random_seed(seed):
    """Set random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------


def setup_work_dir(args):
    """Clone competition repo and set up directory structure with symlinks."""
    work_dir = Path(args.work_dir)
    data_dir = Path(args.data_dir).resolve()
    annotations_dir = Path(args.annotations_dir).resolve()
    checkpoint = Path(args.checkpoint).resolve()

    # Clone competition repo
    if not args.skip_clone:
        if work_dir.exists():
            print(f"  Removing existing work directory: {work_dir}")
            shutil.rmtree(str(work_dir))
        print(f"  Cloning {COMPETITION_REPO_URL}")
        print(f"  -> {work_dir}")
        subprocess.run(
            ["git", "clone", "--depth", "1", COMPETITION_REPO_URL, str(work_dir)],
            check=True,
        )
    else:
        print(f"  Using existing work directory: {work_dir}")

    # Create dataset directory structure with symlinks
    dataset_dir = work_dir / "dataset" / "fathomnet-2025"
    for subdir in ["train_data", "test_data"]:
        (dataset_dir / subdir).mkdir(parents=True, exist_ok=True)

    symlinks = {
        dataset_dir / "train_data" / "images": data_dir / "train_images",
        dataset_dir / "test_data" / "images": data_dir / "test_images",
        dataset_dir / "dataset_train.json": annotations_dir / "dataset_train.json",
        dataset_dir / "dataset_test.json": annotations_dir / "dataset_test.json",
    }
    for link_path, target in symlinks.items():
        if not link_path.exists():
            link_path.symlink_to(target)
            print(f"  Linked: {link_path.name} -> {target}")

    # Set up checkpoint
    ckpt_dir = work_dir / "logs" / PROJECT_NAME / "Fold-0"
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    ckpt_link = ckpt_dir / "last.ckpt"
    if not ckpt_link.exists():
        ckpt_link.symlink_to(checkpoint)
        print(f"  Linked: checkpoint -> {checkpoint}")

    # Create results directory
    (work_dir / "results").mkdir(exist_ok=True)

    # Apply source code patches to fix hardcoded paths
    apply_patches(work_dir)

    # Copy preprocessing artifacts if provided
    if args.preprocessing_dir:
        copy_preprocessing_artifacts(work_dir, Path(args.preprocessing_dir))

    return work_dir


def apply_patches(repo_dir):
    """Patch competition source code to fix hardcoded image paths.

    The original datautils.py constructs image paths using numeric image IDs
    (e.g., '1.png'), but the FathomNet dataset uses UUID filenames
    (e.g., '000b8e39-7240-49fd-9f50-713edcb28544.png'). This patch adds
    support for an image_id->filename mapping passed through the config.
    """
    datautils_path = repo_dir / "src" / "datautils.py"
    content = datautils_path.read_text()

    # Only patch if the original code is present (idempotent)
    original_fragment = "image_path = os.path.join('./dataset/fathomnet-2025/train_data/images',str(img_id)+'.png')"
    if original_fragment not in content:
        print("  Patch: datautils.py already patched or source changed, skipping.")
        return

    old_block = (
        "        if self.phase == 'train' or self.phase == 'valid':\n"
        "            image_path = os.path.join('./dataset/fathomnet-2025/train_data/images',str(img_id)+'.png')\n"
        "        else:\n"
        "            image_path = os.path.join('./dataset/fathomnet-2025/test_data/images',str(img_id)+'.png')"
    )

    new_block = (
        "        # Patched: use image_id_to_filename mapping for UUID filenames\n"
        "        if hasattr(self.args, 'image_id_to_filename') and img_id in self.args.image_id_to_filename:\n"
        "            filename = self.args.image_id_to_filename[img_id]\n"
        "        else:\n"
        "            filename = str(img_id) + '.png'\n"
        "\n"
        "        if self.phase == 'train' or self.phase == 'valid':\n"
        "            image_path = os.path.join('./dataset/fathomnet-2025/train_data/images', filename)\n"
        "        else:\n"
        "            image_path = os.path.join('./dataset/fathomnet-2025/test_data/images', filename)"
    )

    content = content.replace(old_block, new_block)
    datautils_path.write_text(content)
    print("  Patch: Applied image filename mapping fix to datautils.py")


def copy_preprocessing_artifacts(repo_dir, preprocessing_dir):
    """Copy preprocessing artifacts (taxonomy mappings) to repo results dir."""
    preprocessing_dir = Path(preprocessing_dir).resolve()
    results_dir = repo_dir / "results"
    copied = 0

    for artifact in PREPROCESSING_ARTIFACTS:
        src = preprocessing_dir / artifact
        dst = results_dir / artifact
        if src.exists() and not dst.exists():
            shutil.copy2(str(src), str(dst))
            copied += 1
        elif not src.exists():
            print(f"  Warning: preprocessing artifact not found: {src}")

    # Also copy dist_categories.csv if it exists (used by some configs)
    dist_csv = preprocessing_dir / "dist_categories.csv"
    if dist_csv.exists() and not (results_dir / "dist_categories.csv").exists():
        shutil.copy2(str(dist_csv), str(results_dir / "dist_categories.csv"))

    print(f"  Copied {copied} preprocessing artifacts from {preprocessing_dir}")


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------


def run_inference(repo_dir, args):
    """Run model inference using the competition code.

    Loads the model checkpoint, processes all test annotations through the
    DINOv2-based multi-scale encoder, and produces per-annotation predictions.
    """
    import pytorch_lightning as pl

    # Add competition repo to Python path so we can import src modules
    sys.path.insert(0, str(repo_dir))
    original_cwd = os.getcwd()
    os.chdir(repo_dir)

    try:
        from src.datautils import Fathomnet_Dataset
        from src.model import FathomnetModel

        # Load config from competition repo
        config_path = repo_dir / "config" / CONFIG_NAME
        config = OmegaConf.load(str(config_path))

        # Override config for inference
        pl.seed_everything(SEED)
        init_random_seed(SEED)
        config.kfold = False
        config.transform = False
        config.imgxaug = False
        config.kfold_nsplits = 1
        config.num_workers = args.num_workers

        device = args.device
        batch_size = args.batch_size

        # Load test annotations
        test_anno_path = repo_dir / "dataset" / "fathomnet-2025" / "dataset_test.json"
        with open(test_anno_path, "r", encoding="utf-8") as f:
            dataset = json.load(f)

        anno_data = dataset["annotations"]

        # Build category ID <-> name mappings (0-indexed)
        cate_name2id = {}
        cate_id2name = {}
        for cat in dataset["categories"]:
            cate_id = cat["id"] - 1
            cat["id"] = cate_id
            cate_name = cat["name"]
            cate_name2id[cate_name] = cate_id
            cate_id2name[cate_id] = cate_name
        config.category_name2id = cate_name2id
        config.category_id2name = cate_id2name

        # Build image_id -> filename mapping (fixes UUID filename issue)
        image_id_to_filename = {
            img["id"]: img["file_name"] for img in dataset["images"]
        }
        config.image_id_to_filename = image_id_to_filename

        # Prepare fold indices (single fold for inference)
        data_len = len(anno_data)
        sampled_val = np.random.choice(list(range(data_len)), 100).tolist()
        fold_indices = [{"train": list(range(data_len)), "val": sampled_val}]

        print(f"  Device:           {device}")
        print(f"  Batch size:       {batch_size}")
        print(f"  Num workers:      {args.num_workers}")
        print(f"  Test annotations: {len(anno_data)}")
        print(f"  Test images:      {len(dataset['images'])}")
        print(f"  Categories:       {len(cate_name2id)}")

        # Run inference across folds
        results = []
        n_fold = config.kfold_nsplits

        for current_fold in range(n_fold):
            model_path = str(
                repo_dir / "logs" / PROJECT_NAME / f"Fold-{current_fold}" / "last.ckpt"
            )
            print(f"\n  Loading model from: {model_path}")

            model = FathomnetModel.load_from_checkpoint(
                model_path, map_location=torch.device(device)
            ).to(device)
            model.eval()

            config.current_fold = current_fold
            train_anno_ids = fold_indices[0]["train"]
            train_anno = [anno_data[i] for i in train_anno_ids]

            test_dataset = Fathomnet_Dataset(
                train_anno[:], phase="test", args=config
            )
            test_dataloader = DataLoader(
                test_dataset,
                batch_size=batch_size,
                num_workers=args.num_workers,
                shuffle=False,
                drop_last=False,
                pin_memory=True,
            )

            with torch.no_grad():
                for batch in tqdm_module.tqdm(
                    test_dataloader, desc=f"  Fold {current_fold}"
                ):
                    obj_processed_imgs = batch["obj_processed_img"].to(device)
                    obj_anno = batch["obj_anno"]

                    # Multi-scale environmental context encoding
                    global_processed_imgs = {}
                    for scales in model.hparams.img_encoder_size:
                        for crop_scale in model.hparams.env_img_crop_scale_list:
                            _name = str(scales[0]) + "_" + str(crop_scale)
                            global_processed_imgs[_name] = batch[
                                f"global_processed_img{_name}"
                            ].to(device)

                    # Object ViT encoding
                    n_samples = obj_processed_imgs.shape[0]
                    obj_vit_enc_out = model.obj_vit_region_encoder(obj_processed_imgs)
                    obj_vit_embeddings = obj_vit_enc_out.last_hidden_state[:, :1, :]

                    # Multi-scale image ViT encoding
                    img_vit_p_embeddings = {}
                    for scales in model.hparams.img_encoder_size:
                        for crop_scale in model.hparams.env_img_crop_scale_list:
                            _name = str(scales[0]) + "_" + str(crop_scale)
                            img_vit_enc_out = model.img_vit_region_encoders[_name](
                                global_processed_imgs[_name]
                            )
                            img_vit_p_embeddings[_name] = (
                                img_vit_enc_out.last_hidden_state[:, 1:, :]
                            )

                    # Concatenate embeddings
                    concat_embs = obj_vit_embeddings.view(
                        obj_vit_embeddings.shape[0], -1
                    )

                    # Intra-environment attention
                    if model.hparams.intra_env_attn:
                        intra_env_embs_dict = {}
                        for scales in model.hparams.img_encoder_size:
                            for crop_scale in model.hparams.env_img_crop_scale_list:
                                _name = str(scales[0]) + "_" + str(crop_scale)
                                intra_env_embs_dict[_name] = (
                                    model.intra_env_attn_module[_name](
                                        obj_vit_embeddings,
                                        img_vit_p_embeddings[_name],
                                    ).view(n_samples, -1)
                                )
                        intra_env_embs = torch.concat(
                            list(intra_env_embs_dict.values()), 1
                        )
                        concat_embs = torch.concat(
                            (concat_embs, intra_env_embs), dim=-1
                        )

                    # Classification
                    embs = model.concat_proj(concat_embs)
                    logits = model.classifier(embs).squeeze()
                    preds = torch.argmax(logits, dim=1).cpu().numpy().astype(float)
                    preds_class = [
                        model.hparams.category_id2name[preds[i]]
                        for i in range(len(preds))
                    ]
                    obj_annos = obj_anno["id"].cpu().numpy()
                    for i in range(len(obj_annos)):
                        results.append(
                            [current_fold, obj_annos[i], preds_class[i]]
                        )

        # Aggregate predictions via majority voting across folds
        submission = pd.DataFrame(
            results, columns=["fold", "annotation_id", "concept_name"]
        )
        submission = submission[["annotation_id", "concept_name"]]
        voted_submission = (
            submission.groupby(["annotation_id"])["concept_name"]
            .agg(lambda x: x.mode().iloc[0])
            .reset_index()
        )

        # Save results
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"submission_{PROJECT_NAME}.csv"
        voted_submission.to_csv(str(output_path), index=False)

        print(f"\n  Predictions saved to: {output_path}")
        print(f"  Total predictions:    {len(voted_submission)}")

        return output_path

    finally:
        os.chdir(original_cwd)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    args = parse_args()

    # Default work_dir: use TMPDIR if available (fast local NVMe on PACE)
    if args.work_dir is None:
        tmpdir = os.environ.get("TMPDIR", "/tmp")
        args.work_dir = os.path.join(tmpdir, "fathomnet-inference")

    print("=" * 60)
    print("FathomNet 2025 Competition Model Inference")
    print("=" * 60)
    print(f"  Data dir:          {args.data_dir}")
    print(f"  Annotations dir:   {args.annotations_dir}")
    print(f"  Checkpoint:        {args.checkpoint}")
    print(f"  Preprocessing dir: {args.preprocessing_dir}")
    print(f"  Work dir:          {args.work_dir}")
    print(f"  Output dir:        {args.output_dir}")
    print(f"  Device:            {args.device}")
    print(f"  Batch size:        {args.batch_size}")
    print(f"  Num workers:       {args.num_workers}")
    print()

    # Step 1: Setup working directory
    print("Step 1: Setting up working directory...")
    work_dir = setup_work_dir(args)
    print()

    # Step 2: Verify preprocessing artifacts
    print("Step 2: Checking preprocessing artifacts...")
    results_dir = work_dir / "results"
    missing = [f for f in PREPROCESSING_ARTIFACTS if not (results_dir / f).exists()]
    if missing:
        print(f"  Missing artifacts: {missing}")
        print("  Running preprocessing (requires internet for FathomNet API)...")
        subprocess.run(
            [
                sys.executable,
                "A0.data_preprocess.py",
                "--data_path",
                str(work_dir / "dataset" / "fathomnet-2025" / "dataset_train.json"),
            ],
            cwd=str(work_dir),
            check=True,
        )
        print("  Preprocessing complete.")
    else:
        print("  All preprocessing artifacts found.")
    print()

    # Step 3: Run inference
    print("Step 3: Running model inference...")
    output_path = run_inference(work_dir, args)

    print()
    print("=" * 60)
    print("Inference complete!")
    print(f"  Results: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
