import cv2
import numpy as np

img = cv2.imread("logo.png")
#img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
npth= np.array(grayscale )

ret,thresh1 = cv2.threshold(grayscale,0,255,cv2.THRESH_BINARY) #all values less or equal to 0, make it 0. else all 255 or white
npth= np.array(thresh1)
vStack = np.vstack((grayscale,thresh1))
vStack = np.array(vStack)

contours, h = cv2.findContours(thresh1, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours,-1, (0,255,0), 1)
print(len(contours))
cv2.imshow('window logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()