# Number-Plate-Analysis
This project is about identifing number plate from a given picture and analysing the dimensions of each and every character. This is the starting phase of an idea that can be used to identify number plates of over-speeding or suspicious cars from cctv footages.
# Installing the required packages
If you're using IDE's such as PyCharm, Sublime Text, then it won't be much of a burden for you. 
1. Go to settings and click on the "+" icon.
2. Search for the package that you want to install.
Download links to Python IDE and packages:
1. Download PyCharm for Windows- https://www.jetbrains.com/pycharm/download/#section=windows
2. Doenload Jupyter for Windows- https://jupyter.org/
3. Pytesseract or windows- https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
4. Numpy download- https://pypi.org/project/numpy-turtle/0.2/#files
5. OpenCV- https://opencv.org/releases/

Now, Let's get started.
Import OpenCV and numpy. These are the primary libraries we'll put to use in the long run. Read your image. You can either use a copy of your original image or gray scale-converted image of your image to find the contours. After finding the contour points, draw the contours. Since we want the contour to be plotted only around the number plate, apply area and length constraints to eliminate the other useless possibilities. After drawing the contour plot, crop that part and save it as another file. Using pytesseract,ectract the text from our cropped image. Use dimension analysis to fetch the height and width of every characters and the dimension of the number plate.
