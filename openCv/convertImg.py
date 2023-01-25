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
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)
#dilate img
dilated = cv.dilate(canny, (3, 3), iterations= 1)
cv.imshow('dilated', dilated)
#eroding dilated image
eroded = cv.erode(dilated, (3, 3), iterations= 1)
cv.imshow('eroded', eroded)
#resizing the img
resized = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized', resized)
#CROPPING
cropped = img[50:200, 100:400]
cv.imshow('cropped', cropped)
# flipping img
flip = cv.flip(img, -1)
cv.imshow('flipped', flip)
cv.waitKey(0)