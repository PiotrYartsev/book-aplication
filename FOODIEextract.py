# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileReader
from PIL import Image
L=[]
def FOODIEextract():
    for n in os.listdir("/home/piotr/Desktop/Books"):
            if n=="Food":
                 for m in os.listdir("/home/piotr/Desktop/Books/{}".format(n)):
                     if m=="Books to read.docx" or m=="desktop.ini":
                         pass
                     else:
        
                         for k in os.listdir("/home/piotr/Desktop/Books/{}/{}".format(n,m)):
                             if k=="Books to read.docx" or k=="desktop.ini" or k==".gitignore":
                                 pass
                             else:
                                 if k=="athymeandplace":
                                    pdfFileObj = open("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k),'rb')
                                    # Creating a pdf reader object
                                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                                    # Getting number of pages in pdf file
                                    pages = pdfReader.numPages
                                    # Loop for reading all the Pages
                                    for i in range(pages):
                                            # Creating a page object
                                            pageObj = pdfReader.getPage(i)

                                            #print("Page No: ",i)

                                            text = pageObj.extractText().split("\n")
                         
                                            for l in range(len(text)):
                                                if ".Ingredients" in text[l]:
                                                    g=l+1
                                                    if g==len(text):
                                                        pass
                                                    else:
                                                        while not "Directions" in text[g]:
                                                            L.append([text[g],i+1])
                                                            print(text[g])
                                                            g+=1
                                                        
                                                    L.append([text[g+1],i+2])

                                    # closing the pdf file object
                                    pdfFileObj.close()
                                                                    
FOODIEextract()