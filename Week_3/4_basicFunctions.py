
import cv2
#Read img
img = cv2.imread('stock-photo.jpg')
#cv2.imshow('Cat', img)

#Greyscale function
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
greyscale=cv2.resize(greyscale,(500,500))
cv2.imshow('Grey',greyscale)

#Blur function
blur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
#ksize has to be odd numbers
blur=cv2.resize(blur,(500,500))
cv2.imshow('Blur',blur)

#Canny function
canny=cv2.Canny(img,125,200)
canny=cv2.resize(canny,(500,500))
cv2.imshow('Canny',canny)

#Dilate
dilated=cv2.dilate(canny,(3,3),iterations=1)
dilated=cv2.resize(dilated,(500,500))
cv2.imshow('Dilated',dilated)

#Erode function
eroded=cv2.erode(dilated,(3,3),iterations=1)
eroded=cv2.resize(eroded,(500,500))
cv2.imshow('Eroded',eroded)

#Resize
resized=cv2.resize(img,(500,500))
cv2.imshow('Resize',resized)

cv2.waitKey(0)
