import cv2
import numpy as np
import matplotlib.pyplot as plt

def calc_hist(img):
    hst = np.zeros(256, dtype=int)
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            hst[img[i, j]] += 1 # contabiliza os pixels
    return hst

def plot_hist(hst, tit):
    ints = np.arange(256)
    plt.bar(ints, hst, width=1.0)
    plt.title(tit)
    plt.xlabel("Intens")
    plt.ylabel("Freq")

def qualizacao_img(img):
    hst = calc_hist(img)
    cdf = np.zeros(256, dtype=float) #erro se int
    total_px = img.shape[0] * img.shape[1]

    cdf[0] = hst[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hst[i] # frequência atual do histograma + valor acumulado anterior.
    cdf_min = None
    for val in cdf:
        if val > 0:
            if cdf_min is None or val < cdf_min:
                cdf_min = val


    cdf_norm = np.round(((cdf - cdf_min) / (total_px - cdf_min)) * 255).astype(np.uint8)
    eq = cdf_norm[img]
    return eq

img1 = cv2.imread('Fig0222(b)(cameraman).tif', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('pratica_2_1_2.png', cv2.IMREAD_GRAYSCALE)

img1_eq = qualizacao_img(img1)
img2_eq = qualizacao_img(img2)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plot_hist(calc_hist(img1), "Cam - Orig")

plt.subplot(2, 2, 2)
plot_hist(calc_hist(img1_eq), "Cam - Eq")

plt.subplot(2, 2, 3)
plot_hist(calc_hist(img2), "Prac - Orig")

plt.subplot(2, 2, 4)
plot_hist(calc_hist(img2_eq), "Prac - Eq")

plt.tight_layout()
plt.show()

cv2.imwrite('equalizado_cam.tif', img1_eq)
cv2.imwrite('equalizado_prac.png', img2_eq)
