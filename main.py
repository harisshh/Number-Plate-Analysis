# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
import cv2
import numpy as np
import imagetools

#identify the contours in the image

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #find the length and area of each contours

        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        area = cv2.contourArea(cnt)
        print(area)

        #eliminate the unwanted contour details by applying the below condition

        if area > 500 and len(approx) == 4:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
path = 'image.jpg'

#read the image

img = cv2.imread(path)

#getting a copy of the original image to identify contours and draw them

imgContour = img.copy()

#color conversion

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)

#canny edge detection to identify all the edges

imgCanny = cv2.Canny(imgBlur,50,50)
circles = cv2.HoughCircles(imgGray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
masking=np.full((img.shape[0], img.shape[1]),0,dtype=np.uint8)
for j in circles[0, :]:
    cv2.circle(masking, (j[0], j[1]), j[2], (255, 255, 255), -1)

#cropping the image to our desired portion

height, width = img[:2]
croppedImg = cv2.imread('imgslice.jpg')


getContours(imgCanny)
final_img = cv2.bitwise_or(img, img,mask= masking)
cv2.imshow("1",img)
cv2.imshow("2",imgGray)
cv2.imshow("3",imgBlur)
cv2.imshow("4",imgCanny)
cv2.imshow("5",imgContour)
cv2.imshow("6",final_img)
cv2.imshow("7",croppedImg)

cv2.waitKey(0)





