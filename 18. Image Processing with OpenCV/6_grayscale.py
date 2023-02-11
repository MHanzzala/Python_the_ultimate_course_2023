import cv2

#img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("logo.png")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

cv2.imshow('window logo', grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()