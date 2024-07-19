# CODTECH-Computer-Vision
Face Detection Setup:

face_cascade = cv2.CascadeClassifier("/content/haarcascade_frontalface_default.xml"): This line creates a cascade classifier object from the provided XML file (haarcascade_frontalface_default.xml). Cascade classifiers are pre-trained models used for object detection in images and videos. The specific model here is designed to detect frontal human faces.
Image Loading and Grayscale Conversion:

img = cv2.imread("/content/image.png"): This line reads the image from the specified path (/content/image.png) using OpenCV's imread function. The image is assumed to be in BGR (Blue, Green, Red) color format, which is OpenCV's default.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): This line converts the loaded image from BGR to grayscale format using OpenCV's cvtColor function. Face detection algorithms typically work better on grayscale images.
Face Detection (Assuming You're Using Google Colab):

from google.colab.patches import cv2_imshow: This line imports the cv2_imshow function from Google Colab's patches module. This function is likely a custom wrapper around OpenCV's imshow function, potentially addressing display issues within Colab's environment.
cv2_imshow(gray_img): This line displays the grayscale image using the cv2_imshow function.
Drawing Rectangles on Detected Faces:

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5): This line performs the actual face detection. It uses the detectMultiScale method of the cascade classifier to find faces in the grayscale image. The parameters provided control how the detection is performed:
scaleFactor=1.05: This value indicates how much the image will be scaled down in each successive detection pass (slightly smaller to detect faces at different scales).
minNeighbors=5: This parameter specifies the minimum number of neighboring rectangles that must be detected to consider it a true face detection.
for x, y, w, h in faces: This line iterates over the detected faces, where x, y represent the top-left corner coordinates, w is the width, and h is the height of the bounding rectangle around each detected face.
img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3): This line draws a red rectangle (BGR color (255, 0, 0)) with a thickness of 3 pixels around each detected face on the original color image (img).
Potential Display in Google Colab:

cv2_imshow(img): This line, assuming it's similar to OpenCV's imshow, would display the final image with the drawn rectangles on the detected faces within a window in Google Colab's environment.
In essence, this code snippet performs face detection in a given image, converts the image to grayscale for better detection, and then displays the original color image with red rectangles drawn around the detected faces.


![Screenshot 2024-07-19 170544](https://github.com/user-attachments/assets/74c18ec5-4b4a-4d2d-89f3-606d0b254ed9)






