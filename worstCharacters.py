# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:18:47 2019

@author: Dave
"""


from zipfile import ZipFile
import glob
import os


def BuildConsolidatedFile(datadir):
    
    outfile = open(os.path.join(datadir,'consolidatedCharacters.txt'), 'wb')
    for filepath in glob.glob(os.path.join(datadir,'*.zip')):
        #open the zip files to read the files
        
        zipfile = ZipFile(filepath)
        
        for fname in zipfile.infolist():
            if not fname.is_dir() and not fname.filename.startswith('__MACOSX'):            
                with zipfile.open(fname) as f:
                    outfile.write(f.read())
                
    outfile.close()
    
    return os.path.join(datadir,'consolidatedCharacters.txt')

dirpath = os.path.join(os.getcwd(),'datafiles')
outfilepath = BuildConsolidatedFile(dirpath)

