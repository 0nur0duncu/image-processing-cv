# RGB to Grayscale Conversion using OpenCV and NumPy

This code demonstrates how to convert an RGB image to grayscale using OpenCV and NumPy.

## Requirements

- Python 3.x
- OpenCV
- NumPy

```bash
pip install opencv-python numpy
```

## Code Explanation

```python
import cv2 as cv
import numpy as np

# Read the RGB image
BGR = cv.imread("./images/lenna256.jpg")

# Split the image into its B, G, R channels
B, G, R = cv.split(BGR)

# Calculate grayscale values using the formula: Y = 0.299*R + 0.587*G + 0.114*B
gray = np.uint8(0.299*R + 0.587*G + 0.114*B)

# Display the grayscale image
cv.imshow("RGB2GRAY", gray)
cv.waitKey(0)
cv.destroyAllWindows()
```

## Instructions

1. Make sure you have Python, OpenCV, and NumPy installed.
2. Save the RGB image you want to convert to grayscale in the specified path.
3. Replace the path in `cv.imread` with the path to your RGB image.
4. Run the script to see the RGB to Grayscale conversion.
