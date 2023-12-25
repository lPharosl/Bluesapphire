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
from datetime import datetime
# Input file

text_file = open(r'C:\Users\sheep\OneDrive\Bluesapphire\Pattern\Processing\01Colorcheck'+'\\log.txt',"a")

    
Folder = os.getcwd()
Indirection = Folder+"\\Input"
name = os.listdir(Indirection)
k = len(name)

def palette_from_dict(c_dict):
        palette = [] 
        for i in np.arange(256):
            if i in c_dict:
                palette.extend(c_dict[i])
            else:
                palette.extend([0, 0, 0])
        return palette

# Preparing image for run


# Convert and Save image file for analysis   
def Preparingimage(k,Indirection,name,Folder): 
    Message = "Picture:"+ str(int(i)+1) + " of "+str(k)+'\n'+name[i]
    print(Message)
    text_file.write(str(datetime.now("%d-%m-%Y, %H:%M:%S"))+Message)
    filename = (name[i].split(".png",1))[0]
    output = Folder+'\\Backup\\First'
    complete = Folder+'\\Backup\\Final'
    Defect = pd.DataFrame([1,2])
    imo = Image.open(Folder+"\\Input\\"+filename+".png")
    imo.save(output+"\\bmp\\"+filename+".bmp")
    imo.save(complete+"\\bmp\\"+filename+".bmp")
    imo.save(complete+"\\png\\"+filename+".png")
    return filename,output,complete,Defect


# Check Original file result   
def Colorcheck(filename,output,complete,State):
    new = Image.open(output+"\\bmp\\"+filename+".bmp")
    converted = new.quantize(colors=8, method=None, kmeans=0, palette=None)
    # converted
    converted.save(complete+"\\Convert\\"+filename+"con.bmp")
    p = np.array(converted)
    PILImage = Image.fromarray(p, mode='P')

    White = [255, 255, 255] 

    Black   = 	[0, 0, 0]	    #000000 
    White   =	[255, 255, 255]	#FFFFFF 
    Red	    =   [255, 0, 0]	    #FF0000 
    Green   =	[0, 255, 0]	    #00FF00
    Blue    =   [0, 0, 255]	    #0000FF
    Yellow	=   [255, 255, 0]	#FFFF00
    Cyan	=   [0, 255, 255]	#00FFFF
    Magenta	=   [255, 0, 255]	#FF00FF
    colors_dict = {0: White, 1:Green, 2:Blue, 3: Cyan, 4: Red, 5:Yellow, 6: Magenta, 7: Black }
#   print (colors_dict)

    PILImage.putpalette(palette_from_dict(colors_dict))
    PILImage.save(output+"\\Colorcheck\\"+filename+"C.bmp")
    
    # out_dir = r'C:\Users\anupo\OneDrive\Bluesapphire\Pattern\Processing\01Colorcheck\first'
    cnt = 0
    for img in glob.glob(Indirection+"\\"+filename+'C.bmp'):
        Image.open(img)
        Image.open(img).resize((300,300)).save(os.path.join(Folder+"\\"+State, str(filename)+'.png'))
        cnt += 1
    return colors_dict,PILImage
    #PILImage.show()
def Exportexcel(PILImage,complete,filename):
    p = np.array(PILImage)

    df = pd.DataFrame(p)
    def color(a):
        d = {0: 'White', 1:'Green', 2:'Blue', 3: 'Cyan', 4: 'Red', 5:'Yellow', 6: 'Magenta', 7: 'Black' }
        d1 = {k: 'background-color:' + v for k, v in d.items()}
        df1 = pd.DataFrame(index=a.index, columns=a.columns)
        df1 = a.applymap(d1.get).fillna('')
        return df1
    df.style.apply(color,axis = None).to_excel(complete+"\\Excel\\"+filename+'.xlsx',sheet_name='Code')

    with pd.ExcelWriter(complete+"\\Excel\\"+filename+'.xlsx', engine='openpyxl', mode='a') as writer:
        Rowcolor= pd.DataFrame(map(set,df.values)) 
        Rowcolor["sum"] = Rowcolor.sum(axis=1)
        Rowcolor["count"] = pd.DataFrame(map(set,df.values)).count(axis=1)
        Rowcolor["Colorcount"] = pd.DataFrame(df.apply(pd.Series.value_counts).sum(axis=1))
        Defect =Rowcolor["Colorcount"].index[Rowcolor["Colorcount"]<60]
        text_file.write(str(datetime.now("%d-%m-%Y, %H:%M:%S"))+str(Defect)+'\n')
        print (Defect)

        Target = set(np.concatenate(df.values))
        j = []
        f = []
        for t in Target:
            target_value = t  
            values_all=[]
            values_in = []
            for r in range(0,len(df)):
                row = df.iloc[r].values
                values_all.extend(row)
                if target_value in row:
                    values_in.extend(row)

            values_all = sorted(set(values_all))
            values_in = sorted(set(values_in))

            values_out = values_all
            for i in values_in:
                values_out.remove(i)
            values_out = sorted(values_out)
            f = np.array(values_out)
            
            j.append(f)
        


        Rowcolor.to_excel(writer,sheet_name='Summary')
        Rowcolor = pd.DataFrame(j)
        Rowcolor["Target"] = pd.DataFrame(Target)
        Rowcolor.to_excel(writer,sheet_name='Test')        
#        print(df)
        im  = Image.open(complete+"\\png\\"+filename+".png")
    return df
# Output cure image process
def ExportCureimage(colors_dict,complete,filename,State,Defect):
    while Defect.size > 0:
        # test =sns.color_palette("husl", 8)
        # test.show()
        palette_from_dict(colors_dict)
        Colorcheck(filename,complete,complete,State)
        Exportexcel()
    #     new = Image.open(complete+"\\bmp\\"+filename+".bmp")
    #     converted = new.quantize(colors=8, method=None, kmeans=0, palette=None)
    #     # converted
    #     converted.save(complete+"\\Convert\\"+filename+"con.bmp")

    #     # converted.show()
    #     p = np.array(converted)
    # #   print(p)


        
    #     PILImage = Image.fromarray(p, mode='P')

    #     White = [255, 255, 255] 

    #     Black   = 	[0, 0, 0]	    #000000 
    #     White   =	[255, 255, 255]	#FFFFFF 
    #     Red	    =   [255, 0, 0]	    #FF0000 
    #     Green   =	[0, 255, 0]	    #00FF00
    #     Blue    =   [0, 0, 255]	    #0000FF
    #     Yellow	=   [255, 255, 0]	#FFFF00
    #     Cyan	=   [0, 255, 255]	#00FFFF
    #     Magenta	=   [255, 0, 255]	#FF00FF
    #     colors_dict = {0: Black, 1:Green, 2:Blue, 3: Cyan, 4: Red, 5:Yellow, 6: Magenta, 7: White }
    # #   print (colors_dict)

    #     PILImage.putpalette(palette_from_dict(colors_dict))
    #     PILImage.save(complete+"\\Colorcheck\\"+filename+"C.bmp")
        
    #     # out_dir = r'C:\Users\anupo\OneDrive\Bluesapphire\Pattern\Processing\01Colorcheck\output'
    #     cnt = 0
    #     for img in glob.glob(Indirection+filename+'C.bmp'):
    #         Image.open(img)
    #         Image.open(img).resize((300,300)).save(os.path.join(Folder+"\\Final", str(filename)+'.png'))
    #         cnt += 1
        


# Export color value to excel


## Cure image Color
    def Cureimage():
            if Defect.size >0 :
                for row in range(df.shape[0]): # df is the DataFrame
                    for col in range(df.shape[1]):
                        for i in range(0,Defect.size):
                            if df.loc[row,col] == Defect[i]:
                                
                                
                                im  = Image.open(complete+"\\png\\"+filename+".png") # Can be many different formats.
                                pix = im.load()

                                try :
                                    NW  = str(pix[col-1,row-1])
                                except:
                                    NW  = "Blank"
                                try :
                                    N   = str(pix[col,row-1])
                                except:
                                    N   = "Blank"
                                try :                        
                                    NE  = str(pix[col+1,row-1])
                                except:
                                    NE  = "Blank"
                                try :
                                    E   = str(pix[col+1,row])
                                except:
                                    E   = "Blank"
                                try :
                                    SE  = str(pix[col+1,row+1])
                                except:
                                    SE  = "Blank"
                                try :                            
                                    S   = str(pix[col,row+1])
                                except:
                                    S   = "Blank"
                                try :
                                    SW  = str(pix[col-1,row+1])
                                except:
                                    SW   = "Blank"
                                try :
                                    W   = str(pix[col-1,row])    
                                except:
                                    W   = "Blank"

                                surcolor= [NW,N,NE,E,SE,S,SW,W]
                                
                                while 'Blank' in surcolor:
                                    surcolor.remove('Blank')

                                # try :

                                # l = ['(31, 41, 57, 255)', '(31, 41, 57, 255)', '(209, 45, 0, 255)', '(209, 45, 0, 255)', '(209, 45, 0, 255)', '(31, 41, 57, 255)', '(31, 41, 57, 255)', '(31, 41, 57, 255)']
                                # print(L)

        #                             
                                # except:
                                #     pass

        #                       surcolor= [N,E,S,W]
                                test = dict(Counter(surcolor))
                                result = max(test,key=test.get)

                                    
                        
        #                       print(result)
        #                       print (im.size)  # Get the width and hight of the image for iterating over
        #                       print (pix[col-1,row])
        #                        print (pix[col,row])  # Get the RGBA Value of the a pixel of an image
                                pix[col,row] = tuple(map(int,result.replace('(','').replace(')','').replace(' ','').split(','))) # Set the RGBA Value of the image (tuple)
                                
                                im.save(complete+"\\png\\"+filename+'.png')  # Save the modified pixels as .png
            im.save(complete+"\\bmp\\"+filename+'.bmp')
            new = Image.open(complete+"\\bmp\\"+filename+".bmp")
            converted = new.quantize(colors=8, method=None, kmeans=0, palette=None)
                # converted
            converted.save(complete+"\\Convert\\"+filename+"con.bmp")

                # converted.show()
            p = np.array(converted)
            #   print(p)

            PILImage = Image.fromarray(p, mode='P')        
            PILImage.putpalette(palette_from_dict(colors_dict))
            PILImage.save(complete+"\\Colorcheck\\"+filename+"C.bmp")
            # out_dir = r'C:\Users\anupo\OneDrive\Bluesapphire\Pattern\Processing\01Colorcheck\output'
            cnt = 0
            for img in glob.glob(Indirection+filename+'C.bmp'):
                Image.open(img)
                Image.open(img).resize((300,300)).save(os.path.join(Folder+"\\Final", str(filename)+'.png'))
                cnt += 1
#  Move out file         
Finalmove = Folder+'\\Backup\\Final\\PNG'
Check1stmove = Folder+'\\Backup\\First\\Colorcheck'
CheckFimove = Folder+'\\Backup\\Final\\Colorcheck'

outputpath = Folder+'\\Output'
Chkoutputpath = Folder+'\\Check'
for f in os.listdir(Finalmove):
    try:
        os.remove(os.path.join(outputpath, f))
    except:
        pass
    shutil.move(os.path.join(Finalmove, f),outputpath)

for f in os.listdir(Check1stmove):
    try:
        os.remove(os.path.join(Chkoutputpath+'\\First', f))
    except:
        pass
    shutil.move(os.path.join(Check1stmove, f),Chkoutputpath+'\\First')
for f in os.listdir(CheckFimove):
    try:
        os.remove(os.path.join(Chkoutputpath+'\\Final', f))
    except:
        pass
    shutil.move(os.path.join(CheckFimove, f),Chkoutputpath+'\\Final')        
    #PILImage.show()                        
text_file.write(str(datetime.now("%d-%m-%Y, %H:%M:%S"))+"Complete")
text_file.close()
print ("Complete")



# %%
# Cleanup script

Afolder = Folder+'\\Backup\\'

for F in os.listdir(Afolder): #Get Folder First and Final
    for I in os.listdir(os.path.join(Afolder,F)): #Get SubFolder in First and Final
        for N in os.listdir(os.path.join(Afolder,F,I)):    
            text_file.write(str(os.path.join(Afolder,F,I,N))+'\n')
            print((os.path.join(Afolder,F,I,N)))
text_file.close()
#%%

def main():
    for i in range(0,k):
        filename,output,complete,Defect= Preparingimage(k,Indirection,name,Folder)
        State = "First"
        colors_dict,PILImage = Colorcheck(filename,output,complete,State)
        State = "Final"
        while Defect.size > 0:
            ExportCureimage(colors_dict,complete,filename,State,Defect)
            Exportexcel(PILImage,complete,filename)



#%%
