# Introduction
Some code I wrote up for my personal robotics projects at home using OpenCV

## Path planning 
Find the borders of a path given an image of a path for autonomous robot navigation. The image is converted to grayscale, applied a Gaussian blue filter, then taken the inverse binary of the image and finally either a Sobel or Laplacian edge extraction is run. 
After that, a custom algorithm is run to define the border as X and Y coordinate points in a time efficient manner. 
Once we have X and Y coordinates of the path, a path planner find the optimal path by simply taking the center point of the defined borders. 

## Face detection
Simple face detection based on OpenCV's face detection and ageitgey/face_recognition repo. 

## Camera on Raspberry pi
Running a face detection on the raspberry pi, given a Pixy camera. 

## Acknowlegments 
ageitgey/face_recognition repo
https://opencv.org/
