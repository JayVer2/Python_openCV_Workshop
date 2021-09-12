
import cv2
import numpy as np


frame = cv2.imread('Images/collage.png')
edges = cv2.Canny(frame,100,200)


#Load pentagon from template
pentagon = cv2.imread('Images/pentagon.png')
#cv2.imshow('pentagon', pentagon)
pentagonCanny = cv2.Canny(pentagon,100,200)
pentagonContours, hierarchy = cv2.findContours(pentagonCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


pentagonBlank = np.zeros(pentagon.shape)
cv2.polylines(pentagonBlank,pentagonContours, True,(255),1)


pentagonMoments = cv2.moments(pentagonContours[1])
pentagonHuMoments = cv2.HuMoments(pentagonMoments)


print("pentagonHuMoments:\n",pentagonHuMoments,"\n")

contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

blankImage = np.zeros(edges.shape)


goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        #find the difference between moments
        delta = np.sum(pentagonHuMoments-contourHuMoments)
        print(delta)
        if (np.abs(delta)<0.002): #0.002 is our threshold
            print(np.abs(delta))
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,True,(255),1)


#cv2.imshow("pentagon", pentagonBlank)
#cv2.imshow("pentagonContour", pentagonCanny)
cv2.imshow("edges", edges) 
cv2.imshow("good contours", blankImage) 

cv2.waitKey(0)