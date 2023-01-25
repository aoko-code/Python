import cv2 as cv
import numpy as np
img = cv.imread('Resources/Photos/cats 2.jpg')

#translate img(shift img along x and y axis)
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #matrix
    dimensions = (img.shape[1], img.shape[0]) #width and height
    
    return cv.warpAffine(img, transMat, dimensions)
# -x ==> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#rotate image
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#rotate rotated img
rotated_rotates = rotate(rotated, -45)
cv.imshow('rotate rotated img', rotated_rotates)

#resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#flipping
flip = cv.flip(img, -1)
cv.imshow('flipped', flip)

cv.waitKey(0)

