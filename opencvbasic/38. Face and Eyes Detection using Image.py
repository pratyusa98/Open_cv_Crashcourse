
# Face Detection using haarcascade file
import cv2

face=cv2.CascadeClassifier("resources/haarcascades/haarcascade_frontalface_default.xml") # for detecting face
eye = cv2.CascadeClassifier('resources/haarcascades/haarcascade_eye.xml')

image =cv2.imread("resources/a.jpg")
gray= cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)  # convert into gray

# parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray ,1.3 ,2)  # for  faces

for (x ,y ,w ,h) in faces:

    image =cv2.rectangle(image ,(x ,y) ,( x +w , y +h) ,(127 ,0 ,205) ,3)

    #Now detect eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray,1.3,2)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)



image = cv2.resize(image ,(800 ,700))
cv2.imshow("Face Detected" ,image)
cv2.waitKey(0)
cv2.destroyAllWindows()


