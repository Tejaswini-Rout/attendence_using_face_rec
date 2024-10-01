import face_recognition
import csv
import cv2
import numpy as np
import os
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load known face images and get face encodings
cat_image = face_recognition.load_image_file("imagee/cat.jpg")
cat_encodings = face_recognition.face_encodings(cat_image)[0]

dog_image = face_recognition.load_image_file("imagee/dog.jpg")
dog_encodings = face_recognition.face_encodings(dog_image)[0]

rabbit_image = face_recognition.load_image_file("imagee/rabbit.jpg")
rabbit_encodings = face_recognition.face_encodings(rabbit_image)[0]

ak_image = face_recognition.load_image_file("imagee/ak.jpg")
ak_encodings = face_recognition.face_encodings(ak_image)[0]

# Known face encodings and their corresponding names
known_face_encodings = [
    cat_encodings,
    dog_encodings,
    rabbit_encodings,
    ak_encodings
]
known_face_names = [
    "Cat",
    "Dog",
    "Rabbit",
    "Ak"
]

# Copy list for students to mark attendance
students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

# Create a CSV file with the current date as the filename
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

with open(current_date + '.csv', 'w+', newline='') as f:
    lnwriter = csv.writer(f)

    while True:
        # Capture video frame
        _, frame = video_capture.read()

        # Resize the frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if s:
            # Detect faces and get face encodings
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for face_encoding in face_encodings:
                # Compare face encodings with known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = ""
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

                # Mark attendance
                if name in known_face_names and name in students:
                    students.remove(name)
                    print(students)

                    # Log the current time for the recognized student
                    current_time = datetime.now().strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

        # Display the video feed (optional)
        cv2.imshow('Video', frame)

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close any open windows
video_capture.release()
cv2.destroyAllWindows()
