import cv2
import numpy as np


def cross(x):
    pass


# create a black imgae
img = np.zeros((300, 512, 3), np.uint8)  # empty image
cv2.namedWindow("Color Picker")

# Creating TrackBars For Adjusting Colors
cv2.createTrackbar("R", "Color Picker", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker", 0, 255, cross)

# Now creating logic to handle trackbars
while True:
    cv2.imshow("Color Picker", img)
    k = cv2.waitKey(1)
    if k == ord("q"):  # for exit
        break

    # set current positions of four bars
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")
    img[:] = [r, g, b]

    # print(b,g,r)
cv2.destroyAllWindows()