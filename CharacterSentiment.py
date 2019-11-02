# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:18:47 2019

@author: Dave
"""
import HeroFiles
import os
from textblob import TextBlob
import numpy as np

def Get_Sentitment(outfiles, dirpath):
    
    def getTopBottom10Sentiment(lstCharacters):
       
        lstPolarity = [TextBlob(character).sentiment.polarity for character in lstCharacters]
        idx = np.argsort(np.array(lstPolarity))
        sortedlstP = np.array(lstPolarity)[idx]
        sortedlstC = np.array(lstCharacters)[idx]
        
        top_10 = sortedlstC[-10:]
        bottom_10 = sortedlstC[:10]
        polTop10= sortedlstP[-10:]
        polBotom10 = sortedlstP[:10]
        
        return bottom_10, top_10
         
            
    def writefile(filename,data)   :
        
        with open(filename, 'w') as f:
            for line in data:
                
                f.write(line) 
            
    
    
     #read in files for processing
    with open(outfiles['hefile'], 'r') as f:
        helst = f.readlines()
        
    with open(outfiles['shefile'], 'r') as f:
        shelst = f.readlines()
    
    HEb10, HEt10 = getTopBottom10Sentiment(helst)
    SHEb10, SHEt10 = getTopBottom10Sentiment(shelst)
    
    writefile(os.path.join(dirpath,'HE_Bottom10.txt'), HEb10)
    writefile(os.path.join(dirpath,'SHE_Bottom10.txt'), SHEb10)
    writefile(os.path.join(dirpath,'HE_Top10.txt'), HEt10)
    writefile(os.path.join(dirpath,'SHE_Top10.txt'), SHEt10)

    return


    

dirpath = os.path.join(os.getcwd(),'datafiles')
outfiles = HeroFiles.BuildConsolidatedFile(dirpath)
Get_Sentitment(outfiles,dirpath)


