import cv2
import numpy as np

img = cv2.imread("resources/thor.jpg")
img = cv2.resize(img,(400,600))


# Here line accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.line(img,(0,0),(200,200),(255,0,255),5)

#arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (0,125), (255,255), (255, 0, 125), 10)

#Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (84, 80), (320, 128), (128, 0, 255), 8)

#circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (47, 225), 63, (214, 255, 0), -5)

#ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img,(140,160),(100,50),0,0,360,155,5)


#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'THOR', (20, 500), font, 4, (0, 125, 255), 10,cv2.LINE_AA)

cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()