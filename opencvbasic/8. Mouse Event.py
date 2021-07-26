

import cv2
import numpy as np

def draw(event,x,y,flags,param):
    print("X==",x)
    print("Y==",y)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 63, (214, 255, 0), -5)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x,y), (x+100,y+75), (128, 0, 255), 8)

cv2.namedWindow(winname="res")

img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()