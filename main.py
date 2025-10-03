from PIL import Image
import numpy as np
import evaluation as eval

# -----------------------------
# Util: text <-> bits
# -----------------------------
def text_to_bits(text: str) -> list:
    return [int(b) for c in text.encode("utf-8") for b in f"{c:08b}"]

def bits_to_text(bits: list) -> str:
    chars = []
    for b in range(0, len(bits), 8):
        byte = bits[b:b+8]
        if len(byte) < 8:
            break
        chars.append(chr(int("".join(map(str, byte)), 2)))
    return "".join(chars)

# -----------------------------
# Parity Coding: Embed
# -----------------------------
def embed_parity(img_array: np.ndarray, secret_text: str, group_size: int=3):
    secret_bits = text_to_bits(secret_text)
    flat = img_array.flatten()
    idx = 0

    for bit in secret_bits:
        group = flat[idx:idx+group_size]
        lsb = group & 1
        parity = lsb.sum() % 2

        if parity != bit:
            # Flip one bit LSB (here we use the first one).
            group[0] ^= 1
            flat[idx:idx+group_size] = group

        idx += group_size

    return flat.reshape(img_array.shape), len(secret_bits)

# -----------------------------
# Parity Coding: Extract
# -----------------------------
def extract_parity(img_array: np.ndarray, bit_length: int, group_size: int=3):
    flat = img_array.flatten()
    bits = []
    idx = 0

    for _ in range(bit_length):
        group = flat[idx:idx+group_size]
        lsb = group & 1
        parity = lsb.sum() % 2
        bits.append(parity)
        idx += group_size

    return bits_to_text(bits)

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    # 1. Load image (RGB or L(grayscale) mode).
    img = Image.open("6.png").convert("RGB") # Change to your input image. Make sure to use png format.
    arr = np.array(img)

    # 2. Embed text.
    secret = input(str("Insert teks to image: "))
    stego_arr, bit_length = embed_parity(arr, secret, group_size=3)

    # 3. Save output image.
    stego_img = Image.fromarray(stego_arr)
    stego_img.save("stego.png")

    # 4. Load and extract text.
    arr2 = np.array(Image.open("stego.png"))
    extracted = extract_parity(arr2, bit_length, group_size=3)

    print("Original :", secret)
    print("Extracted:", extracted)
    
    # 5. Evaluation.
    # Get the real bits and extracted bits.
    original_bits = text_to_bits(secret)
    extracted_bits = text_to_bits(extracted)
    eval.evaluate_all(arr, stego_arr, original_bits, extracted_bits) # This will print the evaluation results.
