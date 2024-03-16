# RGB to HSI Converter

This Python script converts an RGB image to the HSI (Hue, Saturation, Intensity) color space using the OpenCV library and NumPy.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:0nur0duncu/image-processing-cv.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Odev2_Python
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your RGB image in the `images` directory.

2. Update the file path in the script:

   ```python
   img = cv.imread("./images/your_image.png")
   ```

3. Run the script:

   ```bash
   python Odev2_Python.py
   ```

4. View the converted image in an OpenCV window.

## Algorithm Explanation

The script uses the following formula to convert RGB to HSI:

- H (Hue): atan2((R-G) + (R-B), sqrt((R-G)^2 + (R-B)(G-B))) \* (180/π)

- S (Saturation): 1 - (3 / (R + G + B) \* min(R, G, B))

- I (Intensity): (R + G + B) / 3

The resulting HSI image is displayed using OpenCV.

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests.
