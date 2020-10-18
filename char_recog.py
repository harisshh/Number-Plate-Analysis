import cv2
import pytesseract

#importing pytesseract from our device

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

#read the cropped image

img = cv2.imread('imgslice.jpg')

#color conversion to grayscale

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Detecting Characters

h1, w1,_ = img.shape
print("Plate dimension-" + " " + str(h1) + " x" + " " + str(w1) + " mm")
boundbox = pytesseract.image_to_boxes(img)
for b in boundbox.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,h1- y), (w,h1- h), (0, 0, 255), 2)
    print("Width: " + " " + str(w) + " mm")
    print("Height: " + " " + str(h) + " mm")

#displaying the output image

cv2.imshow('img', img)
cv2.waitKey(0)