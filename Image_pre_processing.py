# -*- coding: utf-8 -*-

import os
from PIL import Image
from pdf2image import convert_from_path

def Image_pre_processing():
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
    
                                         elif a=="IMAGE":
                                              if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a)):
                                                          os.remove("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a))                    
                                              if len(os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a))) == 0:
                                                  print=("no image, made from pdf")
                                                                                               
                                                  pages = convert_from_path(("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)), 500, single_file=True) 
                                                  pages[0].save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.png".format(n,m,k,a), 'PNG')
                                                  d = Image.open("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.png".format(n,m,k,a))
                                                  d_rgb = d.convert('RGB')      
                                                  d_rgb.save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a),quality=5, optimize=True, progressive=True)
                                               
                                              else:
                                                  for l in os.listdir("/home/piotr/Desktop/Books/{}/{}/{}/{}".format(n,m,k,a)):
                                                      if l=="Books to read.docx" or l=="desktop.ini" or l==".gitignore" or l=="IMAGE_RE.jpg":
                                                              pass
                                                      else:
    
                                                          image = Image.open("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE.png".format(n,m,k,a))
                                                          
                                                          image_rgb = image.convert('RGB')
                
                                                              
                                                          image_rgb.save("/home/piotr/Desktop/Books/{}/{}/{}/{}/IMAGE_RE.jpg".format(n,m,k,a),quality=5, optimize=True)
            
