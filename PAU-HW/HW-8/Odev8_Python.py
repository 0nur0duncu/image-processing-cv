import cv2
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

def gaussian_low_pass_filter(f, sigma):
    Fshift = np.fft.fftshift(np.fft.fft2(f))
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

def gaussian_noise(image, snr):
    sigma = np.var(image)
    powerOfSignal = sigma / (10 ** (snr / 10.0))
    noise = np.random.normal(0,scale=np.sqrt(powerOfSignal), size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)
    return noisy_image,noise

Iorj = cv2.imread('./images/lenna.bmp',0)
f = Iorj.astype(np.float64)
N, M = Iorj.shape

mf = f.mean()
F = np.fft.fftshift(np.fft.fft2(f))
Pf = (F * np.conj(F))/(N * M)

g, w = gaussian_noise(Iorj,7)
mv = np.mean(w)
W = np.fft.fftshift(np.fft.fft2(w))
Pv = (W * np.conj(W))/(N * M)

H = Pf / (Pf + Pv)

e = g - (mf + mv)
A = np.fft.fftshift(np.fft.fft2(e))
Q = A * H
p = np.round(np.fft.ifft2(np.fft.fftshift(Q)) + mf)
p = np.real(p)
p = np.clip(p, 0, 255)

NMSEfg = 100 * (np.var(f - g)/np.var(f))
NMSEfp = 100 * (np.var(f - p)/np.var(f))
SNRdb = 10*np.log10(NMSEfg/NMSEfp)
print(NMSEfg, NMSEfp, SNRdb)

plt.figure(figsize=(8,6))
plt.subplot(221)
plt.imshow(Iorj,cmap='gray')
plt.title('Orjinal görüntü')
plt.axis('off')

plt.subplot(222)
plt.imshow(g,cmap='gray')
plt.title('Beyaz gürültülü görüntü, SNR(dB) = 7')
plt.axis('off')

plt.subplot(223)
plt.imshow(p,cmap='gray')
plt.title('Wiener suzgeclenmis görüntü')
plt.axis('off')

plt.subplot(224)
plt.imshow(gaussian_low_pass_filter(g,0.3),cmap='gray')
plt.title('GAGS lenmis görüntü sigma=0.3')
plt.axis('off')

plt.tight_layout()
plt.savefig('./outputs/result.png')
plt.show()