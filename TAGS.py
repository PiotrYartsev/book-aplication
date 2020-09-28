# -*- coding: utf-8 -*-

import os
from PIL import Image
from pdf2image import convert_from_path

def TAGS():
    for n in os.listdir("/home/piotr/Desktop/Books"):
            if n=="Books to read.docx" or n=="desktop.ini" or n=="INFO.txt":
                pass
            else:
        
                 for m in os.listdir("/home/piotr/Desktop/Books/{}".format(n)):
                     if m=="Books to read.docx" or m=="desktop.ini":
                         pass
                     else:
        
                         for k in os.listdir("/home/piotr/Desktop/Books/{}/{}".format(n,m)):
                             if k=="Books to read.docx" or k=="desktop.ini" or k==".gitignore":
                                 pass
                             else:
                                 if k=="VIDEO" or k=="AUDIO":
                                     pass
                                 else:
                                     for a in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k)):
                                         if a=="Books to read.docx" or a=="desktop.ini" or a==".gitignore":
                                             pass
                                         else:
                                              for l in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}".format(n,m,k)):
                                                  if l=="Books to read.docx" or l=="desktop.ini" or l==".gitignore":
                                                      pass
                                                  else:
                                                      if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k)):
                                                            os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k))
                                                      else:
                                                           if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                                                               pass
                                                           else: 
                                                                if not m=="ALL":
                                                                   f= open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),"w+")
                                                                   f.write("{},{},{} ".format(n,m,k))
                                                                   f.close() 
                                                                if m=="ALL":
                                                                   f= open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),"w+")
                                                                   f.write("{},{} ".format(n,k))
                                                                   f.close() 