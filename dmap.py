import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgR = cv.imread('rectified_2.png',0)
imgL = cv.imread('rectified_1.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()

cv.imshow('disparity', disparity)
cv.waitKey()
cv.destroyAllWindows()
