import cv2
import logger as lg
import os

def grayscale(img):
    try:
        edited = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lg.logs(f'Black and White filter applied to picture')
        return edited
    except cv2.error:
        print('Error')