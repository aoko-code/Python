import cv2 as cv
import numpy as np

# create blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
#datatype of an image = uint8
# cv.imshow('Blank', blank)

#paint img certain color
blank[200:300] = 0, 255,0
# cv.imshow('Green', blank)

#draw rectancle
cv.rectangle(blank, (0, 0), (250,250), (0, 0, 255), thickness=-1)
# cv.imshow('rectangle', blank)

#draw circle
cv.circle(blank, (250,250), 30, (255, 0, 0), thickness=-1)
# cv.imshow('circle', blank)

#draw line
cv.line(blank, (0,0), (250, 250), (255, 255, 255))
# cv.imshow('line', blank)
#write text
cv.putText(blank, 'hello my name is cynthia', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 250, 0), 2)
cv.imshow('text', blank)
cv.waitKey(0)
