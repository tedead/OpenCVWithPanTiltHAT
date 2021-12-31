import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import pantilthat
import time

def main():
    print("hi")
    # allow the camera to warmup
    time.sleep(0.1)
    # capture frames from the camera

    #Get current pan & tilt from the PanTilt Hat.
    #This hat moves the camera around. 180 degrees on both x & y axis (-90 to 90)
    pan = pantilthat.get_pan()
    tilt = pantilthat.get_tilt()
    print(pantilthat.show())
    # Load the cascades
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        image = cv2.flip(img, 0)
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            #Also detect smiles
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 4)
            ##for (sx, sy, sw, sh) in smiles:
                ##cv2.rectangle(roi_color, (sx, sy), ((sx + sw, sy + sh)), (255, 255, 255), 2)
                #cv2.rectangle(image, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)

        # Draw the rectangle around each face

        # Display
        cv2.imshow('img', image)

        #Read keyboard inputs for instructions. Either escape or up/down/left/right arrows
        key = cv2.waitKey(30) & 0xff

        #Exit if user presses escape key
        if key == 27:
            break

        if key == 82: #up arrow
            if tilt > -90:
                for x in range(5):
                    tilt = tilt - 1
                    print("Test loop. Current tilt: " + str(tilt))
                    time.sleep(0.005)
                    if(tilt >= -90):
                        pantilthat.tilt(tilt)

        if key == 84: #down arrow
            tilt = pantilthat.get_tilt() + 5 #Get current tilt from device and add 5 movements
            print("New move test. Current tilt: " + str(tilt))
            #if tilt < 90:
                #tilt = tilt + 5
            if(tilt <= 90): #Check to see if movement instructions will still be less than or equal to 90
                pantilthat.tilt(tilt)
            else:
                tilt = 90

        if key == 81: #left arrow
            if pan < 90:
                pan = pan + 5
                if(pan <= 90):
                    pantilthat.pan(pan)

        if key == 83: #right arrow
            if pan > -90:
                pan = pan - 5
                if(pan >= -90):
                    pantilthat.pan(pan)
                    
        # Sleep for a bit so we're not hammering the HAT with updates
        time.sleep(0.005)

    # Release the VideoCapture object
    cap.release()

if __name__ == "__main__":
    main()
