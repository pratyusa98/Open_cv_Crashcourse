#merge all merphological ransform

import cv2
import numpy as np

img = cv2.imread('resources/girl.jpg',0)
img = cv2.resize(img,(300,300))
_,mask= cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)#2X2 kernel with full of ones.

#all morhological opr
e = cv2.erode(mask,kernel)
d = cv2.dilate(mask,kernel)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
blackhat = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)


#display all the result
titles = ['image', 'mask', 'erosion', 'dilation', 'opening', 'closing',
          'tophat', 'gradient',"blackhat"]
images = [img,mask,e,d,o,c,tophat,gradient,blackhat]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()