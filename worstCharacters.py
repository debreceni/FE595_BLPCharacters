# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:18:47 2019

@author: Dave
"""
import HeroFiles
import os

dirpath = os.path.join(os.getcwd(),'datafiles')
outfilepath = HeroFiles.BuildConsolidatedFile(dirpath)

