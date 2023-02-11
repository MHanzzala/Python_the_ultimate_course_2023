
import numpy as np

arr = np.array(["hanzala", "bilal", "hamza", "bilal"])
index = np.where(arr == "bilal")
print(index[0][1])
