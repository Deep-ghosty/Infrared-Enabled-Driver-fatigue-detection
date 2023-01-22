@echo off

title Install Pre-requsites
echo These following packages would be installed..
echo oopencv-python
echo numpy
echo imutils
echo pygame
echo dlib
echo cmake
pause

start /WAIT /B pip install opencv-python
start /WAIT /B pip install numpy
start /WAIT /B pip install imutils
start /WAIT /B pip install pygame
echo If Prompted, click Yes to install cMake
pause
start /WAIT /B winget install cmake
echo Now Add an Environment Varriable in Path
echo Select Path, click on Edit and add this path C:\Program Files\CMake\bin
pause
start /WAIT /B rundll32 sysdm.cpl,EditEnvironmentVariables
echo Press any key if PATH is added
pause 
start /WAIT /B pip install cmake
start /WAIT /B pip install dlib