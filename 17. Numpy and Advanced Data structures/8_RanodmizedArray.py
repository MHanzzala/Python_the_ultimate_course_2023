import numpy as np

from numpy.random import default_rng

randomArray = np.random.default_rng().integers(10, size=(5, 5))
print(randomArray)
