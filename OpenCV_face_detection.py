from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (600, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(600, 480))

# allow the camera to warmup
time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('/home/pi/haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('/home/pi/haarcascade_profileface.xml')
found = False

# capture frames from the camera
while(True):
    camera.capture(rawCapture, format="bgr", use_video_port=True)
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = rawCapture.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # last param = thershold \n",
    profiles = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(x, y, w, h))
        found = True
        image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
    if found == False:
        for (x, y, w, h) in profiles:
            print("A profile is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
                x, y, w, h))
            image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]

    cv2.imshow("Frame", image)
    found = False
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
