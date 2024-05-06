import numpy as np
import matplotlib.pyplot as plt
import cv2

def gaussian_noise(image, snr):
    sigma = np.var(image)
    powerOfSignal = sigma / (10 ** (snr / 10.0))
    noise = np.random.normal(0,scale=np.sqrt(powerOfSignal), size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)
    return noisy_image


image = cv2.imread('./Ders7goruntuleri/LENNAorijinal.bmp',0)
filtered_image = gaussian_noise(image,0)



plt.figure(figsize=(5,5))
plt.subplot(221)
plt.imshow(image, cmap='gray')
plt.axis('off')

F = np.fft.fft2(image)
Fshift = np.fft.fftshift(F)
plt.subplot(222)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')

plt.subplot(223)
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')

F = np.fft.fft2(filtered_image)
Fshift = np.fft.fftshift(F)
plt.subplot(224)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()
