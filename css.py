from cgitb import text
import re
import shutil
import random
import os
bg=['#b6c199','#c8b7a6','#7d94b5','#c29591','#c7ddcc','#abd699','#b999be','#f6ebf4','#E8CEBF','#9DC88D']
#colors
#fonts
#

f=open('css.txt','w')
p=[]
def csscodes(p):
    #basic css background
    content="""
        body{
            background-color: %s;
        }
        """%(random.choice(bg))
    with open('css.txt','w') as f:
        f.write(content)
    with open('css.txt','r') as f:
        content=f.read()
    for i in p:
        with open('css.txt','r') as f:
            content=f.read()
        if(re.match('name',i,re.IGNORECASE)):
            with open('css.txt','a') as f:
                text=""" 
                .input:hover{
                    color: #fff;
                    background-color: #4CAF50;
                    font-size: 20px;
                    transition: ease-in-out 1s;
                    
                }
                .inputbox{
                    border-radius: 8px;
                    transition: ease-in-out 1s;
                }
                """
                with open('css.txt','w') as f:
                    f.write(content[:70]+text+content[70:])
        elif(re.match('submit'or'login',i,re.IGNORECASE)):
            print('css submit')
            with open('css.txt','r') as f:
                text=""" 
                .submit:hover{
                    color: #fff;
                    background-color: #4CAF50;
                    border-radius: 5px;
                    transition: ease-in-out 1s;
                }
                """
        with open('css.txt','w') as f:
            f.write(content[:70]+text+content[70:])
        #coping into new file
    with open('css.txt','r') as f:
        content=f.read()
    with open('result.css','w') as f:
        f.write(content)
    #coping file into htdocs
    src=r'C:\Users\dhanu\Videos\sketch2code\result.css'
    des=r'C:\xampp\htdocs\text2code'
    shutil.copy(src,des)
    #coping to result
    src=r'C:\xampp\htdocs\text2code\result.css'
    dst=r'C:\Users\dhanu\Videos\sketch2code\RESULT'
    shutil.copy(src,dst)
    os.remove(r'C:\Users\dhanu\Videos\sketch2code\result.css')
    # os.remove(r'C:\Users\dhanu\Videos\sketch2code\php.txt')
    # os.remove(r'C:\Users\dhanu\Videos\sketch2code\css.txt')
    # os.remove(r'C:\Users\dhanu\Videos\sketch2code\html.txt')