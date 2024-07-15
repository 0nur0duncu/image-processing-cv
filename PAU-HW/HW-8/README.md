# Image Processing and Noise Reduction

This project demonstrates noise reduction on an image using Gaussian low-pass filter and Wiener filter. It also adds Gaussian white noise to the image and compares the filtering results.

## Libraries Used

- `cv2` (OpenCV): For reading and processing images.
- `numpy`: For mathematical operations and array manipulations.
- `matplotlib`: For visualizing images.

## Functions

### `gaussian_low_pass_filter(f, sigma)`

This function applies a Gaussian low-pass filter to a given image (f).

- `f`: Input image (2D numpy array).
- `sigma`: Standard deviation for the Gaussian filter.

### `gaussian_noise(image, snr)`

This function adds Gaussian white noise to a given image.

- `image`: Input image (2D numpy array).
- `snr`: Signal-to-noise ratio (dB).

## Steps

1. The image `lenna.bmp` is read and loaded in grayscale.
2. The image is converted to `float64` type.
3. Gaussian white noise is added to the image.
4. Noise reduction is performed using the Wiener filter.
5. Noisy and filtered images are calculated.
6. Gaussian low-pass filter is applied, and the results are visualized.
7. The original, noisy, and filtered images are displayed along with the calculated SNR and NMSE values.

## Results

After running the code, the following results are obtained:

- Original image
- Noisy image (SNR(dB) = 7)
- Wiener filtered image
- Gaussian low-pass filtered image (sigma = 0.3)

## Usage

To run this code:

1. Place the `lenna.bmp` file in the `./images/` directory.
2. Install the necessary libraries by running:
   ```bash
   pip install numpy opencv-python matplotlib
   ```
