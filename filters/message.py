import cv2
import logger as lg
import numpy


def message(img, input_txt):
    '''
    Add a message to display on a picture.
    :param img: image src (image to apply the filter)
    :param input_txt: a str to define the texte of the filter
    :return: edited
    '''
    try:
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (100, 350)
        fontScale = 2
        fontColor = (255, 255, 255)
        lineType = 3
        cv2 .waitKey(0)
        edited = cv2.putText(img, f'{input_txt}',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
        lg.logs(f'Message filter applied to picture')
        return edited
    except cv2.error:
        print('Error')
