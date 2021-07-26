#Detect circle on webcam By Houghcircle

import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _,img = cap.read()
    img2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    #parameters---(img,circle_method,dp,mindist,parm1,parm2[p1<p2],)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 550,
                              param1=50, param2=30, minRadius=0,
                              maxRadius=0)
    if circles is not None:
        data = np.uint16(np.around(circles))
        for (x, y ,r) in data[0, :]:
            cv2.circle(img2, (x, y), r, (50, 10, 50), 3) #outer circle
            cv2.circle(img2, (x, y), 2, (0, 255, 100), -1) #center
    cv2.imshow("res",img2)
    if cv2.waitKey(27) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()