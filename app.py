# imports
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import argparse
import os
import datetime

# defining command line parameters
ap = argparse.ArgumentParser()
ap.add_argument("-ns", "--noslide", help="Remove the slider from the application", action="store_true")
ap.add_argument("-ok", "--onlykeyed", help="Show only the final picture with adjusted background", action="store_true")
ap.add_argument("-t", "--threshold", help="Threshold value to adjust the segmentation", type=float, default=0.8)
ap.add_argument("-b", "--background", help="Show original background image next to keyed out image", action="store_true")
ap.add_argument("-nfps", "--nofps", help="Do not display FPS reader", action="store_true")
args = vars(ap.parse_args())

# get videocapture stuff
cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap.set(3, int(height))
cap.set(4, int(width))
cap.set(cv2.CAP_PROP_FPS, 60)
segementor = SelfiSegmentation()
fpsReader = cvzone.FPS()

# get background images
listImg = os.listdir("./images/")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'./images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0
screenshot_counter = 0

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 900, 300)

# parse parameters and decide what to display
if not args["noslide"]:
    cv2.createTrackbar("Threshold", "Image", int(args["threshold"] * 100), 100, lambda x: x)

while True:
    success, img = cap.read()
    threshold = cv2.getTrackbarPos("Threshold", "Image") / 100 if not args["noslide"] else args["threshold"]
    imgOut = segementor.removeBG(img, imgList[indexImg], threshold=threshold)

    if args["onlykeyed"]:
        if args["background"]:
            imgStacked = cvzone.stackImages([imgList[indexImg], imgOut], 2, 1)
            cv2.imshow("Image", imgStacked)
        else:
            cv2.imshow("Image", imgOut)
    else:
        if args["background"]:
            imgStacked = cvzone.stackImages([imgList[indexImg], img, imgOut], 3, 1)
            cv2.imshow("Image", imgStacked)
        else:
            imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
        if not args["nofps"]:
            _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
        cv2.imshow("Image", imgStacked)

    # define keystrokes
    key = cv2.waitKey(1)
    if key == ord('+'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('-'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('c'):
        break
    elif key == ord('s'):
        fileName = f"./screenshots/screenshot_{str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))}.jpg"
