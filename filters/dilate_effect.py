import cv2 as cv
import logger
import os
import numpy

wanted_folder = 'data/output/'

if not os.path.exists(wanted_folder):
    os.mkdir(wanted_folder)

def dilate(image):
    kernel = numpy.ones((20, 20), numpy.uint8)
    img = cv.imread(f'data/imgs/{image}')
    blur = cv.dilate(img,kernel,iterations=5)
    filename = f'{wanted_folder}{image}_dilate.jpg'
    cv.imwrite(filename, blur)
    logger.logs(f'<{filename}> Successfully saved')
