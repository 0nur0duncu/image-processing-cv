import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

I = cv.imread("./images/lenna256.jpg")

plt.subplot(221)
plt.imshow(cv.cvtColor(I,cv.COLOR_BGR2RGB))
plt.title("Original image")

plt.subplot(222)
H = np.flip(I, axis=1)
plt.imshow(cv.cvtColor(H,cv.COLOR_BGR2RGB))
plt.title("Horizontal reflection")

plt.subplot(223)
V = np.flip(I, axis=0)
plt.imshow(cv.cvtColor(V,cv.COLOR_BGR2RGB))
plt.title("Vertical reflection")

plt.tight_layout()
plt.show()