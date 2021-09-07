import cv2 as cv
import numpy


img = cv.imread('Images/stock-photo.jpg')
cv.imshow('Stock Photo', img)



capture = cv.VideoCapture('Images/fire.mp4')


while True:
    isTrue,frame=capture.read()
    #show frame
    cv.imshow('',frame)

    #if the d key is pressed, kill screen
    if cv.waitKey(20) & 0xFF==ord('d'):
        break



capture.release()

cv.destroyAllWindows()

cv.waitKey(0) 