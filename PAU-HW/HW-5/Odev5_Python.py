######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import numpy as np
import cv2
import matplotlib.pyplot as plt

def gaussian_noise(image, snr):
    sigma = np.var(image)
    powerOfSignal = sigma / (10 ** (snr / 10.0))
    noise = np.random.normal(0,scale=np.sqrt(powerOfSignal), size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)

    return noisy_image

def low_pass_filter(image,kernel):
    return cv2.filter2D(image, -1, kernel)

image = cv2.imread('./images/LENNAorijinal.bmp',cv2.IMREAD_GRAYSCALE)

SNR = [10,20,0]
for j in SNR:
    noisy_image = gaussian_noise(image, j)

    plt.figure(figsize=(8,6))
    plt.subplot(221)
    plt.axis("off")
    plt.title(f"Toplumsal Gauss gürültüsü ile bozulmuş görüntü SNR = {j} dB",fontsize=6)
    plt.imshow(noisy_image,cmap='gray')

    kernel_3x3_1 = np.ones((3, 3), np.float32) / 9

    plt.subplot(222)
    plt.axis("off")
    plt.title("AGS1 ile elde edilen görüntü",fontsize=6)
    plt.imshow(low_pass_filter(noisy_image,kernel_3x3_1),cmap='gray')

    kernel_3x3_2 = np.matrix([[1,1,1],[1,2,1],[1,1,1]], np.float32)/10

    plt.subplot(223)
    plt.axis("off")
    plt.title("AGS2 ile elde edilen görüntü",fontsize=6)
    plt.imshow(low_pass_filter(noisy_image,kernel_3x3_2),cmap='gray')

    kernel_3x3_3 = np.matrix([[1,2,1],[2,4,2],[1,2,1]], np.float32)/16

    plt.subplot(224)
    plt.axis("off")
    plt.title("AGS3 ile elde edilen görüntü",fontsize=6)
    plt.imshow(low_pass_filter(noisy_image,kernel_3x3_3),cmap='gray')
    plt.tight_layout()
    plt.savefig(f"./images/decibel_{j}/decibel_{j}_AGS[1,2,3].png")
    plt.show()


    plt.figure(figsize=(8,6))
    plt.subplot(321)
    plt.axis("off")
    plt.title(f"Toplumsal Gauss gürültüsü ile bozulmuş görüntü SNR = {j} dB",fontsize=6)
    plt.imshow(noisy_image,cmap='gray')

    k_s = [3,5,7,9,15]
    for i in range(5):
        kernel_3x3 = np.ones((k_s[i], k_s[i]), np.float32) / (k_s[i]**2)
        plt.subplot(3,2,i+2)
        plt.axis("off")
        plt.title(f"AGS1 {k_s[i]}x{k_s[i]} ile elde edilen görüntü",fontsize=6)
        plt.imshow(low_pass_filter(noisy_image,kernel_3x3),cmap='gray')
        
    plt.tight_layout()
    plt.savefig(f"./images/decibel_{j}/decibel_{j}_AGS1_kernel{k_s}.png")
    plt.show()