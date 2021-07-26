
import cv2
import numpy as np

# Load two images
img1 = cv2.imread("resources/hero1.jpg")
img2 = cv2.imread("resources/strom_breaker.jfif")


img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1 row,column,channel
r,c,ch = img2.shape

#here first(y,x)
roi = img1[0:r,0:c]

#step1 gray convert
#NOw creating gray for img2
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#step2 mask/threshold
#create mask using threshold
_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)

#step3 bitwisenot
#remove bg
mask_inv= cv2.bitwise_not(mask)

#step4 bitwise_and
#put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#step5 bitwise_and
# Take only region of figure from original  image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

#step6 add
# Put logo in ROI and modify the main image
res = cv2.add(img1_bg,img2_fg)

final = img1

final[0:r,0:c]= res   #final output


cv2.imshow("Thor",img1)
cv2.imshow("Strom breaker",img2)
cv2.imshow("roi",roi)
cv2.imshow(" Step -1 gry==",img_gry)
cv2.imshow("Step -2 Mask===",mask)
cv2.imshow("Step -3 Mask_inv",mask_inv)
cv2.imshow("Step -4 Mask_bg",img1_bg)
cv2.imshow("Step -5 Mask fg",img2_fg)
cv2.imshow("Step -6 -Res",res)
cv2.imshow("Step 7== FInal",final)



cv2.waitKey(0)
cv2.destroyAllWindows()