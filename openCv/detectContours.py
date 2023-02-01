import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# blur the img 
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#grab edges using canny edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)
contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


cv.waitKey(0)