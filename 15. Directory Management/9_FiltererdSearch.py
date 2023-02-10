
import os

dirList = os.listdir()
# dirList = [x for x in dirList if not x.endswith('jpg')]
print(dirList)
baseName = "data"
extension = ".jpg"

for i, img in enumerate(dirList):

    imgName = baseName + str(i) + extension

    try:
        os.rename(img, imgName)
    except OSError as error:
        print(error)
