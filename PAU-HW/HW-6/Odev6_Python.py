######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import cv2
import numpy as np
from skimage.util import random_noise
import matplotlib.pyplot as plt

img = cv2.imread('./images/LENNAorijinal.bmp',cv2.IMREAD_GRAYSCALE)

noise_img = random_noise(img, mode='s&p', amount=0.05)

def ms2_filter(img):
  new_img = img.copy()
  row, column = img.shape
  padded_matrix = np.zeros((row+2,column+2))
  padded_matrix[1:-1, 1:-1] = img.copy()
  for i in range(row):
    for j in range(column):
      new_img[i][j] = np.median([padded_matrix[i][j+1],padded_matrix[i+1][j],padded_matrix[i+1][j+1],padded_matrix[i+1][j+2],padded_matrix[i+2][j+1]])
  return new_img

plt.figure(figsize=(6,4))
plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title('original image',fontsize=10)

plt.subplot(222)
plt.imshow(noise_img,cmap='gray')
plt.axis('off')
plt.title('salt&pepper noise',fontsize=10)

plt.subplot(223)
plt.imshow(ms2_filter(noise_img),cmap='gray')
plt.axis('off')
plt.title('MS2 median filter',fontsize=10)

plt.tight_layout()
plt.savefig("./images/figure.jpg")
plt.show()
