import cv2
import numpy as np

img = cv2.imread("logo.png")
#img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
 
cv2.imshow('window logo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()