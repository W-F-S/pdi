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



    cdf_escalado = ((cdf - cdf_min) / (total_px - cdf_min)) * 255
    cdf_norm = np.round(cdf_escalado).astype(np.uint8)
    eq = cdf_norm[img]
    return eq


def navegando(img):



    block_size = 5

    for i in range(0, img.shape[0] - block_size + 1, block_size):
        for j in range(0, img.shape[1] - block_size + 1, block_size):
            # Extract the 5x5 block from the image
            block = img[i:i + block_size, j:j + block_size]
            print(f"Block starting at ({i}, {j}):")
            print(block)



img1 = cv2.imread('Fig0222(b)(cameraman).tif', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('pratica_2_1_2.png', cv2.IMREAD_GRAYSCALE)



navegando(img1)
