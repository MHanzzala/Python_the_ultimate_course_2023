
import os
base= os.getcwd()
path = os.path.join(base, "data")
os.chdir("data")
print(os.listdir(path))
