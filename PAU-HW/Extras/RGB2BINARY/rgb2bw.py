import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


I = cv.imread("./images/shapes.bmp")

plt.subplot(211)
plt.axis("off")
plt.imshow(cv.cvtColor(I,cv.COLOR_BGR2RGB))
plt.title("original image")

"""W, H, D = I.shape
for i in range(W):
  for j in range(H):
    if sum(I[i,j,:])>0:
      I[i,j,:] =255"""

I[np.sum(I, axis=2) > 0] = 255

plt.subplot(212)
plt.axis("off")
plt.imshow(cv.cvtColor(I,cv.COLOR_BGR2RGB))
plt.title("binary image")

plt.tight_layout()
plt.show()