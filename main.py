from __future__ import print_function
from art import *
import cv2 as cv
import numpy as np
import argparse

def grayscale():
    image = cv.imread('data/imgs/img1.png')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Original image', image)
    cv.imshow('Gray image', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

# grayscale()

def gaussian_blur():
    image = cv.imread('data/imgs/img1.png')
    blur = cv.GaussianBlur(image,(3,3),0)
    cv.imshow('Original image', image)
    cv.imshow('Blurred image', blur)
    cv.waitKey(0)
    cv.destroyAllWindows()

# gaussian_blur()

src = None
erosion_size = 0
max_elem = 2
max_kernel_size = 21
title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
title_erosion_window = 'Erosion Demo'
title_dilation_window = 'Dilation Demo'


def main(image):
    global src
    src = cv.imread('data/imgs/img1.png')
    if src is None:
        print('Could not open or find the image: ', image)
        exit(0)
    cv.namedWindow(title_dilation_window)
    cv.createTrackbar(title_trackbar_element_shape, title_dilation_window, 0, max_elem, dilatation)
    cv.createTrackbar(title_trackbar_kernel_size, title_dilation_window, 0, max_kernel_size, dilatation)
    dilatation(0)
    cv.waitKey()


# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv.MORPH_RECT
    elif val == 1:
        return cv.MORPH_CROSS
    elif val == 2:
        return cv.MORPH_ELLIPSE

def dilatation(val):
    dilatation_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_dilation_window)
    dilation_shape = morph_shape(cv.getTrackbarPos(title_trackbar_element_shape, title_dilation_window))
    element = cv.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)
    cv.imshow(title_dilation_window, dilatation_dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()
    main(args.input)