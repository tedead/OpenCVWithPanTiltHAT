#!/usr/bin/python3
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import pantilthat
#import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60 #32
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera

pantilthat.pan(0)
pantilthat.tilt(0)
pan = 0
tilt = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    cv2.imshow("Frame", image)
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == 113:#ord("q"): q key pressed
      break

    #print("Current tilt: " + str(tilt))
    #print("Current pan: " + str(pan))
    #if(key != 255):
    #    print(key)

    if key == 82: #up arrow
        if tilt > -90:
            tilt = tilt - 2
            print("Up arrow tilt: " + str(tilt))
            if(tilt >= -90):
                pantilthat.tilt(tilt)

    if key == 84: #down arrow
        if tilt < 90:
            tilt = tilt + 2

            print("Down arrow tilt: " + str(tilt))

            if(tilt <= 90):
                pantilthat.tilt(tilt)

    if key== 81: #left arrow
        if pan < 90:
            pan = pan + 2

            print("Left arrow pan: " + str(pan))

            if(pan <= 90):
                pantilthat.pan(pan)

    if key== 83: #right arrow
        print("Right arrow keypress. Current pan: " + str(pan))
        if pan > -90:
            pan = pan - 2
            print("Right arrow pan: " + str(pan))
            if(pan >= -90):
                #pantilthat.pan(-90)
                pantilthat.pan(pan)
            #else:
                #pantilthat.pan(pan)
                
    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(0.005)