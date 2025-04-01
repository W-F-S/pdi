import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('einstein.tif', cv2.IMREAD_GRAYSCALE)


histograma = {}

m, n = img.shape

for i in range(m):
    for j in range(n):
        intensidade = img[i, j]
        histograma[intensidade] = histograma.get(intensidade, 0) + 1

valores_intensidade = list(histograma.keys())
frequencias = list(histograma.values())

plt.figure()
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Frequência")
plt.bar(valores_intensidade, frequencias, width=1.0)
plt.show()

























"""

"""
