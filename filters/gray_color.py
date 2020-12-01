import cv2 as cv
import logger
import os

wanted_folder = 'data/output/'

if not os.path.exists(wanted_folder):
    os.mkdir(wanted_folder)

def grayscale(image):
    img = cv.imread(f'data/imgs/{image}')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    filename = f'{wanted_folder}{image}_grayscale.jpg'
    cv.imwrite(filename, gray)
    logger.logs(f'<{filename}> Successfully saved')