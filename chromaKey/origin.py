#!/usr/bin/env python

import numpy as np
import cv2

# Windows size Swttings
winSize = ( 1300, 700 )

# Sets color-range of mask
# [memo] (Blue, Green, Red)
#
lower = np.array([60/2, 50, 80])     # Min
upper = np.array([250/2, 255, 255])  # Max

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

    # Convert BGR to HSR
    hsvFront = cv2.cvtColor(front, cv2.COLOR_BGR2HSV)

    # Make mask by 'hsvFront'
    maskFront = cv2.inRange(hsvFront, lower, upper)

    # Apply Gaussian-blur
    # gMaskFront = cv2.GaussianBlur(maskFront, (5, 5), 0)

    # Revrse Mask area
    # rgMaskFront = cv2.bitwise_not(gMaskFront)
    rgMaskFront = cv2.bitwise_not(maskFront)

    # Attach mask
    streamFront = cv2.bitwise_and(front, front, mask=rgMaskFront)
    streamBack = cv2.bitwise_and(back, back, mask=maskFront)

    # Catinate each mask
    disp = cv2.bitwise_or(streamFront, streamBack, maskFront)

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

