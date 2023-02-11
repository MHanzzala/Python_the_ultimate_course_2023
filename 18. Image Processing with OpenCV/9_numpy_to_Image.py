import cv2
import numpy as np
from numpy.random import default_rng

img = np.random.default_rng().integers(2, size=(200, 200))
img = np.array(img, dtype=np.uint8)
cv2.imshow('logo window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
