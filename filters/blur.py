import cv2 as cv
import logger
import os

wanted_folder = 'data/output/'

if not os.path.exists(wanted_folder):
    os.mkdir(wanted_folder)

def gaussian_blur(image):
    img = cv.imread(f'data/imgs/{image}')
    blur = cv.GaussianBlur(img,(87,87),0)
    filename = f'{wanted_folder}{image}_blur.jpg'
    cv.imwrite(filename, blur)
    logger.logs(f'<{filename}> Successfully saved')
