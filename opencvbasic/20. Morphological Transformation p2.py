#Two more basic Morphological Transformations are
#1) - Opening and 2) - Closing

#-------------Morphological Transformations-----------------------

#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images(gray scale image).
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two basic Morphological Transformations are 1) - Erosion and 2) - Dilation

import cv2
import numpy as np


img = cv2.imread('resources/col_balls.jpg',0)

#Opening --
#Opening is just another name of erosion followed by dilation.
#means first erosion take place then dilation
_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)# 5x5 kernel with full of ones.
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #optional parameters iterations = 2


#closing
#It is opposite of opening
#closing is just another name of dilation followed by erosion.
#means first dilation take place then erosion-

kernel = np.ones((3,3),np.uint8)# 5x5 kernel with full of ones.
closeing= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #optional parameters iterations = 2


TOPHAT = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
GRADIENT = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
BLACKHAT = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)


cv2.imshow("original==",img)
cv2.imshow("mask==",mask)
cv2.imshow("opening==",opening)
cv2.imshow("closing",closeing)
cv2.imshow("TOPHAT",TOPHAT)
cv2.imshow("GRADIENT",GRADIENT)
cv2.imshow("BLACKHAT",BLACKHAT)



cv2.waitKey(0)
cv2.destroyAllWindows()

