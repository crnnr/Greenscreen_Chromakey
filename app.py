import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
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
while True:
    success, img = cap.read()
    imgOut = segementor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))

    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('+'):
     if indexImg < len(imgList)-1:
        indexImg += 1
    elif key == ord('-'):
     if indexImg > 0:
        indexImg -= 1        
    elif key == ord('c'):
        break
