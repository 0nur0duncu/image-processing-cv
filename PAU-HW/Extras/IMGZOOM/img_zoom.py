import cv2 as cv
import matplotlib.pyplot as plt

I = cv.imread("./images/gul.jpg")
W,H,D = I.shape


plt.subplot(211)
plt.imshow(cv.cvtColor(I, cv.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(212)
K = I[200:775,200:775]
plt.imshow(cv.cvtColor(K, cv.COLOR_BGR2RGB))
plt.axis("off")

"""plt.subplot(223)
L = I[1:10:W,1:10:H]
plt.imshow(cv.cvtColor(L, cv.COLOR_BGR2RGB))
plt.axis("off")"""

plt.tight_layout()
plt.show()

B = cv.resize(I, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)
plt.subplot(211)
plt.imshow(cv.cvtColor(B, cv.COLOR_BGR2RGB))

S = cv.resize(I, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
plt.subplot(212)
plt.imshow(cv.cvtColor(S, cv.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
