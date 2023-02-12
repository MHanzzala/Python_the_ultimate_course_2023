import cv2
import numpy as np

img1 = np.zeros((40, 40), np.uint8)
img2 = np.full((40, 40), 255, np.uint8)
img3 = np.zeros((40, 40), np.uint8)
stackVer = np.vstack((img1, img2, img3))
stackHor = np.hstack((img1, img2, img3))
stackVer = np.array(stackVer, np.uint8)
cv2.imshow('Logo Window', stackVer)
cv2.waitKey(0)
cv2.destroyAllWindows()
