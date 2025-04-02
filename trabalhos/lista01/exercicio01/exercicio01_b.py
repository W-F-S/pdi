import cv2
import numpy as np


"""
letra b) aplicando Grayscale na imagem
"""

img = cv2.imread("../ImagensHDR/hw1_atrium.hdr",flags=cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("../ImagensHDR/hw1_memorial.hdr",flags=cv2.IMREAD_UNCHANGED)

#cv2.imshow('Original', img)
#cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Grayscale', gray_image)
#cv2.waitKey(0)

#cv2.destroyAllWindows()

cv2.imwrite('../ImagensHDR/hw1_atrium_grayscale.hdr', gray_image)
cv2.imwrite('../ImagensHDR/hw1_memorial_grayscale.hdr', gray_image2)
