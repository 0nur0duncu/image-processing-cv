import cv2 as cv
import matplotlib.pyplot as plt


I = cv.imread("./images/peppers.png")
height, width = I.shape[:2]
centerX, centerY = (width // 2, height // 2)

plt.subplot(221)
B1 = cv.getRotationMatrix2D((centerX, centerY), 30, 1.0)
B1 = cv.warpAffine(I, B1, (width, height))
plt.imshow(cv.cvtColor(B1,cv.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(222)
B2 = cv.getRotationMatrix2D((centerX, centerY), -90, 1.0)
B2 = cv.warpAffine(I, B2, (width, height))
plt.imshow(cv.cvtColor(B2,cv.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(223)
B3 = cv.getRotationMatrix2D((centerX, centerY), 90, 1.0)
B3 = cv.warpAffine(I, B3, (width, height))
plt.imshow(cv.cvtColor(B3,cv.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(224)
B4 = cv.getRotationMatrix2D((centerX, centerY), -30, 1.0)
B4 = cv.warpAffine(I, B4, (width, height))
plt.imshow(cv.cvtColor(B4,cv.COLOR_BGR2RGB))
plt.axis("off")

plt.show()