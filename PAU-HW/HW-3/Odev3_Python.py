######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image_path = "./images/kelebekler_vadisi.jpg"
I = cv.imread(image_path)
W, H, _ = I.shape

# B, G, R = cv.split(I)
# I = np.uint8(0.299*R + 0.587*G + 0.114*B) # gray

plt.figure(figsize=(10,6))
for i in range(6):
    resized_image = cv.resize(I, (H // 2**i, W // 2**i))

    plt.subplot(2, 3, i+1)
    plt.imshow(cv.cvtColor(resized_image,cv.COLOR_BGR2RGB))
    plt.title(f"{W // 2**i} X {H // 2**i}")
    # plt.axis('off')

plt.tight_layout()
plt.show()
