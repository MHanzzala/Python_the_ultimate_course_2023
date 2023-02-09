import os

folders = ["scripts", "libs", "data"]

for f in folders:

    try:
        os.makedirs(f)
    except OSError as error:
        print(error)
