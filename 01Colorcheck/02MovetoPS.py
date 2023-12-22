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
PSFolder = os.path.split(Folder)

outputpath = Folder+'\\Output'
photoshoppath = PSFolder[0]+'\\02Prepareimage\\Input'
for f in os.listdir(outputpath):
    try:
        os.remove(os.path.join(photoshoppath, f))
    except:
        pass
    shutil.move(os.path.join(outputpath, f),photoshoppath)
# %%
