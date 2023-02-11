
import numpy as np

a= np.array([50,2,1,2,1,7,9,2,1])

spliting= np.hsplit(a, 3)
print(spliting[0])
print(spliting[1])
print(spliting[2])