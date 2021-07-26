#I ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.

import cv2
import numpy as np

#read image
img = cv2.imread("resources/roi_opr.jpg")
img = cv2.resize(img,(600,600))

#ROI (231,41) (342,161)

#pass [(y1:y2),(x1,x2)]
#y = 161-41 =120 , x= 342-231 = 111
roi = img[41:161,231:342]

#now passing data into img
img[41:161,343:454] = roi
img[41:161,455:566] = roi

img[41:161,119:230] = roi
img[41:161,8:119] = roi


cv2.imshow("original",img)
cv2.imwrite("img.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()