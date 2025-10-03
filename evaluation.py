import math
import numpy as np
from skimage.metrics import structural_similarity as ssim

# -----------------------------
# Evaluation
# -----------------------------

def calc_psnr(original: np.ndarray, stego: np.ndarray) -> float:
    mse = np.mean((original.astype(np.float64) - stego.astype(np.float64)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def calc_ssim(original: np.ndarray, stego: np.ndarray) -> float:
    # SSIM only calculate per channel. Then average them.
    ssim_vals = []
    if original.ndim == 3:  # RGB.
        for i in range(original.shape[2]):
            s = ssim(original[:, :, i], stego[:, :, i], data_range=255)
            ssim_vals.append(s)
        return sum(ssim_vals) / len(ssim_vals)
    else:  # Grayscale.
        return ssim(original, stego, data_range=255)

def calc_ber(original_bits: list, extracted_bits: list) -> float:
    errors = sum(o != e for o, e in zip(original_bits, extracted_bits))
    return errors / len(original_bits)

def calc_capacity(secret_bits: int, img_array: np.ndarray) -> float:
    h, w, c = img_array.shape if img_array.ndim == 3 else (*img_array.shape, 1)
    total_pixels = h * w * c
    return secret_bits / total_pixels  # Bits per pixel (bpp).

def evaluate_all(original: np.ndarray, stego: np.ndarray, original_bits: list, extracted_bits: list) -> None:
    psnr_val = calc_psnr(original, stego)
    ssim_val = calc_ssim(original, stego)

    ber_val = calc_ber(original_bits, extracted_bits)
    capacity_val = calc_capacity(len(original_bits), original)

    print("\n=== Evaluation Results ===")
    print(f"PSNR       : {psnr_val:.2f} dB")
    print(f"SSIM       : {ssim_val:.4f}")
    print(f"BER        : {ber_val:.4f}")
    print(f"Capacity   : {capacity_val:.6f} bpp")
