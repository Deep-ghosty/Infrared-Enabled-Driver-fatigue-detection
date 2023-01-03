# Driver-Snoozing-System

The Driver-Snoozing-System is a machine learning system designed to detect when a driver is falling asleep at the wheel and alert them before an accident occurs. The system uses the **shape_predictor_68_face_landmarks.dat file**, which contains data about the location of 68 facial landmarks on a person's face, to analyze the driver's face and determine if they are exhibiting signs of drowsiness.


# Usage
- Clone the repository: 
```
git clone https://github.com/Deep-ghosty/driver-snoozing-system.git
```
- Install the necessary libraries: 
```
pip install -r requirements.txt
```
- Run the snoozing detection script: 
```
python driver_drowsiness.py
```


# Acknowledgments
- The shape_predictor_68_face_landmarks.dat file was trained using the dlib library.
- The face detection functionality is based on the **OpenCV** library.
