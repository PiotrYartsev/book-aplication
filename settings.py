#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# settings.py

import shutil
import os
import os
from string import digits
import subprocess
import PyPDF2 
import textract
import warnings
from tqdm import tqdm
from Orgenise import *
from settings import *
from Image_pre_processing import *
import TAGS
import settings
from INFO import *
from __main__ import *

if __name__ == "__main__": 
    parse_all_files()


def init2():
    inputsss=input("All files: Y/N  ?\n\n")
    if inputsss=="Y":
        #print("y")
        parse_all_files()
    elif inputsss=="N":  
        #print("n")
        parse_all_files()
    
        
        
        check_these_books=[]
        for ob in TAGS.files_system:
            if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(ob[0],ob[1],ob[2])) and os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(ob[0],ob[1],ob[2])) and os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(ob[0],ob[1],ob[2])):
                pass
            else:
        
                check_these_books.append("/home/piotr/Desktop/Books/{}/{}/{}".format(ob[0],ob[1],ob[2]))
                
                
        if len(check_these_books)>0:
            print("""\n only some books: {}""".format(len(check_these_books)))
            
        
            TAGS.files_system=None
            parse_some_files(check_these_books)
    else:
        print("\n not a valid input \n")