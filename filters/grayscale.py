import cv2
import logger as lg
import os

def grayscale(img):
    '''
    Apply a black and white filter to an image.
    :param img: image src (image to apply the filter)
    :return: img
    '''
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lg.logs(f'Black and White filter applied to picture')
        return img
    except cv2.error:
        print('Error')