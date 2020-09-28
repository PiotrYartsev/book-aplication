# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileReader
from PIL import Image

def FOODIE():
    for n in os.listdir("/home/piotr/Desktop/Books"):
            if n=="Food":
                 print("yeah")
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
                                           pdf_reader = PdfFileReader("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k))
                                           if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/FOOD".format(n,m,k)):
                                                            os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/FOOD".format(n,m,k))
                                                            
                                             
                     
                                           f= open("/home/piotr/Desktop/Books/{}/{}/{}/FOOD/FOOD.txt".format(n,m,k),"w+")
                                           f.write("where: {}\n".format("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)))
                                           f.write("Name: {}\n\n".format(k))
                                           for page in range(pdf_reader.getNumPages()):
                                               f.write("\n\n")
                                               f.write("Recepie name: \n\n")
                                               f.write("Recepie page: \n\n")
                                               f.write("Recepie ingrediants: \n\n")
                                               f.write("Recepie text: \n\n")
                                               f.write("Recepie calories: \n\n")
                                               
                                           f.close()
                                           
