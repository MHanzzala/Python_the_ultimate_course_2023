import cv2
import numpy as np

# Load the image
img = cv2.imread("Media/logo.png")

# Rotate the image 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the rotated image
cv2.imwrite("Media/rotated_logo.png", rotated_img)

# Display the rotated image
cv2.imshow("Logo window", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
