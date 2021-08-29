
import cv2
import numpy as np

img =cv2.imread('park.jpg')

cv2.imshow('Park',img)

#Translate function
def translation(img, x, y):
    #-x = left
    #-y = up
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])

    return cv2.warpAffine(img,transMat,dimensions)


#Call the function
translated = translation(img,100,100)
cv2.imshow('translated',translated)

#Rotate
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

rotated= rotate(img,-95)
cv2.imshow('Rotate',rotated)


flip=cv2.flip(img,-1)
cropped = img[200:400,200:400]

cv2.imshow('Flipped',flip)
cv2.imshow('Cropped',cropped)



cv2.waitKey(0)