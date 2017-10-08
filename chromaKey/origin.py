#!/usr/bin/env python

import numpy as np
import cv2

# Windows size Swttings
winSize = ( 1300, 700 )

# Camera Settings
videoStr = cv2.VideoCapture(1)

# Background Settings
backVdo = cv2.VideoCapture('videos/campus.mp4')

while(True):
    # Get each frame
    ret, front = videoStr.read()
    ret, back  = backVdo.read()

    # Resize movies
    front = cv2.resize(front, winSize)
    back = cv2.resize(back, winSize)

    ###################
    hsv = cv2.cvtColor(front, cv2.COLOR_BGR2HSV)
    lower = np.array([60/2, 50, 80])
    upper = np.array([250/2, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    inv_mask = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(front,front,mask= inv_mask)
    res2 = cv2.bitwise_and(back,back,mask=  mask)
    disp = cv2.bitwise_or(res1,res2,mask)

    # Catinate each mask
    # view = cv2.merge(BGR + [255 * maskB * maskG * maskR])

    # Display windows
    cv2.imshow('DEMO:disp',disp)
    # cv2.imshow('DEMO:front',front)
    # cv2.imshow('DEMO:back',back)

    # Delay 10ms and Check keydown 'q' for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release objects
videoStr.release()
backVdo.release()
cv2.destroyAllWindows()   

