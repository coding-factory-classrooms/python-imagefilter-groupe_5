import cv2
import logger as lg
import os
import numpy

def dilate(img, intensity):
    try:
        kernel = numpy.ones((intensity, intensity), numpy.uint8)
        edited = cv2.dilate(img,kernel,iterations=5)
        lg.logs(f'Dilate filter applied to picture')
        return edited
    except cv2.error:
        print('Error')
