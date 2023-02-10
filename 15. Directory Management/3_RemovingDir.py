# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:43:42 2022

@author: Hamsho
"""

import os
import shutil

folders = ["scripts", "libs","data"]

for f in folders:
    
    try:
        shutil.rmtree(f)
    except OSError as error:
        print(error)


