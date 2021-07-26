
import cv2
import numpy as np

img = cv2.imread("resources/lion.jpg")

img = cv2.resize(img,(900,500))

px = img[400,580]
print("the pixel of that co-ordinates==",px) #we get the pixel value [b,g,r]

#Now try to find selected channel value from cordinate
#We know we have three channel -   0,1,2 - blue,green,red
# accessing only blue pixel
blue = img[400,580,0]
print("the pixel having blue color==",blue)

cv2.imshow("Original",img)
cv2.waitKey()
cv2.destroyAllWindows()