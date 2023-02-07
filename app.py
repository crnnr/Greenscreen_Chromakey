import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-ns", "--noslide", help="Remove the slider from the application", action="store_true")
ap.add_argument("-ok", "--onlykeyed", help="Show only the final picture with adjusted background", action="store_true")
args = vars(ap.parse_args())



cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Camera resolution:",width, height)
cap.set(3, int(height))
cap.set(4, int(width))
cap.set(cv2.CAP_PROP_FPS, 60)
segementor = SelfiSegmentation()
fpsReader = cvzone.FPS()

listImg = os.listdir("./images/")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'./images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

if not args["noslide"]:
    cv2.createTrackbar("Threshold", "Image", 80, 100, lambda x: x)

while True:
    success, img = cap.read()
    threshold = cv2.getTrackbarPos("Threshold", "Image") / 100 if not args["noslide"] else 0.8
    imgOut = segementor.removeBG(img, imgList[indexImg], threshold=threshold)

    if args["onlykeyed"]:
        cv2.imshow("Image", imgOut)
    else:
        imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
        _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
        cv2.imshow("Image", imgStacked)

    key = cv2.waitKey(1)
    if key == ord('+'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('-'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('c'):
        break
