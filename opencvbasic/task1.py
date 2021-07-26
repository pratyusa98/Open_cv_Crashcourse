#image conversion project colored image into grayscale
import cv2

path = input("Enter the Path and name of an image: ")
print("You Enter this===",path)

img = cv2.imread(path,0)
img = cv2.resize(img,(560,700)) # width , height

img1 = cv2.flip(img,-1)#it accept 3 parameters 0,-1,1


cv2.imshow("original",img)
cv2.imshow("original_flip",img1)

k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite(r"C:\Users\Dell\Desktop\Opencv_Python\opencv2\resources\thor_gray.png",img)
    print("Save Successfully.....")
elif k == ord("q"):
    cv2.destroyAllWindows()
    print("Close")