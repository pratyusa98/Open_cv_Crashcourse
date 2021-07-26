import cv2

import cv2


vidcap = cv2.VideoCapture("resources/10 Sec Road Trip.mp4")
ret,image = vidcap.read()#READ THE VIDEO

count = 0

while True:

    if ret == True:
      cv2.imwrite("frames\\imgN%d.jpg" % count, image)     # save frame as JPEG file
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
      ret,image = vidcap.read()
      cv2.imshow("res",image)
      print ('Read a new frame:',count ,ret)
      count += 1
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
          cv2.destroyAllWindows()
    else:
      break

vidcap.release()
cv2.destroyAllWindows()

