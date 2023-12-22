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
Afolder = Folder+'\\Backup\\'

for F in os.listdir(Afolder): #Get Folder First and Final
    for I in os.listdir(os.path.join(Afolder,F)): #Get SubFolder in First and Final
        for N in os.listdir(os.path.join(Afolder,F,I)):    
            print((os.path.join(Afolder,F,I,N)))
