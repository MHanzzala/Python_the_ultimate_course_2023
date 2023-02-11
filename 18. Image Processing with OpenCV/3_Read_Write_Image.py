import cv2

img = cv2.imread("Media/logo.png")

cv2.imwrite("Media/newLogo.png", img)
