import cv2

img = cv2.imread("Media/logo.png")

cv2.imwrite("Media/newLogo.png", img)

cv2.imshow('logo window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
