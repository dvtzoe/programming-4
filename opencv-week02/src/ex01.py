import cv2

# 1) Load and convert
img = cv2.imread(r"/home/dvtzoe/kosen/programming-4/opencv-week02/assets/face.png")
img = cv2.resize(img, (600, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2) Detect faces
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
)
# 3) Draw bounding boxes
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
