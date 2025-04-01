import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lena.tif', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("erro ao carregar imagem")

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

    cv2.imwrite('log_transf.jpg', log_img)
    cv2.imwrite('sqrt_transf.jpg', sqrt_img)
    cv2.imwrite('exp_transf.jpg', exp_img)
    cv2.imwrite('quad_transf.jpg', quad_img)
    cv2.imwrite('neg_transf.jpg', neg_img)


