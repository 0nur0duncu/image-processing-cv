######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image_path = "./images/boncuklu_koyu.jpg"
I = cv.imread(image_path)

B, G, R = cv.split(I)

gray = np.uint8(0.299*R + 0.587*G + 0.114*B)

bit = 8

plt.figure(figsize=(10,6))
for i in range(8):
    
    
    plt.subplot(2, 4, i+1, frameon=False)
    plt.imshow(gray,cmap="gray")
    plt.title(f"m = {bit} bit, G = {2**bit}")
    plt.axis('off')
    gray = gray // 2
    bit = bit - 1
    
plt.tight_layout()
plt.show()