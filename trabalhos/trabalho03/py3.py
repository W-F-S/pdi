import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('einstein.tif', cv2.IMREAD_GRAYSCALE)


histograma = {}

m, n = img.shape

for i in range(m):
    for j in range(n):
        intensidade = img[i, j]
        # Atualiza a contagem no histograma
        histograma[intensidade] = histograma.get(intensidade, 0) + 1

# Converter dicionário em listas
valores_intensidade = list(histograma.keys())
frequencias = list(histograma.values())

plt.figure()
plt.title("Histograma da Imagem")
plt.xlabel("Intensidade do Pixel")
plt.ylabel("Frequência")
plt.bar(valores_intensidade, frequencias, width=1.0)
plt.xlim([0, 255])
plt.show()

























"""

"""
