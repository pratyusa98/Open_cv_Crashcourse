#draw shapes on images

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

#img[:]= 255,0,0 #blue #whole img color
#img[200:300,100:300]= 255,0,0 #blue

#create lines
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#reactangle
cv2.rectangle(img,(20,30),(250,350),(0,0,255),2)
#circle
cv2.circle(img,(400,50),30,(255,255,0),5)

#put text
cv2.putText(img,"Hello OpenCV",(250,200),cv2.FONT_HERSHEY_TRIPLEX,1,(0,150,0),3)


cv2.imshow("img",img)

cv2.waitKey(0)