import numpy as np
import cv2

img=cv2.imread('geometric.jpg')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thrash=cv2.threshold(imgGray,130,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for countor in contours:
    approx=cv2.approxPolyDP(countor,0.01*cv2.arcLength(countor,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio>=0.95 and aspectratio<=1.05:
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif(len(approx)==5):
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,'circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
cv2.imshow('geometric',img)
cv2.waitKey(0)
cv2.destroyAllWindows()