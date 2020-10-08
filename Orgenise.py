# -*- coding: utf-8 -*-
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


def Orgenise():
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)
    for o in tqdm(range(len(TAGS.files_system)), ascii=True, desc="Orgenise"):
        n=TAGS.files_system[o][0]
        m=TAGS.files_system[o][1]
        k=TAGS.files_system[o][2]
    
        if k=="VIDEO" or k=="AUDIO":
             pass
        else:
             for a in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k)):
                 if a=="Books to read.docx" or a=="desktop.ini" or a==".gitignore" or a=="INFO.txt":
                     pass
                 elif a=="PDF":

                      for l in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a)):  
                          if l=="Books to read.docx" or l=="desktop.ini" or l==".gitignore" or l=="INFO.txt":
                                  pass
                          elif os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/PDF.pdf".format(n,m,k,a)):
                              pass
                              
                          else:
                              os.rename("/home/piotr/Desktop/Books/{}/{}/{}/{}/{}".format(n,m,k,a,l),"/home/piotr/Desktop/Books/{}/{}/{}/{}/PDF.pdf".format(n,m,k,a))
                 elif a=="IMAGE":

                      for l in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a)):  
                          if l=="Books to read.docx" or l=="desktop.ini" or l==".gitignore" or l=="INFO.txt":
                                  pass
                          elif os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a)):
                              pass
                              
                          else:
                              os.rename("/home/piotr/Desktop/Books/{}/{}/{}/{}/{}".format(n,m,k,a,l),"/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a))
                 if a=="EXTRA":
                    pass
                 else:
                    if ".pdf" in a:

                         if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,k)):
                             os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,k))
                             shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,k))
                         else:
                             if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF/{}".format(n,m,k,a)):
                                 pass
                             else:
                                 shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,k))
                    elif a.endswith(".PNG")  or a.endswith(".jpg") or a.endswith(".jpeg"):

                         if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a)):
                             os.replace("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a),"/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a))
    
                         if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(n,m,k)):
                             os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(n,m,k))
                             shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(n,m,k))
                         else:
                             if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE/{}".format(n,m,k,a)):
                                 pass
                             else:
                                 shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/IMAGE".format(n,m,k))
                                 
                         if a=="PDF" or a=="IMAGE" or a=="EXTRA" or a=="TAGS":
                             pass
                         else:
                             print("{} moved to EXTRA".format(a))
                             
                             if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k)):
                                 os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k))
                                 shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k))
                             else:
                                  if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA/{}".format(n,m,k,a)):
                                      print("""
                                           {} went wrong 
                                           """.format(a))
                                  else:
                                     shutil.move("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a), "/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k))
                     
                        
                    