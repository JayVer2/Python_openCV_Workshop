import cv2
import numpy as np


def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)




#Read img
img = cv2.imread('Images/stock-photo.jpg')

cv2.imshow('Original', img)

#RESIZE
#print(img.shape)
#(1200,972,3) is the size
height = int(img.shape[0] * 0.5)
width = int(img.shape[1] * 0.5)
dim = (width,height)

resized=cv2.resize(img,dim)
cv2.imshow('Resize',resized)

#Use the resized image for the rest
#GREYSCALE and the others
greyscale=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
greyscale=cv2.GaussianBlur(greyscale,(9,9),cv2.BORDER_DEFAULT)
greyscale=cv2.Canny(greyscale,125,200)
cv2.imshow('Greyscale',greyscale)

#ROTATE
rotated = rotate(resized,45)
cv2.imshow('Rotate',rotated)

#DRAW
draw = cv2.circle(resized, (300,175), 80, (0,0,255), thickness=3)
cv2.line(draw,(300-50,175-50),(300+50,175+50),(0,0,255),thickness=3)
cv2.line(draw,(300-50,175+50),(300+50,175-50),(0,0,255),thickness=3)
cv2.imshow('Draw',draw)




cv2.waitKey(0) 