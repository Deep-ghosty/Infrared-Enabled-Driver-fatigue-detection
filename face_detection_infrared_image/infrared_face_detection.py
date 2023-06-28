import cv2
import imutils

# Load the Haar cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the video stream
cap = cv2.VideoCapture(0)

# Initialize a counter for saved screenshots
screenshot_counter = 0

# Loop indefinitely
while True:
    # Read the frame from the video stream
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Infrared Camera', frame)

    # Check for key press events
    key = cv2.waitKey(1) & 0xFF

    # Save a screenshot when 's' key is pressed
    if key == ord('s'):
        screenshot_filename = f'screenshot_{screenshot_counter}.png'
        cv2.imwrite(screenshot_filename, frame)
        print(f'Screenshot saved as {screenshot_filename}')
        screenshot_counter += 1

    # Check if the user pressed the 'q' key
    if key == ord('q'):
        break

# Release the video stream
cap.release()
cv2.destroyAllWindows()
