
import cv2
import numpy as np

img = cv2.imread("resources/pikachu.jpg")
img = cv2.resize(img,(600,400))

print("shape==",img.shape) #returns a tuple of number of (rows, columns, channels)
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("datatype==",img.dtype) #returns Image datatype is obtained
print("Imagetype==",type(img))

# Now try to split an image
#split  -  return 3 channel of ur image which is blue,green,red
# print(cv2.split(img))
b,g,r = cv2.split(img)

# cv2.imshow("blue",b)
# cv2.imshow("green",g)
# cv2.imshow("red",r)

#Now if you want to mix the the channels then use merge

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

mr2 = cv2.merge((b,g,r))
cv2.imshow("bgr",mr2)




cv2.imshow("Original",img)
cv2.waitKey()
cv2.destroyAllWindows()