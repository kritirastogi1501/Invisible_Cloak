import cv2
import numpy as np

img=cv2.imread("222.png")
print(img.shape) #size of image
imgResize=cv2.resize(img,(500,800)) #resizing
print(imgResize.shape)

imgCropped=img[0:400,200:800] #cropped

cv2.imshow('colour',img)
cv2.imshow('resize',imgResize)
cv2.imshow('cropped ',imgCropped)

cv2.waitKey(0)
