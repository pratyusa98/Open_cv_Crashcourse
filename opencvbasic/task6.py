#building trackbar with canny edge

import cv2

img = cv2.imread("resources/building.jpg")
img = cv2.resize(img, (600, 700))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def nothing(x):
    pass


cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold1", "Canny", 0, 255, nothing)
cv2.createTrackbar("Threshold2", "Canny", 0, 255, nothing)

while True:
    a = cv2.getTrackbarPos('Threshold1', 'Canny')
    b = cv2.getTrackbarPos('Threshold2', 'Canny')

    res = cv2.Canny(img_gray, a, b)

    cv2.imshow("Original", img)
    cv2.imshow("Canny", res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()