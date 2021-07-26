#I ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.

import cv2
import numpy as np

#read image
img = cv2.imread("resources/cards.jpg")
img = cv2.resize(img,(600,600))

#(271,59) (387,163)
roi = img[59:163,271:387]


cv2.imshow("original",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()