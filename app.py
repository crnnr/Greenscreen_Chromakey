import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

def change_background(image, segmen, video, th):
    bgimage = cv2.imread(image)
    while True:
        check,frame = video.read()
        videoremovebg = segmen.removeBG(frame,bgimage, threshold=th)
        # Main Window
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        cv2.imshow('video', videoremovebg)
        key = cv2.waitKey(1)
        if key== ord('c'):
            break
        elif key == ord('+'):
            th += 0.05
            print(th)
        elif key == ord('-'):
            th -= 0.05
            print(th)
    return th

video = cv2.VideoCapture(0)
# Auflösung des Videos
video.set(3,640)
video.set(4,480)
# Hintergrundbilder müssen genau diese Auflösung haben!


segmen = SelfiSegmentation()

# Setzen Intialer Threshold
th = 0.45

while True:
    _,frame = video.read()
    #Main Window Initieren
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        th = change_background("1.jpg", segmen, video, th)
    elif key == ord('w'):
        th = change_background("2.jpg", segmen, video, th)
    elif key == ord('e'):
        th = change_background("3.png", segmen, video, th)
    elif key == ord('c'):
        break

