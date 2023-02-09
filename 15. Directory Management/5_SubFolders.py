
import os

folders = ["scripts", "libs", "data"]
subScripts = ["preProcImg", "preProcTable"]

base = os.getcwd()

for f in folders:

    try:
        os.makedirs(f)
    except OSError as error:
        print(error)

for f in subScripts:
    path = os.path.join(base, folders[0], f)
    try:
        os.makedirs(path)
    except OSError as error:
        print(error)
