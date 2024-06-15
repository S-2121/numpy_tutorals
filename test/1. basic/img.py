import cv2
import numpy as np

img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

grayscale_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale_image', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, threshold_grayscale_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold_grayscale_image', threshold_grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow('image[:100,:]', img[:100,:])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow('image[:,100:-100]', img[:,100:-100])
# cv2.waitKey(0)
# cv2.destroyAllWindows()