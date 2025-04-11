import cv2
import numpy as np

img = cv2.imread("../ImagensHDR/hw1_atrium.hdr",flags=cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("../ImagensHDR/hw1_memorial.hdr",flags=cv2.IMREAD_UNCHANGED)

b1, g1, r1 = cv2.split(img)
b2, g2, r2 = cv2.split(img2)

c_quad = 1
int_max = np.max(img)
img_norm = img / int_max


# s = c * log(1 + r); c = 255 / log(1 + max(r))
def transf_log(img):
    global int_max

    c = 255 / np.log(1 + int_max)
    log_img = c * np.log(1 + img)
    return np.array(log_img, dtype=np.uint8)



if __name__ == '__main__':

    log_img_b1 = transf_log(b1)
    log_img_g1 = transf_log(g1)
    log_img_r1 = transf_log(r1)

    log_img_b2 = transf_log(b2)
    log_img_g2 = transf_log(g2)
    log_img_r2 = transf_log(r2)




    cv2.imwrite('./exercicio_d/hw1_atrium_grayscale_log_transf_b1.hdr', log_img_b1)
    cv2.imwrite('./exercicio_d/hw1_atrium_grayscale_log_transf_g1.hdr', log_img_g1)
    cv2.imwrite('./exercicio_d/hw1_atrium_grayscale_log_transf_r1.hdr', log_img_r1)

    cv2.imwrite('./exercicio_d/hw1_memorial_grayscale_log_transf_b2.hdr', log_img_b2)
    cv2.imwrite('./exercicio_d/hw1_memorial_grayscale_log_transf_g2.hdr', log_img_g2)
    cv2.imwrite('./exercicio_d/hw1_memorial_grayscale_log_transf_r2.hdr', log_img_r2)
