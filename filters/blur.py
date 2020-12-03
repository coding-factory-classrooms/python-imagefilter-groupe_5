import cv2
import logger as lg


def gaussian_blur(img, intensity):
    try:
        edited = cv2.GaussianBlur(img,(intensity,intensity),0)
        lg.logs(f'Blur filter applied to picture')
    except cv2.error:
        print('Please enter an impair value')
