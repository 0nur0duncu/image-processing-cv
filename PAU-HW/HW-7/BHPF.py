import cv2
import numpy as np
import matplotlib.pyplot as plt

def butterwort_high_pass_filter(f,D0,n):
  global Fshift
  M,N = f.shape
  H = np.zeros((M,N), dtype=np.float32)
  D0 *= 100
  for u in range(M):
      for v in range(N):
          D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
          H[u,v] = 1 / (1 + (D0/D)**n)
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

f = cv2.imread('./Ders7goruntuleri/cameraman.tif',0)


F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(f,cmap='gray')
plt.title('Asıl görüntü')
plt.axis('off')

D0 = [0.1, 0.2, 0.3, 0.5, 0.7]

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(butterwort_high_pass_filter(f,item,1),cmap='gray')
  plt.title(f'D0 = {item}, n=1')
  plt.axis('off')

plt.tight_layout()
plt.show()

gaussian_noise_image = gaussian_noise(f, 10)
F = np.fft.fft2(gaussian_noise_image)
Fshift = np.fft.fftshift(F)

plt.figure(figsize=(10,6))
plt.subplot(221)
plt.imshow(gaussian_noise_image,cmap='gray')
plt.title('Gauss gürültülü görüntü, SNR(dB) = 10')
plt.axis('off')

n = [1,3,15]

for index,item in enumerate(n):
  plt.subplot(2,2,index+2)
  plt.imshow(butterwort_high_pass_filter(gaussian_noise_image,0.3,item),cmap='gray')
  plt.title(f'D0 = 0.3, n={item}')
  plt.axis('off')

plt.tight_layout()
plt.show()