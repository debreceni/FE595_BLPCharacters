# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:47:09 2019

@author: Dave
"""

import HeroFiles
import os
from textblob import TextBlob
import numpy as np
import pandas as pd

def Get_CommonDescriptors(outfiles, dirpath):
     #read in files for processing
    with open(outfiles['hefile'], 'r') as f:
        helst = f.readlines()
        
    with open(outfiles['shefile'], 'r') as f:
        shelst = f.readlines()
        
    cmblst = ' '.join(helst+shelst)
    
    tbObj = TextBlob(cmblst)
    lstdescr = [phrase for phrase in tbObj.noun_phrases]
    #create a unique list
    lstdescr = list(set(lstdescr))
    cntdescr = [tbObj.noun_phrases.count(phrase) for phrase in lstdescr]
    
    dfDescr = pd.DataFrame(list(zip(lstdescr,cntdescr)), columns=['Descriptor','Count'])
    
    dfDescr.sort_values('Count', ascending=False).head(10).to_csv(os.path.join(dirpath,'Top10Descriptors.txt'), index=None, sep='\t')
    
    return 



dirpath = os.path.join(os.getcwd(),'datafiles')
outfiles = HeroFiles.BuildConsolidatedFile(dirpath)

Get_CommonDescriptors(outfiles, dirpath)
