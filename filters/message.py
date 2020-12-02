import cv2 as cv
import logger
import os
import numpy

wanted_folder = 'data/output/'

if not os.path.exists(wanted_folder):
    os.mkdir(wanted_folder)

def message(image, input_txt):
    font = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (100, 350)
    fontScale = 2
    fontColor = (255, 255, 255)
    lineType = 3
    cv.waitKey(0)
    img = cv.imread(f'data/imgs/{image}')
    txt = cv.putText(img, f'{input_txt}',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
    filename = f'{wanted_folder}{image}_txt.jpg'
    cv.imwrite(filename, txt)
    logger.logs(f'<{filename}> Successfully saved')
