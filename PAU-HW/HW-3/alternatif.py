import cv2 as cv
import matplotlib.pyplot as plt

I = cv.imread("../Hafta3resimler/images.jpeg")

plt.subplot(221)
plt.imshow(cv.cvtColor(I,cv.COLOR_BGR2RGB))
plt.axis("off")
plt.title("256 X 256")

plt.subplot(222)
I1 = I.copy()
plt.imshow(cv.cvtColor(I1[::2,::2],cv.COLOR_BGR2RGB))
plt.axis("off")
plt.title("128 X 128")

plt.subplot(223)
I2 = I.copy()
plt.imshow(cv.cvtColor(I2[::4,::4],cv.COLOR_BGR2RGB))
plt.axis("off")
plt.title("64 X 64")

plt.subplot(224)
I3 = I.copy()
plt.imshow(cv.cvtColor(I3[::8,::8],cv.COLOR_BGR2RGB))
plt.axis("off")
plt.title("32 X 32")

plt.tight_layout()
plt.show()