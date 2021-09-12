
#Objective: find location of certain shapes
#Performing line detection on the image to extract contours


import cv2
import numpy as np

frame = cv2.imread('Images/collage.png')
cv2.imshow('Original',frame)

edges = cv2.Canny(frame,100,200)
cv2.imshow('Edges',edges)


contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


#edges.shape returns a tuple containing width and height
blankImage = np.zeros(edges.shape)

goodContours = []
for contour in contours:
    if cv2.contourArea(contour)>100:
        goodContours.append(contour)

        cv2.polylines(blankImage, contour, isClosed=True, color=(255),thickness=1)


cv2.imshow("big contours", blankImage) 

cv2.waitKey(0)