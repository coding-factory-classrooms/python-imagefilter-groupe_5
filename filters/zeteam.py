import cv2
import logger as lg
import os
import numpy



def ze_team(img):
    '''
    Apply our filter to an image.
    :param img: image src (image to apply the filter)
    :return: edited
    '''
    try:
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (100, 350)
        fontScale = 2
        fontColor = (255, 255, 255)
        lineType = 3
        cv2.waitKey(0)
        edited = cv2.putText(img, f'Leonard Allan Mael',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
        lg.logs(f' ZeTeam filter applied to picture')
        return edited
    except cv2.error:
        print('Error')
