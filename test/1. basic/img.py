import cv2
import numpy as np

img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image[:100,:]', img[:100,:])
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image[:,100:-100]', img[:,100:-100])
cv2.waitKey(0)
cv2.destroyAllWindows()