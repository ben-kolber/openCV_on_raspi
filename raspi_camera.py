# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import face_recognition
from PIL import Image

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
    face_locations = face_recognition.face_locations(image)

    # locate center of face
    count = 0
    for face_location in face_locations:
        # Print the location of each face in this image\n",
        top, right, bottom, left = face_location
        print("FACE NUM {} LOCATED".format(count))
        count += 1
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
            top, left, bottom, right))

        center_face_Y = (int)(top + ((bottom - top) / 2))
        center_face_X = (int)(left + ((right - left) / 2))

        print("located at AXIS X: {} | AXIS Y: {}".format(center_face_X, center_face_Y))
        print('-' * 30)
        print(' ' * 30)
        # draw rectangle on image \n",
        image = cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)

        # draw a rectangle around center face
        image = cv2.rectangle(image, ((center_face_X - 1), (center_face_Y - 1)),
                              ((center_face_X + 1), (center_face_Y + 1)), (0, 255, 255), 5)

    pil_image = Image.fromarray(image)
    pil_image.show()

    # using openCV
    '''
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
    '''

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
