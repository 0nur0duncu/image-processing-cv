# Image Processing with Salt and Pepper Noise and MS2 Median Filter

This project demonstrates the addition of salt and pepper noise to an image and its subsequent filtering using the MS2 median filter.

## Libraries Used

- `cv2` (OpenCV): For reading and processing images.
- `numpy`: For mathematical operations and array manipulations.
- `skimage`: For adding random noise to images.
- `matplotlib`: For visualizing images.

## Functions

### `ms2_filter(img)`

This function applies the MS2 median filter to a given image.

- `img`: Input image (2D numpy array).

## Steps

1. The image `LENNAorijinal.bmp` is read and loaded in grayscale.
2. Salt and pepper noise is added to the image.
3. The noisy image is filtered using the MS2 median filter.
4. The original, noisy, and filtered images are visualized and saved.

## Results

After running the code, the following results are obtained:

1. **Original Image**: The original grayscale image.
2. **Noisy Image**: The image with added salt and pepper noise (amount = 0.05).
3. **Filtered Image**: The image filtered using the MS2 median filter.

The results are saved in the `./images/figure.jpg` file.

## Usage

To run this code:

1. Place the `LENNAorijinal.bmp` file in the `./images/` directory.
2. Install the necessary libraries by running:
   ```bash
   pip install numpy opencv-python scikit-image matplotlib
   ```
