#HSV -  Hue saturation value
#Hsv is use to separate image information on the basis of color luminous or intensity.
#We use Hsv where we perform operation on the basis of color.
#HSV related to hexaon color model
# H - hue - use to select color from 360 portion
#staturation is amount of color  which is selected in hue.(color shades)
#V  -  value which is brightness of the color.

# Static
# import cv2
# import numpy as np
#
# img = cv2.imread("resources/color_balls.jpg")
#
# while True:
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     l_v = np.array([110,50,50])
#     u_v = np.array([130,235,225])
#
#     mask = cv2.inRange(imgHSV, l_v, u_v)
#     res = cv2.bitwise_and(img,img, mask=mask)
#
#
#     cv2.imshow("original", img)
#     cv2.imshow("mask", mask)
#     cv2.imshow("res", res)
#     k = cv2.waitKey(0)
#     if k == ord('q'):
#         break
#
# cv2.destroyAllWindows()

# dynamic

import cv2
import numpy as np
from stackimg import stackImages


def empty(a):
    pass


# img = cv2.imread("resources/color_balls.jpg")
cap = cv2.VideoCapture(0)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    _,img = cap.read()
    img = cv2.resize(img,(600,400))

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.putText(img, "Original", (20, 50), cv2.FONT_ITALIC,
               2, (0, 125, 255), 2)

    cv2.putText(imgHSV, "imgHSV", (20, 50), cv2.FONT_ITALIC,
                2, (0, 125, 255), 2)

    cv2.putText(mask, "mask", (20, 50), cv2.FONT_ITALIC,
                2, (0, 125, 255), 2)

    cv2.putText(imgResult, "imgResult", (20, 50), cv2.FONT_ITALIC,
                2, (0, 125, 255), 2)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
