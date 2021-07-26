
#How to create a border for an image using opencv

import cv2
import numpy as np


img1 = cv2.imread("resources/lion.jpg")
img1 = cv2.resize(img1,(1000,600))

# copyMakeBorder(img,top,bottom,right,left,bordertype,border_color)
img1 = cv2.copyMakeBorder(img1,10,1,5,50,cv2.BORDER_CONSTANT,value = [255,255,125])

cv2.imshow("res",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()