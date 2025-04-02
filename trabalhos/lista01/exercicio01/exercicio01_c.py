import cv2
import numpy as np

img = cv2.imread("../ImagensHDR/hw1_atrium_grayscale.hdr",flags=cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("../ImagensHDR/hw1_memorial_grayscale.hdr",flags=cv2.IMREAD_UNCHANGED)

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

    log_img = transf_log(img)
    log_img2 = transf_log(img2)

    cv2.imwrite('../ImagensHDR/hw1_atrium_grayscale_log_transf.hdr', log_img)
    cv2.imwrite('../ImagensHDR/hw1_memorial_grayscale_log_transf.hdr', log_img2)
