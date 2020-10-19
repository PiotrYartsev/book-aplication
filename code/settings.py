#! /bin/python3
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
import sys
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
#        for u in TAGS.files_system:
#            print(u)
#            print("\n ")
        for ob in TAGS.files_system:
            if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(ob[0],ob[1],ob[2])) and os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(ob[0],ob[1],ob[2])) and os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(ob[0],ob[1],ob[2])):
                pass
            else:
                check_these_books.append("/home/piotr/Desktop/Books/{}/{}/{}".format(ob[0],ob[1],ob[2]))
#                print("{}/{}/{}".format(ob[0],ob[1],ob[2]))
                
        if len(check_these_books)>0:
            TAGS.files_system=None
            parse_some_files(check_these_books)
            for r in check_these_books:
                print(r)
                print("\n")
            #print(TAGS.files_system)
        else:
            TAGS.files_system=None
            sys.exit("\nNothing new!")
    else:
        print("\n not a valid input \n")
    
    
    
    new_k = []
    for elem in TAGS.files_system:
        if elem not in new_k:
            new_k.append(elem)
    TAGS.files_system = new_k
#    for r in TAGS.files_system:
#                print(r)
#                print("\n")