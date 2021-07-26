import cv2


img1 = cv2.imread("resources/roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("resources/bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))

def blend(x):
    pass


cv2.namedWindow('win')
cv2.createTrackbar('alpha','win',1,100,blend)

while True:
    alpha = cv2.getTrackbarPos('alpha', 'win')
    na = float(alpha / 100)
    result = cv2.addWeighted(img1,1-na, img2, na, 0)
    cv2.putText(result, str(alpha), (20, 50), cv2.FONT_ITALIC,
               2, (0, 125, 255), 2)
    cv2.imshow('result', result)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()