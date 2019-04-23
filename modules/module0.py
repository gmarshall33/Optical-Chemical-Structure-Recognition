# Convert images into a standard format for the detection algorithm
# Resizing, Padding, Filtering, etc.
import cv2
# TODO create standardized image functions


def preproc_naive(filepath, scale=.25):
    img = cv2.imread(filepath)
    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    return img
