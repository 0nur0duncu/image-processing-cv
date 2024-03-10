import numpy as np
import cv2 as cv

image = np.zeros((512, 512), dtype=np.uint8)

center = (256, 256)
radius = 100

# cv.circle(M, (256,256), 100, 255, thickness=-1)

for i in range(512):
    for j in range(512):
        distance = np.sqrt((i - center[0])**2 + (j - center[1])**2)
        if distance <= radius:
            image[i, j] = 255

cv.imshow("Circle", image)
cv.imwrite("circle.png",image)
cv.waitKey(0)
cv.destroyAllWindows()
