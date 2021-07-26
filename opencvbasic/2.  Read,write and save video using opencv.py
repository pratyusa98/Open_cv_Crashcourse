import cv2

width = 500
height = 300
cap = cv2.VideoCapture("resources/10 Sec Road Trip.mp4")


while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(width,height))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("original",frame)
    cv2.imshow("Gray", gray)

    k = cv2.waitKey(15)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
