# Import libraries
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import numpy as np


# reading by each frame
def detect(path):
    frame = cv2.imread(f'{path}')
    bbox, label, conf = cv.detect_common_objects(frame)  # find all common objects in frame
    output_image = draw_bbox(frame, bbox, label, conf)  # draw box above object
    cv2.imwrite(f'{path}-edited.jpg', output_image)
    width, height, channels = frame.shape
    return height, width
