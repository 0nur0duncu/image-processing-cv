import cv2
import numpy as np
import matplotlib.pyplot as plt

D0 = [0.1, 0.2, 0.3, 0.5, 0.7]

def ideal_high_pass_filter(f,D0):
  global Fshift
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
              
  H = 1 - H
  Gshift = Fshift * H
  G = np.fft.ifftshift(Gshift)
  g = np.abs(np.fft.ifft2(G))
  return g

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

def gaussian_high_pass_filter(f, sigma):
    global Fshift
    M,N = f.shape
    sigma *= 100
    H = np.zeros((M,N), dtype=np.float32)
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            H[u,v] = np.exp(-D**2/(2*sigma*sigma))
    H = 1 - H
    Gshift = Fshift * H
    G = np.fft.ifftshift(Gshift)
    g = np.abs(np.fft.ifft2(G))
    return g

f = cv2.imread('./images/cameraman.tif',0)
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(f,cmap='gray')
plt.title('Asıl görüntü')
plt.axis('off')

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(ideal_high_pass_filter(f,item),cmap='gray')
  plt.title(f'D0 = {item}')
  plt.axis('off')

plt.tight_layout()
plt.savefig('./images/ideal_high_pass_filter.png')

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(f,cmap='gray')
plt.title('Asıl görüntü')
plt.axis('off')

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(butterwort_high_pass_filter(f,item,1),cmap='gray')
  plt.title(f'D0 = {item}, n=1')
  plt.axis('off')

plt.tight_layout()
plt.savefig('./images/butterwort_high_pass_filter.png')

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(f,cmap='gray')
plt.title('Asıl görüntü')
plt.axis('off')

for index,item in enumerate(D0):
  plt.subplot(2,3,index+2)
  plt.imshow(gaussian_high_pass_filter(f,item),cmap='gray')
  plt.title(f'sigma = {item}')
  plt.axis('off')

plt.tight_layout()
plt.savefig('./images/gaussian_high_pass_filter.png')

plt.show()