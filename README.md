

<h1 align="center">Driver-Snoozing-System</h1> 
<div align="center">
  <img src="https://media3.giphy.com/media/3orieNJUfjfm4txQkg/giphy.gif?cid=ecf05e47xg5nqugakk8npub55zzcpktosnjxvmrhgu7rxg8f&rid=giphy.gif&ct=g.gif" border="0"></
  </p>

  
The Driver-Snoozing-System is a machine learning system designed to detect when a driver is falling asleep at the wheel and alerts the driver before an accident occurs. The system uses the **shape_predictor_68_face_landmarks.dat file**, which contains data about the location of 68 facial landmarks on a person's face, to analyze the driver's face and determine if they are exhibiting signs of drowsiness.</p>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
</div>

## How to Contribute?

- Take a look at the [contribution guide](/.github/CONTRIBUTING.md)

## How to make a Pull Request?
- Take a look at  [Pull Request guide](.github/Pull_request_guide.md)

# Usage 
_To get a local copy up and running follow these simple steps._
- Clone the repository with 
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
- The shape_predictor_68_face_landmarks.dat file was trained using the [**dlib**](http://dlib.net/) library.
- The face detection functionality is based on the [**OpenCV**](https://opencv.org/) library.


 ### Repo holders
[Ekansh rajput](https://github.com/Regression1607)
<br>
[Divyansh mittal](https://github.com/Divyansh-Mitta01 )</br>
## Miscellaneous

Do consider looking at other paradigms of this documentation
  - [Code Of Conduct](/.github/CODE_OF_CONDUCT.md)
  - [How to contribute?](/.github/CONTRIBUTING.md)
  - [How to Make a Pull Request](.github/Pull_request_guide.md)

[contributors-shield]: https://img.shields.io/github/contributors/Deep-ghosty/Driver-Snoozing-System.svg?style=for-the-badge
[contributors-url]: https://github.com/Deep-ghosty/Driver-Snoozing-System/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Deep-ghosty/Driver-Snoozing-System.svg?style=for-the-badge
[forks-url]: https://github.com/Deep-ghosty/Driver-Snoozing-System/network/members
[stars-shield]: https://img.shields.io/github/stars/Deep-ghosty/Driver-Snoozing-System.svg?style=for-the-badge
[stars-url]: https://github.com/Deep-ghosty/Driver-Snoozing-System/stargazers
[issues-shield]: https://img.shields.io/github/issues/Deep-ghosty/Driver-Snoozing-System.svg?style=for-the-badge
[issues-url]: https://github.com/Deep-ghosty/Driver-Snoozing-System/issues
