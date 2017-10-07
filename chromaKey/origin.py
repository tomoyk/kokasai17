#!/usr/bin/env python

import numpy as np
import cv2

# Windows size Swttings
winSize = ( 1300, 700 )

# Camera Settings
videoStr = cv2.VideoCapture(0)

# Background Settings
backVdo = cv2.VideoCapture('videos/campus.mp4')

while(True):
    # Get each frame
    ret, front = videoStr.read()
    ret, back  = backVdo.read()

    # Resize movies
    front = cv2.resize(front, winSize)
    back = cv2.resize(back, winSize)

    # Split front-movie colors to RGB
    BGR = cv2.split(front)

    # Thresh Settings
    #
    # [memo]
    # cv2.THRESH_BINARY      cv2.THRESH_OTSU        cv2.THRESH_TRIANGLE
    # cv2.THRESH_BINARY_INV  cv2.THRESH_TOZERO      cv2.THRESH_TRUNC
    # cv2.THRESH_MASK        cv2.THRESH_TOZERO_INV
    # 
    threshB = [cv2.THRESH_BINARY, 120]
    threshR = [cv2.THRESH_BINARY_INV, 60]
    threshG = [cv2.THRESH_BINARY, 60]

    # Set channnel-color
    _, maskB = cv2.threshold(BGR[0], threshB[1], 1, threshB[0])
    _, maskR = cv2.threshold(BGR[1], threshR[1], 1, threshR[0])
    _, maskG = cv2.threshold(BGR[2], threshG[1], 1, threshG[0])

    # Catinate each mask
    view = cv2.merge(BGR + [255 * maskB * maskG * maskR])

    # Display windows
    cv2.imshow('DEMO:view',view)
    cv2.imshow('DEMO:back', back)

    # Delay 10ms and Check keydown 'q' for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release objects
videoStr.release()
backVdo.release()
cv2.destroyAllWindows()   

