# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:23:42 2019

@author: 
"""

import argparse
import cv2
import numpy as np

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    
    if center is None:
        center = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def resize(image):
    
    r = 300.0 / image.shape[1]
    dim = (300, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Resized", resized) 

    

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])


height = image.shape[0]
width = image.shape[1]

cv2.imshow("Gato", image)

cropped = image[0:int(height/2), 0:int(width/2)]
cv2.imshow("A cat's back", cropped) 


NoviImage = cv2.imread(args["image"])
NoviImage = cv2.rectangle(NoviImage, (0, 0), (int(width/2), int(height/2)),
                          (0, 255, 0), cv2.FILLED)

cv2.imshow("A cat's back", NoviImage) 

rotated = rotate(image, 180)

cv2.imshow("A rotated image", rotated)

resize(rotated)


cv2.waitKey(0)

