import cv2
import numpy

img1=cv2.imread('rose.jpg')
img2=cv2.imread('mainlogo.png')

#add=img1+img2
#add=cv2.add(img1,img2) #adding the pixels
#weight=cv2.addWeighted(img1, 0.2 , img2,0.8 ,0) 
rows, cols ,cha= img2.shape
roi =img1[0:rows, 0:cols]


cv2.imshow("image",weight)
cv2.waitKey(0)
cv2.destoryAllWindows()
