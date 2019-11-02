# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:18:47 2019

@author: Dave
"""


from zipfile import ZipFile
import glob
import os
import re
import string

def BuildConsolidatedFile(datadir):
    matchstring = '^[^a-zA-Z]*(?P<MTCH>[a-zA-Z]+)'

    rg = re.compile(matchstring)
    removepunc = string.punctuation[:6] + string.punctuation[7:12] + string.punctuation[13:]
    HEoutfile = open(os.path.join(datadir,'HE_Characters.txt'), 'w')
    SHEoutfile = open(os.path.join(datadir,'SHE_Characters.txt'), 'w')
    for filepath in glob.glob(os.path.join(datadir,'*.zip')):
        #open the zip files to read the files
        
        zipfile = ZipFile(filepath)
        
        for fname in zipfile.infolist():
            if not fname.is_dir() and not fname.filename.startswith('__MACOSX'):            
                with zipfile.open(fname) as f:
                    try: 
                        for i, l in enumerate(f):
                            
                            s = l.decode('ascii').strip()
                            m = rg.match(s)
                            
                            outstring = s[m.start('MTCH'):].lower().translate(str.maketrans('','',removepunc))
                            #check if a match exists
                            if m.group('MTCH').lower() == 'he':
                                #parse out the string to start with the part found
                                HEoutfile.write(outstring)
                                HEoutfile.write("\n")
                            if m.group('MTCH').lower() == 'she':
                                #parse out the string to start with the part found                                
                                SHEoutfile.write(outstring)
                                SHEoutfile.write("\n")
                    except:
                        pass
                
    HEoutfile.close()
    SHEoutfile.close()
    
    return {"hefile":os.path.join(datadir,'HE_Characters.txt'),
            "shefile":os.path.join(datadir,'SHE_Characters.txt')}


