import cv2 as cv

img = cv.imread('Photos/DSC04262.JPG')

#capture = cv.VideoCapture(0)
#
#while True:
#    isTrue, frame = capture.read()
#    cv.imshow('Video', frame)
#
#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break
#
#capture.release()

# cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), (0,255,0), 40,  thickness = -1)
#cv.line() cv.putText()

#converting image to grayscale- gray = cv.cvtColot(img, cv.COLOR_BGR2GRAY)
#blur - cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

#edge cascade - canny = cv.Canny(ing, 125, 175)

# dilated = cv.dilated(canny, (7,7), iterations = 1)

# eroding - eroded = cv.erode(dilated, (3,3), iterations = 1)

# resize - resize = cv.resize(img, (500,500))

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST)



cv.rectangle(img, (0,0), (img.shape[1]//2, img.shape[0]//2), (0,255,0), thickness = 20)
cv.imshow('bruh', img)

cv.waitKey(0)