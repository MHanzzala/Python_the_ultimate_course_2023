import numpy as np

from numpy.random import default_rng

randomArr=np.random.default_rng().integers(10, size=(5,8))
print(randomArr)