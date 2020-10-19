# -*- coding: utf-8 -*-
#! /bin/python3
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
from string import digits
import subprocess
import PyPDF2 
import textract
import warnings
from tqdm import tqdm
warnings.filterwarnings("ignore")




def parse_all_files():
    global files_system
    files_system=[] 
    for categories in os.listdir("/home/piotr/Desktop/Books"):
            if categories=="Books to read.docx" or categories=="desktop.ini" or categories=="INFO.txt":
                pass
            else:
                for packages in os.listdir("/home/piotr/Desktop/Books/{}".format(categories)):
                    if packages=="Books to read.docx" or packages=="desktop.ini":
                        pass
                    else:
                       try:
                            for books in os.listdir("/home/piotr/Desktop/Books/{}/{}".format(categories,packages)):
                                if books=="Books to read.docx" or books=="desktop.ini" or books==".gitignore" or books=="VIDEO" or books=="AUDIO":
                                    pass
                                else:
                                    if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(categories,packages,books)):
                                        g=[]
                                        g.append(categories)
                                        g.append(packages)
                                        g.append(books)
                                        files_system.append(g)
                                    elif os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}".format(categories,packages,books)): 
                                        g=[]
                                        g.append(categories)
                                        g.append(packages)
                                        g.append(books)
                                        files_system.append(g)
                                        
                       except NotADirectoryError:
                                  print("""
/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf ffile not found""".format(categories,packages,books))


def parse_some_files(path_to_book_folder):
    global files_system
    
    files_system=[]
    for w in path_to_book_folder:



        stuff=str(w)
        #print(stuff)
        stuff=stuff.replace("/home/piotr/Desktop/Books/","")
        #print(stuff)
        list_stuff=stuff.split('/')
        #print(list_stuff)
        files_system.append([list_stuff[0],list_stuff[1],list_stuff[2]])
        

    

    #print(files_system)
                    


             
def Make_tags():
 
    for o in tqdm(range(len(files_system)), ascii=True, desc="Make tags"):
            n=files_system[o][0]
            m=files_system[o][1]
            k=files_system[o][2]
#            print(k)

            try:
                 try:
                    FILE_PATH = "/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k)
                    text=""
                    with open(FILE_PATH, mode='rb') as f:
                        reader = PyPDF2.PdfFileReader(f)
                        if reader.isEncrypted:
                            reader.decrypt('')
                        for page in reader.pages:
                            #print(page.extractText())
                            text=text+str(page.extractText())
                    
                    words_from_book=text#.decode( encoding="utf8", errors="replace")
                    #print(len(words_from_book))
                    
                    
                 except KeyError:
                      text = textract.process("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k), encoding='utf8', errors='ignore')
                      words_from_book=text.decode( encoding="utf8", errors="replace")
                      #print(len(words_from_book))

                      
                      
                  
                 words_from_book.replace("\n"," ")

                 words_from_book.replace("\n"," ")
                 words_from_book.replace("\x0c"," ")
                    
                    
                 remove_digits = str.maketrans('', '', digits)
                 words_from_book = words_from_book.translate(remove_digits)
                    
                 words_from_book=str(words_from_book)
#                 print(len((words_from_book)))
                 if os.path.exists('/home/piotr/Desktop/book_application/tag-generator/data/test'):
                        os.remove('/home/piotr/Desktop/book_application/tag-generator/data/test')
                 f = open('/home/piotr/Desktop/book_application/tag-generator/data/test','w')
                 f.write(words_from_book)
                 f.close()
            
                 
                
            except UnicodeDecodeError:
                print("""
                      
/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf  decode error""".format(n,m,k))
                if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                        os.remove("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k))
                if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k)):
                        os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k))
    
                f = open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),'w')
                if m=="ALL":
                      f.write("{},None,{}".format(n,k))  
                else:
                    f.write("{},{},{}".format(n,m,k))
                f.close()
                break

    
            #print(k)
    
            commands = '''
            cd
            cd /home/piotr/Desktop/book_application/tag-generator/
            python3 tagger.py 30
            '''
    
            process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, err = process.communicate(commands.encode( encoding='utf8', errors="replace"))
                
    
            out2=out.decode(encoding='utf8', errors="replace").replace('The likeky tags for the document are:', '')
            out2=out2.replace("[","")
            out2=out2.replace("]","")
            out2=out2.replace("'","")
            out2=out2.replace(",","")
            out2=out2.replace("\n","")
                
            li = list(out2.split(" ")) 
            for p in li:
                    if len(p)<3:
    #                    print("""
    #                          {} is too short""".format(p))
                        li.remove(p)
                    if  len(p)>25:
    #                     print("""
    #                           {} is too long""".format(p))
                         li.remove(p)
    #        print(li)
    #        print("""
    #                 
    #                  """)
    #        
            
            if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                    os.remove("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k))
            if not os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k)):
                                os.makedirs("/home/piotr/Desktop/Books/{}/{}/{}/TAGS".format(n,m,k))     
    
            f = open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),'w')
            if m=="ALL":
                  f.write("{},None,{}".format(n,k))  
            else:
                f.write("{},{},{}".format(n,m,k))
                
            for stuff in li:
              #  print(stuff)
                f.write(",{}".format(stuff))
            f.close()
                
        
    
