from cgitb import text
import os
from docx import Document
import cv2
from pytesseract import pytesseract
from pytesseract import Output
import shutil
import re
#creating dialog for image
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
print(file_path)
l=[]
pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread(file_path)
#converting image to text in dictionary
image_data=pytesseract.image_to_data(img,output_type=Output.DICT)
print(image_data['text'])
#appending text to list and removing ' '
for i in range(len(image_data['text'])):
    if(image_data['text'][i]!=''):
        l.append(image_data['text'][i])
#REMOVING DUPLICATES
l = list(dict.fromkeys(l))
#REVERSING THE LIST
l=l[::-1]
#printing image text in list
import code
import re
html=['name','address','phone','email','website','description','keywords','username','date','time','submit',]
    
for i in range(len(html)):
    if(re.match(l[i],html[i],re.IGNORECASE)):
        print(i)
        code="""   <input type="%s" name="%s" placeholder="%s"> """%(i,i,i)
        print(code)
        for j in range(len(html)):
            if(re.match(l[j],j,re.IGNORECASE)):
                html.remove(l[j])
                
        
print(i)