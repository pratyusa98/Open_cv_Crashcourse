# Approximation and Convex hull

import cv2

#Find countour area , aprroximation and convex hull
img = cv2.imread("resources/shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

area1 = []
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (0, 0, 0), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # find area of contour
    area = cv2.contourArea(c)
    area1.append(area)


    if area < 10000:
        # contour Approx -  it is use to approx shape with less number of vertices
        epsilon = 0.01 * cv2.arcLength(c, True)  # arc length take contour and return its perimeter
        data = cv2.approxPolyDP(c, epsilon, True)
        # Convexhull is used to provide proper contours convexity.

        hull = cv2.convexHull(data)

        x, y, w, h = cv2.boundingRect(hull)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (125, 10, 20), 5)

print("Area",area1)

cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()