import tkinter as tk
from tkinter import filedialog
from pytesseract import pytesseract
import cv2
from pytesseract import Output
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
#printing the list
print(l)