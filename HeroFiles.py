# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:18:47 2019

@author: Dave
"""


from zipfile import ZipFile
import glob
import os
import re

def BuildConsolidatedFile(datadir):
    matchstring = '^[^a-zA-Z]*(?P<MTCH>[a-zA-Z]+)'

    rg = re.compile(matchstring)

    HEoutfile = open(os.path.join(datadir,'HE_Characters.txt'), 'wb')
    SHEoutfile = open(os.path.join(datadir,'SHE_Characters.txt'), 'wb')
    for filepath in glob.glob(os.path.join(datadir,'*.zip')):
        #open the zip files to read the files
        
        zipfile = ZipFile(filepath)
        
        for fname in zipfile.infolist():
            if not fname.is_dir() and not fname.filename.startswith('__MACOSX'):            
                with zipfile.open(fname) as f:
                    try: 
                        l = str(f.readline().decode("ascii"))
                        m = rg.match(l)
                        f.seek(0)
                        if m.group('MTCH').lower() == 'he':
                            HEoutfile.write(f.read())
                        if m.group('MTCH').lower() == 'she':
                            SHEoutfile.write(f.read())
                    except:
                        pass
                
    HEoutfile.close()
    SHEoutfile.close()
    
    return {"hefile":os.path.join(datadir,'HE_Characters.txt'),
            "shefile":os.path.join(datadir,'SHE_Characters.txt')}


