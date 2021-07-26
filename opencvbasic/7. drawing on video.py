import cv2
import datetime

cap = cv2.VideoCapture("resources/10 Sec Road Trip.mp4")

# 3 width #4 height predefine
print("Width====",cap.get(3))
print("Height===",cap.get(4))


while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(1080,480))
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    text = ' Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
    frame = cv2.putText(frame, text, (20, 20), font, 1,(0, 155, 255), 1, cv2.LINE_AA)

    frame = cv2.rectangle(frame, (84, 180), (320, 128), (128, 0, 255), 8)

    cv2.imshow("original",frame)


    k = cv2.waitKey(30)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
