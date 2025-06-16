import cv2
print("imported")
a=int(input("see? 1. image\n2. video\n 3. camera="))
if a==1:
    img=cv2.imread("111.jpeg")
    cv2.imshow("Output",img)
    cv2.waitKey(0)
elif a==2:
    cap=cv2.VideoCapture("resources/3.2 - Tuples part 1.mp4")
    while True:
        success, img=cap.read()
        cv2.imshow("video",img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
else:
    cap=cv2.VideoCapture(0)  #using webcam
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)
    cap.set(1,500)
    while True:
        success, img=cap.read()
        cv2.imshow("video",img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break