import cv2
import logger as lg
import os
import numpy


def dilate(img, intensity):
    '''
    Apply a dilatation filter to an image.
    :param img: image src (image to apply the filter)
    :param intensity: a value to define the intensity of the filter (higher value = more dilatation)
    :return: edited
    '''
    try:
        kernel = numpy.ones((intensity, intensity), numpy.uint8)
        edited = cv2.dilate(img,kernel,iterations=5)
        lg.logs(f'Dilate filter applied to picture')
        return edited
    except cv2.error:
        print('Error')
