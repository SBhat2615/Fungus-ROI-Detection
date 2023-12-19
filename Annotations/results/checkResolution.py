import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

path = f'/Users/siddhartha/Desktop/PROJECTS/Fungus-ROI-Detection/Annotations/results/F005a02-1.png'

img = cv2.imread(path)

height, width, _ = img.shape
img = img[:, :(width // 2), :]
cv2.imshow('original', img)
resized_image = cv2.resize(img, (width, height*2))
cv2.imshow('resized', resized_image)
cv2.waitKey(20000)