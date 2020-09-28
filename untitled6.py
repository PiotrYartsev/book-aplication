# -*- coding: utf-8 -*-

import os
from PIL import Image
from pdf2image import convert_from_path



f= open("C:\\Users\\PiotrYartsev\\Desktop\\Books\\INFO.txt","w")
f.truncate()
f.write("Name, pdf directory, image directory, degraded image directory, tags, extr directory if not empty \n")
for n in os.listdir("C:\\Users\\PiotrYartsev\\Desktop\\Books"):
        if n=="Books to read.docx" or n=="desktop.ini" or n=="INFO.txt":
            pass
        else:
    
             for m in os.listdir("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}".format(n)):
                 if m=="Books to read.docx" or m=="desktop.ini":
                     pass
                 else:
    
                     for k in os.listdir("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}".format(n,m)):
                         if k=="Books to read.docx" or k=="desktop.ini" or k==".gitignore":
                             pass
                         else:
                             if k=="VIDEO" or k=="AUDIO":
                                 pass
                             else:
                                  
                                  if os.path.exists("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\PDF\\PDF.pdf".format(n,m,k)):
                                      a_pdf= "C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\PDF\\PDF.pdf".format(n,m,k)

                                  else:
                                        a_pdf="None"
                                        
                                  if os.path.exists("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\IMAGE\\IMAGE.png".format(n,m,k)):
                                      a_image= "C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\IMAGE\\IMAGE.png".format(n,m,k)

                                  else:
                                        a_image="None"    
                                        
                                  if os.path.exists("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\IMAGE\\IMAGE_RE.jpg".format(n,m,k)):
                                      a_image_re= "C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\IMAGE\\IMAGE_RE.jpg".format(n,m,k)
                                  
                                  else:
                                       a_image_re="None"
                                  
                                  if os.path.exists("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\TAGS\\TAGS.txt".format(n,m,k)):
                                        tags= open("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\TAGS\\TAGS.txt".format(n,m,k),"r")
                                        a_tags="({})".format(tags.readline())
                                        
                                  else:
                                        a_tags="None"
                                  
                                  if os.path.exists("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\EXTRA".format(n,m,k)):
                                       if len(os.listdir("C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\EXTRA".format(n,m,k)))==0:
                                            a_extra="None"
                                       else:
                                            a_extra="C:\\Users\\PiotrYartsev\\Desktop\\Books\\{}\\{}\\{}\\EXTRA".format(n,m,k)
                                        
                                  else:
                                        a_extra="None"
                                        
                                        
                                  f.write("{},{},{},{},{},{}\n".format(k,a_pdf,a_image,a_image_re, a_tags,a_extra))  

f.close() 