import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('im1.JPG', cv2.IMREAD_GRAYSCALE)
# more parameter for cv2 = IMREAD_COLOR =1 ; IMREAD_UNCHANGED=-1

cv2.imshow('image',img) # 'image' header of the window
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('newimg.png',img) #save img
##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.plot([50,100],[80,100], 'c', linewidth=5)
##plt.show()

