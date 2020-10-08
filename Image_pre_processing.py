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
import warnings
from tqdm import tqdm
from Orgenise import *
from settings import *
from Image_pre_processing import *
import TAGS
from INFO import *
from __main__ import *


def Image_pre_processing():
     books_could_not_convert=[]
     for o in tqdm(range(len(TAGS.files_system)), ascii=True, desc="Image pre processing"):
         n=TAGS.files_system[o][0]
         m=TAGS.files_system[o][1]
         k=TAGS.files_system[o][2]
         if k=="VIDEO" or k=="AUDIO":
             pass
         else:
             for a in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k)):
                 if a=="Books to read.docx" or a=="desktop.ini" or a==".gitignore":
                     pass

                 elif a=="IMAGE":
                      if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a)):
                                  os.remove("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a)) 
                      if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.png".format(n,m,k,a)):
                                  os.remove("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.png".format(n,m,k,a)) 
                      if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a)):
                                  os.remove("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a))                    
                      if len(os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a))) == 0:
                          #print("no image, made from pdf")
                          try:                                             
                              pages = convert_from_path(("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)), 500, single_file=True) 
                              pages[0].save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a), 'JPEG')
                              d = Image.open("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a))
                              d_rgb = d.convert('RGB')      
                              d_rgb.save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a),quality=5, optimize=True, progressive=True)
                          except:
                              books_could_not_convert.append("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k))
                      else:
                          for l in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a)):
                              if l=="Books to read.docx" or l=="desktop.ini" or l==".gitignore" or l=="IMAGE_RE.jpg":
                                      pass
                              else:

                                  image = Image.open("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.jpg".format(n,m,k,a))
                                  
                                  image_rgb = image.convert('RGB')

                                      
                                  image_rgb.save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a),quality=5, optimize=True)
     if len(books_could_not_convert):                  
         print("\n {} \n".format(books_could_not_convert))