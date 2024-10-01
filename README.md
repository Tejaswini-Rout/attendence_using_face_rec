# face_rec
Code Overview
The system captures a video feed from a webcam, detects faces, compares them to a set of known face encodings, and logs attendance to a CSV file if the recognized face hasn't been marked present yet.
It writes the name of the recognized person and the time they were recognized into a CSV file named after the current date.
Key Components:
Face Recognition:

The code uses the face_recognition library to load images and get their face encodings.
These encodings are then compared to the faces detected in the video feed.
Video Capture:

cv2.VideoCapture(0) is used to access the webcam feed.
Frames are resized to 25% of their original size to speed up the face recognition process.
CSV Logging:

The recognized person's name and the time of recognition are written to a CSV file, ensuring no duplicate attendance marks for the same individual.
Attendance Logic:

Once a face is recognized, the person is removed from the students list to prevent multiple entries for the same person.
