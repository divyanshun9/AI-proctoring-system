import cv2
import time

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera

# Measure FPS
start_time = time.time()
num_frames = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    num_frames += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Calculate FPS
end_time = time.time()
fps = num_frames / (end_time - start_time)

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

print(f"Average FPS: {fps}")
