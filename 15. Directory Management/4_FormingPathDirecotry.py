import os
folders = ["scripts", "libs", "data"]
subScript = ["prePorcImg", "preProcTable"]


base = os.getcwd()

for f in folders:
    try:
        os.makedirs(f)
    except OSError as error:
        print(error)

for f in subScript:
    path = os.path.join(base, folders[0], f)
    try:
        os.makedirs(f)
    except OSError as error:
        print(error)
