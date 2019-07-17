#!/usr/bin/python3
import cv2

image = cv2.imread('image.jpg')  

grayimg = image
height, width, channels = image.shape

for i in range(height):  
    for j in range(width):  
        grayimg[i,j] = 0 * image[i,j][0] + 0.19 * image[i,j][1] +  0.19 * image[i,j][2]  

cv2.imshow('srcImage', image)             
cv2.imshow('grayImage', grayimg)  
cv2.waitKey(0)  
