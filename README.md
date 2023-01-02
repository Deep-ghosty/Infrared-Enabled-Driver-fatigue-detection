# Driver-Snoozing-System

The Driver-Snoozing-System is a machine learning system designed to detect when a driver is falling asleep at the wheel and alert them before an accident occurs. The system uses the **shape_predictor_68_face_landmarks.dat file**, which contains data about the location of 68 facial landmarks on a person's face, to analyze the driver's face and determine if they are exhibiting signs of drowsiness.

### To implement a driver snoozing system , you would need to follow these steps:

1. Install the necessary libraries, such as dlib and OpenCV, and download the shape_predictor_68_face_landmarks.dat file.
2. Load the shape_predictor_68_face_landmarks.dat model and use it to detect and identify facial landmarks in video frames captured from a camera or video file.
3. Analyze the facial landmarks to determine whether the driver is snoozing or not. For example, you could check whether the driver's eyes are closed or partially closed for a certain amount of time.
4. If the driver is detected as snoozing, trigger an alarm or notification to alert the driver and prevent a potential accident.


Requirements
Python 3.x
dlib
OpenCV
# Usage
- Clone the repository: 
```
git clone https://github.com/your-username/driver-snoozing-system.git
```
- Install the necessary libraries: 
```
pip install -r requirements.txt
```
- Run the snoozing detection script: 
```
python detect_snoozing.py
```


# Acknowledgments
- The shape_predictor_68_face_landmarks.dat file was trained using the dlib library.
- The face detection functionality is based on the **OpenCV** library.
