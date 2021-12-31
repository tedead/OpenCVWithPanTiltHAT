#!/usr/bin/python3
#import tflite_runtime.interpreter as tflite
import math
import time
import pantilthat
import keyboard
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2

pantilthat.pan(0)
pantilthat.tilt(0)
pan = 0
tilt = 0

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

while True:
    key = cv2.waitKey(1) & 0xFF
    print(keyboard.read_key())
    
    if key == ord("q"):
       print("You pressed q")
        
    if keyboard.read_key() == "up":
        if tilt > -90:
            tilt = tilt - 2
            pantilthat.tilt(tilt)
            print("Tilt: " + str(tilt))
    
    if keyboard.read_key() == "down":
        if tilt < 90:
            tilt = tilt + 2
            pantilthat.tilt(tilt)
            print("Tilt: " + str(tilt))
    
    if keyboard.read_key() == "left":
        if pan < 90:
            pan = pan + 2
            pantilthat.pan(pan)
            print("Pan: " + str(pan))
    
    if keyboard.read_key() == "right":
        if pan > -90:
            pan = pan - 2
            pantilthat.pan(pan)
            print("Pan: " + str(pan))
