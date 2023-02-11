import cv2
import numpy as np

img = cv2.imread("logo.png")
#img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

grayImg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grayNP= np.array(grayImg) 
print(np.unique(grayNP))
 
ret,thresh = cv2.threshold(grayImg,0,255,cv2.THRESH_BINARY) 
grayNP= np.array(grayImg) 
print(np.unique(grayNP)) 

cv2.imshow('window logo',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()