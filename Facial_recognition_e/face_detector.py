import cv2
import glob



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#images = glob.glob('*.jpg')
img = cv2.imread('news.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.3, minNeighbors= 5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0),3)

image_resize = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
print(type(faces))
print(faces)
cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()