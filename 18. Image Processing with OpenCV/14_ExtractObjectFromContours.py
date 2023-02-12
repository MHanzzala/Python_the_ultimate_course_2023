import cv2
import numpy as np

img = cv2.imread("Media/logo.png")
original = cv2.imread("Media/logo.png")
# img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
npth = np.array(grayscale)

# all values less or equal to 0, make it 0. else all 255 or white
ret, thresh1 = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY)
npth = np.array(thresh1)


contours, h = cv2.findContours(
    thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 255), 1)

vStack = np.vstack((img, original))
vStack = np.array(vStack)

imlist = []
for i, cnt in enumerate(contours):
    im = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    cv2.drawContours(im, [cnt], -1, (255, 255, 255), -1)
    imlist.append(im)

imtoshow1 = np.hstack((imlist[0:7]))
imtoshow2 = np.hstack((imlist[7:13]))

cv2.imshow('Logo window 1', imtoshow1)
cv2.imshow('Logo window 2', imtoshow2)
cv2.waitKey(0)
cv2.destroyAllWindows()
