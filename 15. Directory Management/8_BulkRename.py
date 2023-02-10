# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:43:42 2022

@author: Hamsho
"""

import os

dirList = os.listdir()
print(dirList)
baseName= "dataset"
extension = ".jpg"

for i,img in enumerate(dirList):
    imgName = baseName + str(i) + extension
 
    try:
        os.rename(img, imgName)
    except OSError as error:
        print(error)

 