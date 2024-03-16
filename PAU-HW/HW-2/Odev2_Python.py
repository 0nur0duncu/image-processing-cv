######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################


import cv2 as cv
import numpy as np

img = cv.imread("./images/peppers.png")
BGR = np.float32(img) / 255
B, G, R = cv.split(BGR)

numerator=1/2*((R-G)+(R-B))
denominator = np.power(np.power(R-G,2)+(R-B) * (G-B),0.5)
H = np.arccos(np.divide(numerator,denominator+0.000001))
H[B>G]=360-H[B>G]

H = np.divide(H,360)
S = 1 - (3 / (R + G + B) * np.minimum(np.minimum(R, G), B))

I = np.divide(B + G + R, 3)


HSI = cv.merge((H, S, I))
cv.imshow("RGB2HSI", cv.cvtColor(HSI,cv.COLOR_BGR2RGB))
cv.waitKey(0)
cv.destroyAllWindows()