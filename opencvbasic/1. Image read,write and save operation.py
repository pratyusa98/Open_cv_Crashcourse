import cv2
print("package imported")

img = cv2.imread("resources/avengers.jpg",1) #1 color 0: gray -1:unchanged increase saturation
img2 = cv2.imread("resources/avengers.jpg",0) #1 color 0: gray -1:unchanged increase saturation
img3 = cv2.imread("resources/avengers.jpg",-1) #1 color 0: gray -1:unchanged increase saturation


## resize the image
img = cv2.resize(img,(1000,400)) # width , height
img2 = cv2.resize(img2,(1000,400)) # width , height
img3 = cv2.resize(img3,(1000,400)) # width , height
print(img)

#display image
cv2.imshow("Original",img)
cv2.imshow("Original_gray",img2)
cv2.imshow("Original_unchanged",img3)


cv2.waitKey(0)
cv2.destroyAllWindows()