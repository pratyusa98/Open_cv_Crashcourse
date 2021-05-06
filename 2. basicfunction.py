import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('resources/lena.png')

#convert into grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blurr image
imgBlur = cv2.GaussianBlur(img,(7,7),0)
#edge detector
imgCanny = cv2.Canny(img,150,200)
#Dialation
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
#erode
imgErode = cv2.erode(imgDialation,kernel,iterations=1)


# cv2.imshow('GrayImg',imgGray)
# cv2.imshow('imgBlur',imgBlur)
cv2.imshow('imgCanny ',imgCanny)
cv2.imshow('imgDialation ',imgDialation)
cv2.imshow('imgErode ',imgErode)
cv2.waitKey(0)