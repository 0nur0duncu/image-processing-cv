# Image High-Pass Filtering

This project demonstrates the application of three types of high-pass filters (Ideal, Butterworth, and Gaussian) on an image. The filters are applied with varying parameters to show their effects.

## Libraries Used

- `cv2` (OpenCV): For reading and processing images.
- `numpy`: For mathematical operations and array manipulations.
- `matplotlib`: For visualizing images.

## Functions

### `ideal_high_pass_filter(f, D0)`

This function applies an ideal high-pass filter to a given image (f).

- `f`: Input image (2D numpy array).
- `D0`: Cutoff frequency.

### `butterwort_high_pass_filter(f, D0, n)`

This function applies a Butterworth high-pass filter to a given image (f).

- `f`: Input image (2D numpy array).
- `D0`: Cutoff frequency.
- `n`: Order of the filter.

### `gaussian_high_pass_filter(f, sigma)`

This function applies a Gaussian high-pass filter to a given image (f).

- `f`: Input image (2D numpy array).
- `sigma`: Standard deviation for the Gaussian filter.

## Steps

1. The image `cameraman.tif` is read and loaded in grayscale.
2. The image is transformed using the Fourier Transform and shifted to the center.
3. Each type of high-pass filter (Ideal, Butterworth, and Gaussian) is applied with different parameters.
4. The filtered images are visualized and saved.

## Results

After running the code, the following results are obtained:

1. **Ideal High-Pass Filter Results**:
   - Original image
   - Filtered images with different D0 values
2. **Butterworth High-Pass Filter Results**:
   - Original image
   - Filtered images with different D0 values and order n=1
3. **Gaussian High-Pass Filter Results**:
   - Original image
   - Filtered images with different sigma values

The results are saved in the `./images/` directory as:

- `ideal_high_pass_filter.png`
- `butterwort_high_pass_filter.png`
- `gaussian_high_pass_filter.png`

## Usage

To run this code:

1. Place the `cameraman.tif` file in the `./images/` directory.
2. Install the necessary libraries by running:
   ```bash
   pip install numpy opencv-python matplotlib
   ```
