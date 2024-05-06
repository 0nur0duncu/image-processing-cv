import cv2
import numpy as np
import matplotlib.pyplot as plt

def ideal_low_pass_filter(f,D0):
  D0 *= 100
  M,N = f.shape
  H = np.zeros((M,N), dtype=np.float32)
  for u in range(M):
      for v in range(N):
          D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
          if D <= D0:
              H[u,v] = 1
          else:
              H[u,v] = 0
              
  F = np.fft.fft2(f)
  Fshift = np.fft.fftshift(F)
  Gshift = Fshift * H
  G = np.fft.ifftshift(Gshift)
  g = np.abs(np.fft.ifft2(G))
  return g

def gaussian_noise(image, snr):
    sigma = np.var(image)
    powerOfSignal = sigma / (10 ** (snr / 10.0))
    noise = np.random.normal(0,scale=np.sqrt(powerOfSignal), size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)
    return noisy_image

f = cv2.imread('./Ders7goruntuleri/LENNAorijinal.bmp',0)

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(f,cmap='gray')
plt.title('Asıl görüntü')
plt.axis('off')

D0 = [0.05, 0.15, 0.3, 0.5, 0.85]

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(ideal_low_pass_filter(f,item),cmap='gray')
  plt.title(f'D0 = {item}')
  plt.axis('off')

plt.show()

gaussian_noise_image = gaussian_noise(f, 10)
plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(gaussian_noise_image,cmap='gray')
plt.title('Gauss gürültülü görüntü, SNR(dB) = 10')
plt.axis('off')

D0 = [0.05, 0.15, 0.3, 0.5, 0.85]

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(ideal_low_pass_filter(gaussian_noise_image,item),cmap='gray')
  plt.title(f'D0 = {item}')
  plt.axis('off')

plt.tight_layout()
plt.show()