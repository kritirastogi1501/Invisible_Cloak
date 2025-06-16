import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8) #coloured
#print(img.shape)
#img[200:400]=255,0,0  #colour a specific portion other than black

#to draw line=
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(10,255,0),10)

#to draw rectangle=
cv2.rectangle(img,(0,0),(300,450),(0,0,255),5)
#cv2.imshow("image",img)

#to fill rectangle
#cv2.rectangle(img,(0,0),(300,450),(0,0,255),cv2.FILLED)

#circle=

cv2.circle(img,(300,300),50,(255,0,0),4,23)

#to put text=
cv2.putText(img,"hello world",(300,400),cv2.FONT_ITALIC,1,(255,255,0),2)

cv2.imshow("image",img)
cv2.waitKey(0)
