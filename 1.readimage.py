import cv2

print('Package Imported')
#read image

# img = cv2.imread('resources/lena.png')
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# read video

# cap = cv2.VideoCapture('resources/10 Sec Road Trip.mp4')
#
# while True:
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break

# open webcam

cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #brightness

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

