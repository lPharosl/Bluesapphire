#%%
from enum import unique
from itertools import count
from telnetlib import SE
from tkinter import E, N, NE, NW, S, SW
from typing import List
from matplotlib.style import library
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
Inputpath = PFolder[0]+'\\03Finishingimage\\Input'
Librarypath = PFolder[0]+'\\05MovetoCatalog\\OriginalPNG'
photoshoppath = Folder+'\\Output'
photoshoppathInput = Folder+'\\Input'
for f in os.listdir(photoshoppath):
    try:
        os.remove(os.path.join(Inputpath,f))
    except:
        pass
    shutil.move(os.path.join(photoshoppath, f),Inputpath)
for f in os.listdir(photoshoppathInput):
    try:
        os.remove(os.path.join(Librarypath,f))
    except:
        pass
    shutil.move(os.path.join(photoshoppathInput, f),Librarypath)
# %%
