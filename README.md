# Image Watermarking - Parity Coding

This repository implements watermarking using the **Parity Coding** method to hide text within images.

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
imageio==2.37.0
lazy_loader==0.4
networkx==3.5
numpy==2.3.3
packaging==25.0imageio==2.37.0
lazy_loader==0.4
networkx==3.5
numpy==2.3.3
packaging==25.0
pillow==11.3.0
scikit-image==0.25.2
scipy==1.16.2
tifffile==2025.9.30
pillow==11.3.0
scikit-image==0.25.2
scipy==1.16.2
tifffile==2025.9.30
```