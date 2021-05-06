## Resizing And Cropping

import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)

#resize
imgResize = cv2.resize(img,(224,224))
print('after_resize',imgResize.shape)

#crop
imgCrop = img[0:200,200:500]

cv2.imshow('Myimg',img)
cv2.imshow('imgResize ',imgResize )
cv2.imshow("Image Cropped",imgCrop)
cv2.waitKey(0)