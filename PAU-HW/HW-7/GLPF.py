import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_noise(image, snr):
    
    sigma = np.var(image)
    powerOfSignal = sigma / (10 ** (snr / 10.0))
    noise = np.random.normal(0,scale=np.sqrt(powerOfSignal), size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)
    return noisy_image

def gaussian_low_pass_filter(f, sigma):
    global Fshift
    M,N = f.shape
    sigma *= 100
    H = np.zeros((M,N), dtype=np.float32)
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            H[u,v] = np.exp(-D**2/(2*sigma*sigma))
    Gshift = Fshift * H
    G = np.fft.ifftshift(Gshift)
    g = np.abs(np.fft.ifft2(G))
    return g

f = cv2.imread('./Ders7goruntuleri/LENNAorijinal.bmp',0)
gaussian_noise_image = gaussian_noise(f, 10)
F = np.fft.fft2(gaussian_noise_image)
Fshift = np.fft.fftshift(F)


plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(gaussian_noise_image,cmap='gray')
plt.title('Gauss gürültülü görüntü, SNR(dB) = 10')
plt.axis('off')

sigma = [0.1, 0.2, 0.3, 0.5, 1]

for index,item in enumerate(sigma):
  plt.subplot(2,3,index+2)
  plt.imshow(gaussian_low_pass_filter(gaussian_noise_image,item),cmap='gray')
  plt.title(f'sigma = {item}')
  plt.axis('off')

plt.tight_layout()
plt.show()