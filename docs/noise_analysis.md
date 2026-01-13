# Analysis of Impulse Noise Characteristics

## The Uniqueness of Salt-and-Pepper Noise
Unlike Gaussian noise, which affects every pixel with a small perturbation, Salt-and-Pepper (S&P) noise is:
1.  **Sparse**: Only a subset of pixels are affected.
2.  **Extreme**: The noise values are typically saturated (0 or 255).
3.  **Independent**: The noise value is independent of the underlying signal.

## Why Oracle Detection Matters
Because of property #2 (Extreme), S&P noise is theoretically detectable with near-100% accuracy using simple thresholding, *provided* the original image signal does not contain those extreme values.

This repository exploits this property to establish an **engineering upper bound**. By assuming we can detect the noise perfectly (Oracle), we can focus solely on the **inpainting problem** (how to fill the holes).

## Comparison with Real-World Scenarios
In real scenarios (e.g., thermal sensors):
*   Noise is not always 0/255 (dead pixels might be gray).
*   The signal might contain 0/255 (hot targets).

Therefore, while this Oracle Restorer achieves perfect results on synthetic data, real-world algorithms (like my MAPD framework) must deal with the uncertainty of detection. This codebase serves as the **idealized reference** for those complex methods.
