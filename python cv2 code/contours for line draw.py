import cv2
import numpy as np
img=cv2.imread("face1.jpg")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imggray=cv2.GaussianBlur(imggray,(9,9),0)
imggray=cv2.Canny(img,127,300)
ret,thresh=cv2.threshold(imggray,127,255,0)
c,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(c))
print(c[0:6])
s=cv2.drawContours(img,c,-1,(0,255,0),4)
cv2.imshow("original",imggray)
cv2.imshow("output",s)
cv2.imshow("orignal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
