import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)
# cv.imshow('Cat', img)
# convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# blur the img 
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

#grab edges using canny edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)

#GRAB EDGES USING THRESHOLD
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresgold', thresh)
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
cv.waitKey(0)
#boundaries of objects
