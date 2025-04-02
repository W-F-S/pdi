import cv2
import numpy as np


"""

letra b) aplicando Grayscale na imagem


img = cv2.imread("./ImagensHDR/hw1_atrium.hdr",flags=cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("./ImagensHDR/hw1_memorial.hdr",flags=cv2.IMREAD_UNCHANGED)

#cv2.imshow('Original', img)
#cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Grayscale', gray_image)
#cv2.waitKey(0)

#cv2.destroyAllWindows()

cv2.imwrite('./ImagensHDR/hw1_atrium_grayscale.hdr', gray_image)
cv2.imwrite('./ImagensHDR/hw1_memorial_grayscale.hdr', gray_image2)
"""


"""
aplicando transformacao gama na imagem
"""
img = cv2.imread("./ImagensHDR/hw1_atrium_grayscale.hdr",flags=cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("./ImagensHDR/hw1_memorial_grayscale.hdr",flags=cv2.IMREAD_UNCHANGED)

c_quad = 1
int_max = np.max(img)
img_norm = img / int_max


# s = c * log(1 + r); c = 255 / log(1 + max(r))
def transf_log(img):
    global int_max

    c = 255 / np.log(1 + int_max)
    log_img = c * np.log(1 + img)
    return np.array(log_img, dtype=np.uint8)

# s = c * sqrt(r); c = 255 / sqrt(max(r))
def transf_sqrt(img):
    global int_max

    c = 255 / np.sqrt(int_max)
    sqrt_img = c * np.sqrt(img)
    return np.array(sqrt_img, dtype=np.uint8)


# s = c * (exp(r_norm) - 1); c = 255 / (exp(1) - 1) e r_norm = r/255.
def transf_exp(img):
    global img_norm

    c = 255 / (np.exp(1) - 1)
    exp_img = c * (np.exp(img_norm) - 1)
    return np.array(exp_img, dtype=np.uint8)

# s = ((f / F_max)^2) * 255
def transf_quad(img):
    global c_quad
    global int_max
    global img_norm

    quad_img = c_quad * (img_norm ** 2) * 255
    return np.array(quad_img, dtype=np.uint8)

# s = 255 - r
def transf_neg(img):
    neg_img = 255 - img
    return neg_img

if __name__ == '__main__':

    log_img = transf_log(img)
    sqrt_img = transf_sqrt(img)
    exp_img = transf_exp(img)
    quad_img = transf_quad(img)
    neg_img = transf_neg(img)

    cv2.imwrite('./ImagensHDR/tranformacoes/log_transf.hdr', log_img)
    cv2.imwrite('./ImagensHDR/tranformacoes/sqrt_transf.hdr', sqrt_img)
    cv2.imwrite('./ImagensHDR/tranformacoes/exp_transf.hdr', exp_img)
    cv2.imwrite('./ImagensHDR/tranformacoes/quad_transf.hdr', quad_img)
    cv2.imwrite('./ImagensHDR/tranformacoes/neg_transf.hdr', neg_img)
