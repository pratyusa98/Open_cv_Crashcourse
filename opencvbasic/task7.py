#different technique
#1. ColorFull Image
#2. Gray scale
#3. Equalization
#4. CLAHE (Contrast Limited Adaptive Histogram Equalization)

import numpy as np
import cv2
from matplotlib import pyplot as plt
#with color image--------------------

img = cv2.imread("resources/thor.jpg")
img = cv2.resize(img,(500,650))
b, g, r = cv2.split(img)

cv2.imshow("img", img)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

#Plotting different channel with hist
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.title("ColorFull Image")
plt.show()

##########################################################

# #Gray scale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title("Gray Image")
plt.show()

###################################################3

#Equalization
#Histogram equalization is good when  of the image is confined to a particular region.
#It accept gray scale image
equ = cv2.equalizeHist(img_gray)
res = np.hstack((img_gray,equ)) #stacking images side-by-side
cv2.imshow("equ",res)
hist1 = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()

########################################################

#CLAHE (Contrast Limited Adaptive Histogram Equalization)
# create a CLAHE object (Arguments are optional).
#It is used to enchance image and also handle noise froom image region
#gray scale imge is required
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_gray)
cv2.imshow('clahe',cl1)
hist2 = cv2.calcHist([cl1], [0], None, [256], [0, 256])
plt.plot(hist2)
plt.title("CLAHE")
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()