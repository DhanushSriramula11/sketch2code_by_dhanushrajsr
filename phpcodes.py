#formal list
import os
import webbrowser
import shutil
import re
p=[]
p=p[::-1]
def phpcode(p):
    count=0
#basic php code
    content="""<?php
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ?>"""
    with open('php.txt','w') as f:
        f.write(content)
    with open('php.txt','r') as f:
        content=f.read()
    #AI PHP
    for i in p:
        with open('php.txt','r') as f:
            content=f.read()
            if(re.match('name',i,re.IGNORECASE)):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
            elif(re.match('email',i,re.IGNORECASE)):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
            elif((re.match('mobile',i,re.IGNORECASE))or(re.match('phone',i,re.IGNORECASE))):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
                    
            elif(re.match('password',i,re.IGNORECASE)):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
            elif(re.match('address',i,re.IGNORECASE)):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
            elif(re.match('age',i,re.IGNORECASE)):
                count=count+1
                with open('php.txt','a') as f:
                    text=""" 
                    $%s = $_POST['%s'];
                    """%(i,i)
                with open('php.txt','w') as f:
                    f.write(content[:10]+text+content[10:])
    if(count==2):
        with open('php.txt','r') as f:
            content=f.read()
        with open('php.txt','a') as f:
            text="""
            $con = mysqli_connect('localhost','root','','test');
            """
        with open('php.txt','w') as f:
            f.write(content[:170]+text+content[170:])
        #writing insertion codes
        p=p[::-1]
        for j in p:
            print("p in php is",j)
            with open('php.txt','r') as f:
                content=f.read()
            if(re.match('name',j,re.IGNORECASE) or re.match('NAME',j,re.IGNORECASE)):
                print("php name....")
                with open('php.txt','a') as f:
                    text="""
                    $qry="insert into login(%s) values('$%s')"; 
                    $run=mysqli_query($con,$qry);
                         """%(j,j)
        
                    with open('php.txt','w') as f:
                        f.write(content[:270]+text+content[270:])
            elif(re.match('password',j,re.IGNORECASE)):
                with open('php.txt','a') as f:
                    text=""" 
                    $qry="insert into login(%s) values('$%s')"; 
                    $run=mysqli_query($con,$qry);
                    
                    """%(j,j)
                    with open('php.txt','w') as f:
                        f.write(content[:570]+text+content[570:])
        #default for data inserted in database or not
        with open('php.txt','a') as f:
            text="""
            
            
            $run=mysqli_query($con,$qry);
            if($run){
                echo "<h1>Data Inserted Successfully</h1>";
            }
            else{
                echo "data not inserted and check the entered data";
            }
            
            
        """
        with open('php.txt','w') as f:
            f.write(content[:770]+text+content[770:])

                    
    print('count value is:',count)
    #coping in to new file
    with open('php.txt','r') as f:
        content=f.read()
    with open('result.php','w') as f:
        f.write(content)
    #coping to htdocs
    src=r'C:\Users\dhanu\Videos\sketch2code\result.php'
    dst=r'C:\xampp\htdocs\text2code'
    shutil.copy(src,dst)
    #coping to RESULT
    src=r'C:\xampp\htdocs\text2code\result.php'
    dst=r'C:\Users\dhanu\Videos\sketch2code\RESULT'
    shutil.copy(src,dst)
    #removing after coping
    os.remove(r'C:\Users\dhanu\Videos\sketch2code\result.php')
    #openning in browser
    url='http://localhost/text2code/result.html'
    webbrowser.open_new_tab(url)
     #removing all txt files
    os.remove(r'C:\Users\dhanu\Videos\sketch2code\php.txt')
    # os.remove(r'C:\Users\dhanu\Videos\sketch2code\css.txt')
    # os.remove(r'C:\Users\dhanu\Videos\sketch2code\html.txt')   