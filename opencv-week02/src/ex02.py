import cv2

# Open the default webcam (camera index 0)
cap = cv2.VideoCapture(0)
# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
while True:
    # Read a frame from the webcam
    check, frame = cap.read()
    if not check:
        print("❌ Cannot access camera")
        break
    # Convert frame to grayscale (Haar works on grayscale images)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    face_detect = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.1,  # How much the image is reduced at each scale
        minNeighbors=5,  # Higher value » fewer detections but more accurate
        minSize=(30, 30),  # Minimum face size to detect
    )
    # Draw bounding boxes on detected faces
    for x, y, w, h in face_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    # Display the output frame
    cv2.imshow("Face Detection Camera", frame)
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
