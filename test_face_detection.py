import cv2
import numpy as np
import face_recognition
from PIL import Image

img = cv2.imread("/Users/benjaminkolber/Desktop/Personal Programming /open_cv/pics/face_1.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


face_cascade = cv2.CascadeClassifier(
    '/Users/benjaminkolber/Desktop/Personal Programming /open_cv/open_cv/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # last param = thershold \n",


for (x, y, w, h) in faces:
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(x, y, w, h))
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in eyes:
    #    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

cv2.imshow('img', img)

# draw a rect around face using cv2 and present image.
image = face_recognition.load_image_file(
    "/Users/benjaminkolber/Desktop/Personal Programming /open_cv/pics/face_14.jpeg")
face_locations = face_recognition.face_locations(image)

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
