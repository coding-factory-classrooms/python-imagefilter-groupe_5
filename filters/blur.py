import cv2
import logger as lg


def gaussian_blur(img, intensity):
    '''
    Apply a blur filter to an image.
    :param img: image src (image to apply the filter)
    :param intensity: a value to define the intensity of the filter (higher value = more blur)
    :return: edited
    '''
    try:
        edited = cv2.GaussianBlur(img,(intensity,intensity),0)
        lg.logs(f'Blur filter applied to picture')
        return edited
    except cv2.error:
        print('Please select an impair value')
