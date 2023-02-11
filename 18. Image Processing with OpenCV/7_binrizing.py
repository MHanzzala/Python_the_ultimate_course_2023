import cv2
import numpy as np

# Load the image
img = cv2.imread("Media/logo.png")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Print the unique values in the grayscale image
gray_np = np.array(gray_img)
print("Unique values in grayscale image:", np.unique(gray_np))

# Apply thresholding to the grayscale image
ret, thresholded_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY)

# Print the unique values in the thresholded image
thresholded_np = np.array(thresholded_img)
print("Unique values in thresholded image:", np.unique(thresholded_np))

# Save the thresholded image
cv2.imwrite("Media/threshold_logo.png", thresholded_img)

# Display the thresholded image
cv2.imshow("LOGO", thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
