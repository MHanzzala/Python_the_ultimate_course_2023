import os

dirList = os.listdir()
print(dirList)
baseName = "dataset"
extension = ".jpg"

for i, img in enumerate(dirList):
    imgName = baseName + str(i) + extension

    try:
        os.rename(img, imgName)
    except OSError as error:
        print(error)
