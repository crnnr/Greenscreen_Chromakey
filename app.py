import cv2
import numpy as np

# Initialize the background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

def change_background(image, video):
    bg_image = cv2.imread(image)
    bg_image = cv2.resize(bg_image, (640, 480))
    for i in range(30):
        check, frame = video.read()
        fgmask = bg_subtractor.apply(frame)
    while True:
        check, frame = video.read()
        fgmask = bg_subtractor.apply(frame)
        _, fgmask = cv2.threshold(fgmask, 128, 255, cv2.THRESH_BINARY)
        black_img = np.zeros_like(frame)
        cv2.bitwise_and(black_img, black_img, mask=fgmask)
        cv2.addWeighted(bg_image, 0.7, black_img, 0.3, 0, black_img)
        cv2.imshow('video', image)
        key = cv2.waitKey(1)
        if key == ord('c'):
            break

video = cv2.VideoCapture(0)
# Auflösung des Videos
video.set(3,640)
video.set(4,480)

while True:
    _,frame = video.read()
    #Main Window Initieren
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        change_background("1.jpg", video)
    elif key == ord('w'):
        change_background("2.jpg", video)
    elif key == ord('e'):
        change_background("3.png", video)
    elif key == ord('c'):
        break