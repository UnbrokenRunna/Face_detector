import cv2
#Fetch the xml file code to detect face
faces_cascade_try = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#REad the image
img = cv2.imread('news.jpg')

#convert image to gray

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces_search = faces_cascade_try.detectMultiScale(gray_img, scaleFactor = 1.3, minNeighbors =5)

for x, y, w, h in faces_search:
    img = cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0),3)
im_resize =cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
print(type(faces_search))
print(faces_search)
cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows