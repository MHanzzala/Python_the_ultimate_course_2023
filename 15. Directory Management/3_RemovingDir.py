import os
import shutil

folders = ["scripts", "libs", "data"]

for f in folders:

    try:
        shutil.rmtree(f)
    except OSError as error:
        print(error)
