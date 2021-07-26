#read video from webcm and save

import cv2

# camera = "https://192.168.43.1:8080/video"

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.open(camera)

#it is 4 byte code which is use to specify the video codec
#Various codec --
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0) #0 for gray

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    output.write(frame)
    output.write(gray)

    cv2.imshow("video",frame)
    cv2.imshow("videogray", gray)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()
output.release()
cv2.destroyAllWindows()
