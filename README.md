# Image Steganography - Parity Coding

This repository implements steganography using the **Parity Coding** method to hide text within images.

## Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/theprodigy18/PyEmbedText.git
   cd PyEmbedText
   ```

2. **Create and activate virtual environment** (optional)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare input image** in **lossless format** (PNG)
   - Edit line 63: replace `"6.png"` with your image filename
   
2. **Run the program**
   ```bash
   python main.py
   ```

3. **Enter the text** you want to hide when prompted

4. **Output**: File `stego.png` contains the image with hidden text

## Important Notes

⚠️ **Use lossless format (PNG)** - do not use JPEG/JPG as compression will corrupt the hidden data

## Requirements

```
Pillow>=10.0.0
numpy>=1.24.0
```