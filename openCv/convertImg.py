import cv2 as cv

img = cv.imread('Resources/Photos/lady.jpg')

cv.imshow('Cat', img)

#convert image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', gray)
#blur image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
#edge cascade

cv.waitKey(0)