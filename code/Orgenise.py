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
        a=k.split(".")[0]

        if k=="VIDEO" or k=="AUDIO":
             pass
        elif ".pdf" in k:
            if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/".format(n,m,a)):
                os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,a))
                if ".pdf" in k:
                      if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a)):
                          os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a))
                      
                      shutil.move("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k), "/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a))
                      os.rename("/home/piotr/Desktop/Books/{}/{}/{}/PDF/{}".format(n,m,a,k),"/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,a))
                elif "." in k:
                      if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a)):
                          os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a))
                      
                      shutil.move("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k), "/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a))
                else:
                      pass
                  
            elif os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/".format(n,m,a)):
                      if ".pdf" in k:
                          if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a)):
                              os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a))
                          
                          shutil.move("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k), "/home/piotr/Desktop/Books/{}/{}/{}/PDF".format(n,m,a))
                          os.rename("/home/piotr/Desktop/Books/{}/{}/{}/PDF/{}".format(n,m,a,k),"/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,a))
                      elif "." in k:
                          if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a)):
                              os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a))
                         
                          shutil.move("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k), "/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,a))
                      else:
                          pass