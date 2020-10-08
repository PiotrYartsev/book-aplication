import os
from string import digits

import subprocess
import PyPDF2

import textract
for n in os.listdir("/home/piotr/Desktop/Books"):
            if n=="Books to read.docx" or n=="desktop.ini" or n=="INFO.txt":
                pass
            else:
                 for m in os.listdir("/home/piotr/Desktop/Books/{}".format(n)):
                     if m=="Books to read.docx" or m=="desktop.ini":
                         pass
                     else:
                         try:
                             for k in os.listdir("/home/piotr/Desktop/Books/{}/{}".format(n,m)):
                                 if k=="Books to read.docx" or k=="desktop.ini" or k==".gitignore":
                                     pass
                                 else:
                                     if k=="VIDEO" or k=="AUDIO":
                                         pass
                                     else:
                                            #print(k)
                                            #text = textract.process("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k), encoding='utf8', errors='ignore')
                                            try:
                                                while True:
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
                                                            break
                                                     except KeyError:
                                                          text = textract.process("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf".format(n,m,k), encoding='utf8', errors='ignore')
                                                          words_from_book=text.decode( encoding="utf8", errors="replace")
                                                          break
                                            
                                                     #text.replace("\n"," ")
    

                                                words_from_book.replace("\n"," ")
                                                words_from_book222=words_from_book
                                                    
                                                    
                                                    
                                                words_from_book222.replace("\n"," ")
                                                words_from_book222.replace("\x0c"," ")
                                                    
                                                    
                                                remove_digits = str.maketrans('', '', digits)
                                                words_from_book222 = words_from_book222.translate(remove_digits)
                                                    
                                                words_from_book222=str(words_from_book222)
                                                    
                                                f = open('/home/piotr/Desktop/book_application/tag-generator/data/test','w')
                                                f.write(words_from_book222)
                                                f.close()
                                                    
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
#                                                            print("""
#                                                                  {} is too short""".format(p))
                                                            li.remove(p)
                                                        if  len(p)>25:
#                                                             print("""
#                                                                   {} is too long""".format(p))
                                                             li.remove(p)
#                                                print(li)
#                                                print("""
#                                                          
#                                                          """)
                                                
                                                if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                                                        os.remove("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k))
    
                                                f = open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),'w')
                                                if m=="ALL":
                                                      f.write("{},None,{}".format(n,k))  
                                                else:
                                                    f.write("{},{},{}".format(n,m,k))
                                                    
                                                for stuff in li:
                                                    f.write(",{}".format(stuff))
                                                f.close()
                                                
                                            except UnicodeDecodeError:
                                                print("""
                          
/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdf  decode error""".format(n,m,k))
                                                if os.path.exists("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k)):
                                                        os.remove("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k))
    
                                                f = open("/home/piotr/Desktop/Books/{}/{}/{}/TAGS/TAGS.txt".format(n,m,k),'w')
                                                if m=="ALL":
                                                      f.write("{},None,{}".format(n,k))  
                                                else:
                                                    f.write("{},{},{}".format(n,m,k))
                                                f.close()
                                                pass
                                            
                         except FileNotFoundError:
                                print("/home/piotr/Desktop/Books/{}/{}/{}/PDF/PDF.pdffile not found".format(n,m,k))