
import numpy as np

arr = np.array(["john","mrhamsho","jack","mrhamsho"])
index= np.where(arr=="mrhamsho")
print(index[0][1])