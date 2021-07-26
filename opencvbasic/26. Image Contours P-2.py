# Contour and its functions
# Moment
# Approximation
# Convexhull

import cv2
import numpy as np

img = cv2.imread("resources/shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# img = cv2.drawContours(img,cnts,-1,(176,80,15),4)

# moment get center if shape

for c in cnts:
    # compute the center of the contour
    # an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
        # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (0,0,0), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()