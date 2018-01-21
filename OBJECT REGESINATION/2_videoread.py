import cv2
import numpy as np

cap =cv2.VideoCapture(0) # 0 defaul web cam 1 second 2 third ...
savevideo_fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('OUTPUT.MP4',savevideo_fourcc,20.0 ,(640,480))
while True:
    ret,frame=cap.read() # ret will wet true or false   and frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    cv2.imshow( "videoframe" ,frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
