#-------------Morphological Transformations-----------------------

#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images(gray scale image).
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two basic Morphological Transformations are 1) - Erosion and 2) - Dilation

import cv2
import numpy as np


img = cv2.imread('resources/col_balls.jpg',0)

#Erosion---
#it erodes away the boundaries of foreground object
#kernal slides through all the image and all the pixel
#from the original image conside 1 only if kernal's pixel is 1

_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)# 5x5 kernel with full of ones.
erosion = cv2.erode(mask,kernel) #optional parameters   iterations = 2


#Dilation --
#It is just opposite of erosion.
#Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’
#So it inc. the white region in the image or size of foreground object in.
#Normally, in cases like noise removal, erosion is followed by dilation.
#Because, erosion removes white noises, but it also shrinks our object.

kernel = np.ones((1,1),np.uint8)# 5x5 kernel with full of ones.
dilation  = cv2.dilate(mask,kernel) #iterations = 2 (optional parameters) iterations = 2




cv2.imshow("mask==",mask)
cv2.imshow("img",img)
# cv2.imshow("ker=",kernel)
cv2.imshow("erosion==",erosion)
cv2.imshow("dilate==",dilation)



cv2.waitKey(0)
cv2.destroyAllWindows()

