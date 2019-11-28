import numpy as np
import cv2
import matplotlib.pyplot as plt
import face_recognition
from PIL import Image
import sys
import random
from matplotlib.pyplot import figure


def show(string, image):
    cv2.imshow(string, image)
    cv2.waitKey()

img = cv2.imread(
    "/Users/benjaminkolber/Desktop/Personal Programming /open_cv/pics/sample_path.png")

# get image grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply gaussian blur
gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 0)

# binary conversion using
thresh = 127
im_bw_2 = cv2.threshold(gaussian_blur, thresh, 255, cv2.THRESH_BINARY)[1]

# inverse of the binary image
inverse = cv2.bitwise_not(im_bw_2)

# sobel Line Extraction
sobelx = cv2.Sobel(inverse, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(inverse, cv2.CV_64F, 0, 1, ksize=5)
sobelxy = cv2.add(sobelx, sobely)

# Laplacian Line Extraction
laplacian = cv2.Laplacian(inverse, cv2.CV_64F, 0)

# XY coordinates
right_line = []
left_line = []
i = 0
CUTOFF = 130  # cut off top 1/3 of image pixel 322 / 922
MAX_ROWS = j = 921
MAX_COLUMNS = k = 1226

# base case -> find start of line.
L_found = False
R_found = False
for i in range(MAX_COLUMNS):
    if(not L_found):  # first left point
        i += 1
    if(laplacian[j][i] > 0 and not L_found):
        L_found = True

    if(not R_found):  # first right point
        k -= 1
    if(laplacian[j][k] > 0 and not R_found):
        R_found = True

    if (k == 0 or i == MAX_COLUMNS):
        j -= 1
    if(L_found and R_found):
        break

left_line.append([i, j])  # left border coordinates
right_line.append([k, j])  # right border coordinates
right_range = []
left_range = []

# find left line trajectory
LEFT = i
RIGHT = k  # first point where left line was found to start
iteration = 6
optimal_path = []

while (j > CUTOFF):
    found_right = False
    found_left = False

    if (laplacian[j][RIGHT] <= 0):  # Right line does not continue straight
        # search close vicinity
        RIGHT -= (int)(iteration / 2)
        for i in range(iteration):  # search close vicinity
            if (laplacian[j][RIGHT] <= 0):
                RIGHT += 1
            else:
                found_right = True
    else:
        found_right = True

    if(laplacian[j][LEFT] <= 0):  # Left line does not continue straight
        LEFT -= (int)(iteration / 2)
        for i in range(iteration):  # search close vicinity
            if(laplacian[j][LEFT] <= 0):
                LEFT += 1
            else:
                found_left = True
    else:
        found_left = True

    # check if a certain point was not found
    if (not found_left or not found_right):
        j -= 1  # move up a row
        LEFT -= (int)(iteration / 2)
        RIGHT -= (int)(iteration / 2)
    else:
        if ((RIGHT - LEFT) > 40 and j % 15 == 0):  # check if pixels belong to same line more or less
            optimal_path.append([((RIGHT + LEFT)/2), j])
            right_line.append([RIGHT, j])
            left_line.append([LEFT, j])
            right_range.append([((RIGHT + LEFT)/2 + RIGHT) / 2, j])
            left_range.append([((RIGHT + LEFT)/2 + LEFT) / 2, j])
            j -= 1
        else:
            right_line.append([RIGHT, j])
            left_line.append([LEFT, j])
            right_range.append([((RIGHT + LEFT)/2 + RIGHT) / 2, j])
            left_range.append([((RIGHT + LEFT)/2 + LEFT) / 2, j])
            j -= 1


figure(num=None, figsize=(12, 12), facecolor='w', edgecolor='k')

# plt.plot(optimal_X, optimal_Y, marker='v', color='r')
plt.plot(*zip(*right_line), marker='.', color='k', ls='')
plt.plot(*zip(*left_line), marker='.', color='k', ls='')

plt.plot(*zip(*right_range), marker='.', color='r', ls='')
plt.plot(*zip(*left_range), marker='.', color='r', ls='')

plt.plot(*zip(*optimal_path), marker='^', color='b', ls='')

plt.gca().invert_yaxis()
# plt.gca().invert_xaxis()

show('gray', gray)
show('binary', inverse)
show('laplacian', laplacian)
plt.show()
