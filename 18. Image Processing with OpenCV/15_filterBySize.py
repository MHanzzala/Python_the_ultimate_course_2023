import cv2
import numpy as np

# Read the image from file
img = cv2.imread("Media/logo.png")
original = cv2.imread("Media/logo.png")

# Convert the image to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to a NumPy array
npth = np.array(grayscale)

# Apply binary threshold to the grayscale image
# All values less than or equal to 0 will be set to 0 (black)
# All values greater than 0 will be set to 255 (white)
ret, thresh1 = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY)
npth = np.array(thresh1)

# Find contours in the thresholded image
contours, h = cv2.findContours(
    thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(img, contours, -1, (255, 0, 255), 1)

# Stack the original and modified images vertically
vStack = np.vstack((img, original))
vStack = np.array(vStack)

# Create a list to store the separate contours
imlist = []

# Iterate through the contours
for i, cnt in enumerate(contours):
    # Calculate the area of the contour
    area = cv2.contourArea(cnt)

    # Only process contours with an area greater than 26 pixels
    if area > 26:
        # Create a black image with the same shape as the original image
        im = np.zeros((img.shape[0], img.shape[1]), np.uint8)

        # Draw the contour on the black image
        cv2.drawContours(im, [cnt], -1, (255, 255, 255), -1)

        # Add the contour image to the list
        imlist.append(im)

# Calculate the midpoint of the contour list
bound1 = int(len(imlist)/2)
bound2 = len(imlist)+1

# Stack the first half of the contour images horizontally
imtoshow1 = np.hstack((imlist[0:bound1]))

# Stack the second half of the contour images horizontally
imtoshow2 = np.hstack((imlist[bound1:bound2]))

# Display the first stack of contour images
cv2.imshow('Window Logo 1', imtoshow1)

# Display the second stack of contour images
cv2.imshow('Window Logo 2', imtoshow2)

# Wait for a key press
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
