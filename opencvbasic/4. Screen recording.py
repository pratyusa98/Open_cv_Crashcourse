#screen recorder
import cv2
import pyautogui as p
import cv2 as c
import numpy as np

#create resultion
rs = p.size()

fn = input("Enter Path Name: ")
fps = 30.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module
c.namedWindow("LIve_Recording",c.WINDOW_NORMAL)
#Resize the window
c.resizeWindow("Live",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("LIve_Recording", f)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

output.release()
c.destroyAllWindows()
