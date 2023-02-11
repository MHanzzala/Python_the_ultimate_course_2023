
import numpy as np

a= np.array([50,2,1,2,1,7,9,2])
b= np.array([2,5,8])
d= np.array([20,30,1])
c= np.concatenate([b,a,d]) 
print(c)