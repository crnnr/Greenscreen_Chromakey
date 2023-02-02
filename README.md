# Greenscreen_Chromakey
Captures Stream of Webcam and replaces with a custom picture

# What you'll need
Python 3.9.X and above

# How to Setup

1. Install python Packages: `opencv-python, cvzone, mediapipe`
2. Clone Repository
3. Run in commandline via cmd: 
   `python app.py`
Note: The App can be closed by pressing "c" or Interrupting the process with Ctrl-C 

# Features

1. Dynamic Backgroundimage selection:

Included in the repo is an "Image" Folder.
After running the app it scans the folder for pictures and puts them in an Array. 
You can then cycle trough Pictures using the "+" and "-" Key.
This folder can be changed in lines 13 and 17 in the Code. 
Please note that the Pictures need to have the same resolution as the Webcam.

# Command line parameters

-noslide: Removes the slider from the app

-onlykeyed: Shows only the final picture with the adjusted background, no webcam feed or slider.

# TODO

1. Implement Dynamic Threshold Adjustment
2. Add logging functions
