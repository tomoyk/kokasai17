#!/usr/bin/env python

import numpy as np
import cv2

# Background Settings
backWid = 1300
backHei = 700
backVdo = cv2.VideoCapture('backVdo.avi')

# Camera Settings
vStream = cv2.VideoCapture(0)


while(True):
    # Get each frame
    ret, front = vStream.read()
    ret, back  = backVdo.read()

    

    

