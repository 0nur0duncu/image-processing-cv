import cv2 as cv
import numpy as np

M = np.zeros((256,256),dtype=np.uint8)
M[:,:] = np.arange(256)

"""for i in range(256):
  M[i,:] = [j for j in range(256)]"""
  
cv.imshow("2D-RAMP-FNC",M)
cv.imwrite("2d_ramp_function.png",M)
cv.waitKey(0)
cv.destroyAllWindows()