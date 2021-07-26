#Blending means addition of two images
#if you want to blend two images then both have same size
#Here We use two important functions cv2.add(), cv2.addWeighted()

import cv2

img1 = cv2.imread("resources/roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("resources/bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))

# cv2.imshow("thor==",img1)
# cv2.imshow("bro_thor==",img2)

#simple blending not suitable
result = img2 + img1 #numpy addition in this we get module between value

#recommended to use cv2.add
result1 = cv2.add(img1,img2) #its your saturated oprn which means value to value

#function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)
#weight  = w1+w2 = 1(max)
result2 = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow("result==",result)
cv2.imshow("result1==",result1)
cv2.imshow("result2==",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()