#!/bin/bash
#SBATCH --job-name=fathomnet-inference
#SBATCH --account=paceship-dsgt_clef2026
#SBATCH --partition=gpu-rtx6000
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=4:00:00
#SBATCH -qinferno
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=mgustineli3@gatech.edu
#
# FathomNet 2025 Competition Model Inference
#
# Runs the winning model from dhlee-work/fathomnet-cvpr2025-ssl on the
# FathomNet 2025 test set. Predictions are saved as CSV for import into
# FiftyOne Enterprise via 04_import_predictions.py.
#
# Expected runtime: ~1.5-2 hours on RTX 6000 GPU
#
# Usage:
#   cd inference
#   bash sbatch/run.sh
#

set -eu

# ============================================================================
# Determine paths
# ============================================================================

# SLURM copies script to temp location, so use SLURM_SUBMIT_DIR if available
if [ -n "${SLURM_SUBMIT_DIR:-}" ]; then
    INFERENCE_DIR="$SLURM_SUBMIT_DIR"
else
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    INFERENCE_DIR="$(dirname "$SCRIPT_DIR")"
fi

REPO_DIR="$(dirname "$INFERENCE_DIR")"

# ============================================================================
# Configuration
# ============================================================================

# Shared PACE project storage
SHARED_DIR="$HOME/ps-dsgt_clef2026-0/shared/fathomnet-2025"

# Data paths
DATA_DIR="$SHARED_DIR"
ANNOTATIONS_DIR="$REPO_DIR/data"
CHECKPOINT="$SHARED_DIR/checkpoints/last-002.ckpt"
PREPROCESSING_DIR="$SHARED_DIR/preprocessing"

# Output (persisted back to the repo)
OUTPUT_DIR="$INFERENCE_DIR/results"

# Working directory in TMPDIR (fast local NVMe, cleaned up after job)
WORK_DIR="$TMPDIR/fathomnet-inference-${SLURM_JOB_ID:-local}"

# ============================================================================
# Print job info
# ============================================================================

echo "=============================================="
echo "Job: FathomNet 2025 Model Inference"
echo "=============================================="
echo "Job ID:          ${SLURM_JOB_ID:-local}"
echo "Node:            $(hostname)"
echo "Date:            $(date)"
echo "Repo:            ${REPO_DIR}"
echo "Inference dir:   ${INFERENCE_DIR}"
echo "Data dir:        ${DATA_DIR}"
echo "Annotations dir: ${ANNOTATIONS_DIR}"
echo "Checkpoint:      ${CHECKPOINT}"
echo "Preprocessing:   ${PREPROCESSING_DIR}"
echo "Work dir:        ${WORK_DIR}"
echo "Output dir:      ${OUTPUT_DIR}"
echo ""
nvidia-smi
echo ""

# ============================================================================
# Validate inputs
# ============================================================================

echo "Validating inputs..."

if [ ! -f "$CHECKPOINT" ]; then
    echo "ERROR: Checkpoint not found: $CHECKPOINT"
    echo "Download it with: gdown 1dr0BQJm2G9edhJNRu9vaUCdA4lMNeeRo -O $CHECKPOINT"
    exit 1
fi

if [ ! -d "$DATA_DIR/train_images" ] || [ ! -d "$DATA_DIR/test_images" ]; then
    echo "ERROR: Image directories not found in $DATA_DIR"
    echo "Run: python -m fathomnet_voxel51.05_download_images_local --output_dir $DATA_DIR"
    exit 1
fi

if [ ! -f "$ANNOTATIONS_DIR/dataset_test.json" ]; then
    echo "ERROR: Annotations not found: $ANNOTATIONS_DIR/dataset_test.json"
    exit 1
fi

# Check preprocessing artifacts
if [ ! -d "$PREPROCESSING_DIR" ]; then
    echo "WARNING: Preprocessing directory not found: $PREPROCESSING_DIR"
    echo "Creating it and copying artifacts from competition repo..."
    mkdir -p "$PREPROCESSING_DIR"
    COMP_RESULTS="$HOME/clef/fathomnet-cvpr2025-ssl/results"
    if [ -d "$COMP_RESULTS" ]; then
        cp -v "$COMP_RESULTS/dist_categories_debug.csv" "$PREPROCESSING_DIR/" 2>/dev/null || true
        cp -v "$COMP_RESULTS/dist_categories.csv" "$PREPROCESSING_DIR/" 2>/dev/null || true
        cp -v "$COMP_RESULTS/hierarchical_label.csv" "$PREPROCESSING_DIR/" 2>/dev/null || true
        cp -v "$COMP_RESULTS/hierachical_labelencoder.pkl" "$PREPROCESSING_DIR/" 2>/dev/null || true
    else
        echo "WARNING: Competition repo results not found at $COMP_RESULTS"
        echo "Preprocessing will run during inference (requires internet access)."
    fi
fi

echo "  All inputs validated."
echo ""

# ============================================================================
# Setup per-job virtual environment in TMPDIR (fast local NVMe)
# ============================================================================

echo "Setting up per-job virtual environment..."

JOB_VENV_DIR="$TMPDIR/fathomnet-venv-${SLURM_JOB_ID:-local}"
JOB_VENV="$JOB_VENV_DIR/.venv"

echo "  TMPDIR: $TMPDIR"
echo "  Venv:   $JOB_VENV"

mkdir -p "$JOB_VENV_DIR"
uv venv "$JOB_VENV" --python 3.11

# Activate the virtual environment
source "$JOB_VENV/bin/activate"

# Install inference dependencies from pyproject.toml
echo "  Installing dependencies from pyproject.toml..."
UV_LINK_MODE=copy uv pip install "$INFERENCE_DIR"

# Install PyTorch with CUDA support (overrides CPU-only wheel from above)
echo "  Installing PyTorch with CUDA..."
UV_LINK_MODE=copy uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

echo "  Virtual environment ready!"
echo ""

# Verify PyTorch CUDA
python -c "import torch; print(f'  PyTorch: {torch.__version__}, CUDA: {torch.cuda.is_available()}, Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
echo ""

# ============================================================================
# Create output directory
# ============================================================================

mkdir -p "$OUTPUT_DIR"

# ============================================================================
# Environment variables
# ============================================================================

# Performance tuning
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

# Disable wandb logging during inference
export WANDB_MODE=disabled

# ============================================================================
# Run inference
# ============================================================================

echo "Starting inference..."
echo ""

srun python "$INFERENCE_DIR/run_inference.py" \
    --data_dir "$DATA_DIR" \
    --annotations_dir "$ANNOTATIONS_DIR" \
    --checkpoint "$CHECKPOINT" \
    --preprocessing_dir "$PREPROCESSING_DIR" \
    --work_dir "$WORK_DIR" \
    --output_dir "$OUTPUT_DIR" \
    --batch_size 2 \
    --num_workers "$SLURM_CPUS_PER_TASK" \
    --device cuda

echo ""
echo "=============================================="
echo "End Time: $(date)"
echo "Inference complete!"
echo "Results saved to: $OUTPUT_DIR/"
echo "=============================================="
