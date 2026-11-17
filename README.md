# qdelta-shift

Reference implementation for **Quantile Drift Bounds for Streaming Classifiers**.

## Repository contents

- `src/` — streaming quantile estimators, drift detectors, and calibration utilities
- `experiments/` — experiment drivers for the synthetic and real-world score streams
- `configs/` — experiment configuration used for the SRLS 2025 submission
- `results/` — cached metrics behind the reported tables
- `cli_interface.json` — machine-readable interface of the monitoring CLI

## Quick start

```bash
pip install -r requirements.txt
python experiments/run_streaming.py --config configs/srls2025.yaml
```

## Citation

If you use this code, please cite:

> L. Okonkwo, A. Diaz. Quantile Drift Bounds for Streaming Classifiers. Under review at SRLS 2025.
