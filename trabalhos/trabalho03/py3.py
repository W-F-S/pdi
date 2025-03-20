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



cdf = np.zeros(256, dtype=int)

cdf[0] = histograma[0]

#calculando cdf
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histograma[i] # frequência atual do histograma + valor acumulado anterior.


cdf_min=1
# menor valor diferente de zero
for i in range(len(cdf)):
    if(cdf[i] < cdf_min and cdf[i]!=0):
        cdf_min = cdf[i]

total_pixels = m * n

# Normalizando a CDF
for i in range(256):
        cdf[i] = ((cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255)


for i in range(m):
    for j in range(n):
        #print(f"{i},{j}={str(cdf[img[i, j]])}")
        img_new[i, j] = cdf[img[i, j]]

print(img_new)
cv2.imwrite('equalizado.tif', img_new)
