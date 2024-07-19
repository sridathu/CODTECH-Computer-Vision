import cv2
face_cascade =cv2.CascadeClassifier("/content/haarcascade_frontalface_default.xml")
img = cv2.imread("/content/image.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
from google.colab.patches import cv2_imshow
cv2_imshow(gray_img)
#Apply face_cascade to the gary image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
minNeighbors=5)
print(faces)
for x,y,w,h in faces:
  img=cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
cv2_imshow(img)
