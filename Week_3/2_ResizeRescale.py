import cv2

#First function rescales the frame
def rescaleFrame(frame, scale = 0.25):

    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


#Second function for changing resolution
def ChangeRes(width,height):

    capture.set(3,width)
    capture.set(4,height)


#Read and rescale image
img = cv2.imread('Images/stock-photo.jpg')
rescale_img = rescaleFrame(img)
cv2.imshow('Stock Photo', rescale_img)

#Read vid
capture = cv2.VideoCapture('Images/fire.mp4')



while True:
    isTrue,frame=capture.read()

    #Rescale
    frame_resized = rescaleFrame(frame)

    cv2.imshow('',frame)
    cv2.imshow('Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()