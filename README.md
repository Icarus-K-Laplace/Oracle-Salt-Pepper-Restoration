# Oracle-Salt-Pepper-Restoration
Oracle-Salt-Pepper-Restoration: An engineering upper-bound baseline for impulse noise removal. By assuming perfect noise detection (oracle), this project implements a two-stage sparse inpainting strategy to establish the theoretical performance limit for blind restoration algorithms.
# Oracle-Salt-Pepper-Restoration 🎯

### An Engineering Upper-Bound Baseline for Impulse Noise Removal

> **Developed independently by an undergraduate student.**
> This project explores the theoretical limits of salt-and-pepper noise removal under the assumption of perfect detection. It serves as a rigorous engineering benchmark for evaluating more complex, blind restoration algorithms.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 💡 The "Why" Behind This Project

In academic research, we often develop complex algorithms (like CNNs or variational methods) to solve inverse problems. However, a fundamental question is often overlooked:

> **"What is the best possible performance we could achieve if we knew exactly where the noise is?"**

**My Hypothesis:**
If we assume an **Oracle** (perfect knowledge of noise locations), the restoration problem simplifies to a sparse inpainting task. By implementing this ideal scenario with high engineering precision, we establish a **performance upper bound**.

This repository is not about proposing a "new generalized method", but about **engineering the optimal solution for a specific, well-defined problem**.

---

## 🛠️ Methodology: Two-Stage Oracle Restoration

### Stage 1: Oracle Detection & Fast Repair
- **Assumption**: Salt-and-pepper noise manifests as extreme values (0 or 255) in 8-bit images.
- **Logic**: Instead of statistical guessing, we use threshold-based oracle detection to identify outliers with near-100% precision.
- **Action**: Apply sparse median filtering only to detected pixels.

### Stage 2: Residual Refinement
- **Observation**: Single-pass filtering may leave residual artifacts or miss non-extreme outliers.
- **Logic**: A second pass scans for geometric inconsistencies in the restored image.
- **Action**: Apply multi-scale adaptive filtering (window sizes 3→5→7) to refine complex regions.

---

## 📊 Performance (The "Upper Bound")

Tested on `scene1.png` (Infrared):

| Metric | Standard Median | **Oracle-Guided (Ours)** | Improvement |
|:---:|:---:|:---:|:---:|
| **PSNR (dB)** | 28.5 | **39.8+** | **+11.3 dB** |
| **SSIM** | 0.85 | **0.99** | **+0.14** |
| **Visuals** | Blurry edges | **Near-perfect reconstruction** | - |

*> Note: This performance serves as a target for blind restoration algorithms (like my MAPD framework).*

---

## 🚀 Usage

### 1. Installation
Pure Python, minimal dependencies.
```bash
pip install numpy opencv-python
