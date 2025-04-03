import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('einstein.tif', cv2.IMREAD_GRAYSCALE)

histograma = np.zeros(256, dtype=int)

m, n = img.shape

img_new =  np.zeros([m, n], dtype = int)

for i in range(m):
    for j in range(n):
        histograma[img[i, j]] += 1  # Contabiliza os pixels



cdf = np.zeros(256, dtype=float)

cdf[0] = histograma[0]

#calculando cdf
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histograma[i] # frequência atual do histograma + valor acumulado anterior.


cdf_min=1
cdf_min = np.min(cdf[cdf > 0])

total_pixels = m * n

for i in range(256):
        cdf[i] = ((cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255)
cdf_normalizado = np.round(cdf).astype(np.uint8)

img_new = cdf_normalizado[img]

print(img_new)
cv2.imwrite('equalizado.tif', img_new)
