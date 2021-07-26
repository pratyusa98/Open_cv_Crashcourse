#read video from webcm and save

import cv2
import pafy

url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url)
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(cv2.CAP_DSHOW)
cap.open(data.url)


while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(500,300))
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
