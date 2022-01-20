import cv2
import numpy as numpy

img = cv2.imread('imprimir.PNG', cv2.IMREAD_COLOR)

cv2.namedWindow('Hello Word')
cv2.imshow('Hello Word', img)
cv2.waitKey()