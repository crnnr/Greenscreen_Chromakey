import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
<<<<<<< Updated upstream

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
=======
import os

# video capture and resolution setting
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segementor = SelfiSegmentation()
fpsReader = cvzone.FPS()

#grabing all images in folder
listImg = os.listdir("./images/")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'./images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0
>>>>>>> Stashed changes

while True:
    success, img = cap.read()
    imgOut = segementor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))

    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
<<<<<<< Updated upstream
    if key == ord('q'):
        th = change_background("1.jpg", segmen, video, th)
    elif key == ord('w'):
        th = change_background("2.jpg", segmen, video, th)
    elif key == ord('e'):
        th = change_background("3.png", segmen, video, th)
    elif key == ord('c'):
        break

=======
#managekeystroke functionality
    if key == ord('+'):
     if indexImg < len(imgList)-1:
        indexImg += 1
    elif key == ord('-'):
     if indexImg > 0:
        indexImg -= 1        
    elif key == ord('c'):
        break
>>>>>>> Stashed changes
