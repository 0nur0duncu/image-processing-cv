import cv2 as cv
import matplotlib.pyplot as plt

I = cv.imread("./images/peppers.png")

plt.subplot(2, 2, 1)
K = cv.resize(I, (25, 25))
plt.imshow(cv.cvtColor(K, cv.COLOR_BGR2RGB))

plt.subplot(2, 2, 2)
L1 = cv.resize(I, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
plt.imshow(cv.cvtColor(L1, cv.COLOR_BGR2RGB))

plt.subplot(2, 2, 3)
L2 = cv.resize(I, None, fx=0.5, fy=0.5, interpolation=cv.INTER_NEAREST)
plt.imshow(cv.cvtColor(L2, cv.COLOR_BGR2RGB))

plt.subplot(2, 2, 4)
L3 = cv.resize(I, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
plt.imshow(cv.cvtColor(L3, cv.COLOR_BGR2RGB))

plt.tight_layout()  # Alt ve üst etiketlerin çakışmasını önler
plt.show()