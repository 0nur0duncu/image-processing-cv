import cv2 as cv
import numpy as np

BGR = cv.imread("./images/lenna256.jpg")
B, G, R = cv.split(BGR)

gray = np.uint8(0.299*R + 0.587*G + 0.114*B)
cv.imshow("RGB2GRAY", gray)
cv.waitKey(0)
cv.destroyAllWindows()