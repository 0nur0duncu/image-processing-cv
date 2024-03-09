# Image Resizing Example

This is a simple Python script using OpenCV and Matplotlib to demonstrate image resizing with different interpolation methods.

## Requirements

- Python 3.x
- OpenCV
- Matplotlib

## Installation

Install the required Python packages using the following command:

```bash
pip install opencv-python matplotlib
```

## Usage

1. Clone the repository:

```bash
git clone git@github.com:0nur0duncu/image-processing-cv.git
cd extras/IMGRESIZE
```

2. Run the script:

```bash
python img_resize.py
```

3. View the results:

The script will display a 2x2 grid of subplots, each showing a different image resizing technique:

- Subplot 1: Original image resized to 25x25 pixels.
- Subplot 2: Bilinear interpolation with a scaling factor of 1.5.
- Subplot 3: Nearest-neighbor interpolation with a scaling factor of 0.5.
- Subplot 4: Bicubic interpolation with a scaling factor of 0.5.
