#!/bin/bash
# Launcher script for FathomNet 2025 model inference job.
#
# Usage:
#   cd inference
#   bash sbatch/run.sh
#
#   # Dry run (preview command without submitting)
#   bash sbatch/run.sh --dry-run
#

set -eu

# ============================================================================
# Parse Arguments
# ============================================================================

DRY_RUN=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Submit FathomNet 2025 model inference job to PACE cluster."
            echo ""
            echo "Options:"
            echo "  --dry-run    Preview command without submitting job"
            echo "  -h, --help   Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# ============================================================================
# Determine paths
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFERENCE_DIR="$(dirname "$SCRIPT_DIR")"

# ============================================================================
# Setup
# ============================================================================

echo "=============================================="
echo "FathomNet 2025: Model Inference"
echo "=============================================="
echo "Inference dir: ${INFERENCE_DIR}"
echo ""

# Create log directory
LOG_DIR="${INFERENCE_DIR}/logs"
mkdir -p "${LOG_DIR}"

# Job script
JOB_SCRIPT="${SCRIPT_DIR}/_job.sh"

# ============================================================================
# Submit job
# ============================================================================

CMD="sbatch \
    --output=${LOG_DIR}/slurm_%j.log \
    ${JOB_SCRIPT}"

if [[ "${DRY_RUN}" == "true" ]]; then
    echo "[DRY-RUN] ${CMD}"
else
    echo "Submitting job..."
    ${CMD}
    echo ""
    echo "=============================================="
    echo "Job submitted!"
    echo "=============================================="
    echo ""
    echo "Monitor with: squeue -u \$USER"
    echo "View logs in: ${LOG_DIR}/"
fi
