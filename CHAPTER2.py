import cv2
import numpy as np

img=cv2.imread('222.png')#normal
kernel=np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,200)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=5)
imgEroded=cv2.erode(imgDilation,kernel,iterations=2)

cv2.imshow("blur",imgBlur) #blur
cv2.imshow("gray",imgGray) #gray
cv2.imshow("canny",imgCanny) #canny
cv2.imshow("dilation",imgDilation) #canny
cv2.imshow("erosion",imgEroded) #canny

cv2.waitKey(0)
