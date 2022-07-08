import phpcodes as x
import css
from cgitb import text
import os
import cv2
from pytesseract import pytesseract
from pytesseract import Output
import shutil
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
for word in l:
    print(word)
#BASIC HTML CODE
html = """
<!DOCTYPE html>
<html>
<head>
<title>AI CREATED SITE</title>
</head>
<link rel="stylesheet" href="result.css">
<body>
<form action="result.php" method="post">

























































</form>
</body>
</html>
"""
with open('html.txt','w') as f:
    f.write(html)
#AI LOGIC
with open('html.txt','r') as f:
    content = f.read()
# with open('html.txt','w') as f:
     
for i in l:
    with open('html.txt','r') as f:
        content = f.read()
#NAME
    if('NAME' in i or 'Name' in i or 'name' in i or 'username' in i or 'USERNAME' in i or 'Username' in i or 'user' in i or 'User' in i or 'USER' in i):
        print('NAME1')
        with open('html.txt','a') as f:
            # content = f.read()
            text="""<label  class="input">NAME</label>
    <br>
    <br>
    <input type="text" name="NAME" class="inputbox" placeholder="NAME">
    <br>
    <br>"""
            with open('html.txt','w') as f:
                f.write(content[:160]+text+content[160:])
#EMAIL
    elif('EMAIL' in i or 'Email' in i or 'email' in i):
        print('EMAIL1')
        text="""<label   class="input">EMAIL</label>
    <br>
    <br>
    <input type="text" name="EMAIL" class="inputbox" placeholder="EMAIL">
    <br>
    <br>"""
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
#PASSWORD
    elif('PASSWORD' in i or 'Password' in i or 'password' in i):
        print('PASSWORD1')
        text="""<label  class="input">PASSWORD</label>
    <br>
    <br>
    <input type="PASSWORD" name="PASSWORD" class="inputbox" placeholder="PASSWORD">
    <br>
    <br>"""
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
#AGE
    elif('AGE' in i or 'Age' in i or 'age' in i):
        print('AGE1')
        text="""<label  class="input">AGE</label>
    <br>
    <br>
    <input type="text" name="AGE" class="inputbox" placeholder="AGE">
    <br>
    <br>"""
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
#PHONE
    elif('PHONE' in i or 'Phone' in i or 'phone' in i or 'number' in i or 'Number' in i or 'NUMBER' in i or 'mobile' in i or 'Mobile' in i or 'MOBILE' in i):   
        print('PHONE1')
        text="""<label  class="input">PHONE</label>
    <br>
    <br>
    <input type="TEL name="PHONE" class="inputbox" placeholder="PHONE" >
    <br>
    <br>"""
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
#DATE
    elif('date' in i or 'DATE' in i  or 'Date' in i):
        print('DATE1')
        text="""<label  class="input">DATE</label>
    <br>
    <br>
    <input type="DATE" name="DATE" id="DATE"  class="inputbox" placeholder="DATE">
    <br>
    <br>"""
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
#SUBMIT
    elif('SUBMIT' in i or 'Submit' in i or 'submit' in i or 'login' in i or 'Login' in i or 'LOGIN' in i):
        print("SUBMIT1")
        
        text="""
        <br>
        
        <input type="submit" value="{}" class="submit">""".format(i)
        with open('html.txt','w') as f:
            f.write(content[:160]+text+content[160:])
            
#converting txt file to html file
with open('html.txt','r') as f:
    content = f.read()
with open('result.html','w') as f:
    f.write(content)
#changing file directory
import shutil
import os
# path to source directory
src_dir = r'C:\Users\dhanu\Videos\sketch2code\result.html'

# path to destination directory
dest_dir = r'C:\xampp\htdocs\text2code'

# getting all the files in the source directory
shutil.copy(src_dir, dest_dir)
#removing file after copy
#coping html code to HTML CODE
src_dir=r'C:\xampp\htdocs\text2code\result.html'
dest_dir=r'C:\Users\dhanu\Videos\sketch2code\RESULT'
#coping using shutil
shutil.copy(src_dir, dest_dir)
#removing file after copy
# os.remove(r'C:\Users\dhanu\Videos\sketch2code\result.html')
# os.remove(r'C:\Users\dhanu\Videos\sketch2code\php.txt')
# os.remove(r'C:\Users\dhanu\Videos\sketch2code\css.txt')
# os.remove(r'C:\Users\dhanu\Videos\sketch2code\html.txt')
css.csscodes(l)
x.phpcode(l)