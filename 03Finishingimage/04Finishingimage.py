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
# Input file

Folder = os.getcwd()
Indirection = Folder+"\\Input"
name = os.listdir(Indirection)
k = len(name)

# Preparing image for run
for i in range(0,k):
    print("Picture:",i+1," of ",k)
    print(name[i])
    
    filename = (name[i].split(".png",1))[0]
    output = Folder+'\\output'
    Defect = pd.DataFrame([1,2])
    imo = Image.open(Folder+"\\Input\\"+filename+".png")
    imo.save(output+"\\bmp\\"+filename+".bmp")
    imo.save(output+"\\png\\"+filename+".png")
    # test =sns.color_palette("husl", 8)
    # test.show()
#  Move out file       
Finalmove = Folder+'\\Backup\\Final\\'
Outputfolder = ['PNG','BMP']
Check1stmove = Folder+'\\Backup\\First\\Colorcheck'
CheckFimove = Folder+'\\Backup\\Final\\Colorcheck'

outputpath = Folder+'\\Output'
Chkoutputpath = Folder+'\\Check'
for e in Outputfolder:
    k = os.path.join(Finalmove,e)
    o = os.path.join(outputpath,e)
    for f in os.listdir(k):
        shutil.move(os.path.join(k, f),o)

for f in os.listdir(Check1stmove):
    try:
        os.remove(os.path.join(Chkoutputpath+'\\First', f))
    except:
        pass
    shutil.move(os.path.join(Check1stmove, f),Chkoutputpath+'\\First')
for f in os.listdir(CheckFimove):
    try:
        os.remove(os.path.join(Chkoutputpath+'\\Final',f))
    except:
        pass
    shutil.move(os.path.join(CheckFimove, f),Chkoutputpath+'\\Final')        
    #PILImage.show()                        
print ("Complete")


# %%
# Cleanup script

Afolder = Folder+'\\Backup\\'

for F in os.listdir(Afolder): #Get Folder First and Final
    for I in os.listdir(os.path.join(Afolder,F)): #Get SubFolder in First and Final
        for N in os.listdir(os.path.join(Afolder,F,I)):    
            print((os.path.join(Afolder,F,I,N)))

# %%
