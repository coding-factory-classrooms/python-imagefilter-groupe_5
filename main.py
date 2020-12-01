import cv2 as cv
import logger

def grayscale():
    image = cv.imread('data/imgs/img1.png')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    filename = 'data/output/graySaved.jpg'
    cv.imwrite(filename, gray)
    logger.logs(f'<{filename}> Successfully saved')

# grayscale()

def gaussian_blur():
    image = cv.imread('data/imgs/img1.png')
    blur = cv.GaussianBlur(image,(31,31),0)
    filename = 'data/output/blurSaved.jpg'
    cv.imwrite(filename, blur)
    logger.logs(f'<{filename}> Successfully saved')

gaussian_blur()


