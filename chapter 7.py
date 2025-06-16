import cv2

def empty():
    pass


path='222.png'
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,240)
cv2.createTrackbar("Hue Min","trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","trackbars",170,179,empty)
cv2.createTrackbar("Sat Min","trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","trackbars",255,255,empty)
cv2.createTrackbar("Val Min","trackbars",0,255,empty)
cv2.createTrackbar("Val Max","trackbars",255,255,empty)



while True:
    img=cv2.imread(path)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","trackbars")
    h_max=cv2.getTrackbarPos("Hue Max","trackbars")
    s_min=cv2.getTrackbarPos("Sat Min","trackbars")
    s_max=cv2.getTrackbarPos("Sat Max","trackbars")
    v_min=cv2.getTrackbarPos("Val Min","trackbars")
    v_max=cv2.getTrackbarPos("Val Max","trackbars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.waitKey(1)