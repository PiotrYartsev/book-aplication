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
from Image_pre_processing import *
from TAGS import *
from INFO import *
import os
from PIL import Image
from pdf2image import convert_from_path
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


def INFO():
    f= open("/home/piotr/Desktop/Books/INFO.txt","w")
    f.truncate()
    f.write("Name, pdf directory, image directory, degraded image directory, tags, extr directory if not empty \n")
    for o in tqdm(range(len(TAGS.files_system)), ascii=True, desc="INFO"):
         n=TAGS.files_system[o][0]
         m=TAGS.files_system[o][1]
         k=TAGS.files_system[o][2]
         if k=="VIDEO" or k=="AUDIO":
             pass
         else:
              
              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)):
                  a_pdf= "/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)

              else:
                    a_pdf="None"
                    
              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE/IMAGE.png".format(n,m,k)):
                  a_image= "/home/piotr/Desktop/Books/{}/{}/{}/IMAGE/IMAGE.png".format(n,m,k)

              else:
                    a_image="None"    
                    
              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/IMAGE/IMAGE_RE.jpg".format(n,m,k)):
                  a_image_re= "/home/piotr/Desktop/Books/{}/{}/{}/IMAGE/IMAGE_RE.jpg".format(n,m,k)
              
              else:
                   a_image_re="None"
              
              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                    tags= open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),"r")
                    a_tags="({})".format(tags.readline())
                    
              else:
                    a_tags="None"
              
              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k)):
                   if len(os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k)))==0:
                        a_extra="None"
                   else:
                        a_extra="/home/piotr/Desktop/Books/{}/{}/{}/EXTRA".format(n,m,k)
                    
              else:
                    a_extra="None"
                    
                    
              f.write("{},{},{},{},{},{}\n".format(k,a_pdf,a_image,a_image_re, a_tags,a_extra))  
    
    f.close() 