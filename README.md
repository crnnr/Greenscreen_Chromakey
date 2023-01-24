Background Changer

This is a simple Python script that allows you to change the background of a live video feed using OpenCV and the SelfiSegmentationModule from the cvzone package.
Features

    Changes the background of a live video feed to a specified image
    Allows for adjusting the threshold value for the background removal
    Allows for switching between multiple background images

Setup
Prerequisites

    Python 3.x
    OpenCV
    cvzone

Installation

    Install the required packages by running pip install opencv-python cvzone in your command line.
    Clone or download this repository to your local machine.
    Run the script using python background_changer.py

Usage

    Run the script and allow access to your webcam.
    Press 'q', 'w' or 'e' to change the background to the corresponding image.
    Press '+' or '-' to adjust the threshold value for the background removal.
    Press 'c' to exit the program.

Note

    Make sure that the background images you want to use have the same resolution as your webcam's resolution.
    The script uses the webcam's resolution of 640x480 by default, but you can change it by modifying the video.set(3,640) and video.set(4,480) lines in the script.

Limitations

    The SelfiSegmentationModule is not perfect, so the background removal may not always be accurate.
    The script can only handle one person in the video feed.
    The script only works with static background images.
