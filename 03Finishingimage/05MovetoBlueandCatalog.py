#%%
from enum import unique
from itertools import count
from telnetlib import SE
from tkinter import E, N, NE, NW, S, SW
from typing import List
from pandas.core import groupby
import xlsxwriter 
from PIL import Image
import glob, os
import pandas as pd
from pandas.core.construction import array
import seaborn as sns
import numpy as np
from collections import Counter  
import shutil
Folder = os.getcwd()
PFolder = os.path.split(Folder)
BMPpath = Folder+'\\Output\\BMP'
Librarypath= PFolder[0]+'\\05MovetoCatalog\\BMP4Run'
Bluepath = PFolder[0]+'\\04MovetoBlue'
for f in os.listdir(BMPpath):
    try:
        os.remove(os.path.join(Librarypath,f))
    except:
        pass
    try:
        os.remove(os.path.join(Bluepath,f))
    except:
        pass
    shutil.copy(os.path.join(BMPpath, f),Librarypath)
    shutil.move(os.path.join(BMPpath, f),Bluepath)

# %%
