import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('einstein.tif', cv2.IMREAD_GRAYSCALE)

# Dimensões da imagem
m, n = img.shape

# Criar histograma
histograma = np.zeros(256, dtype=int)
for i in range(m):
    for j in range(n):
        histograma[img[i, j]] += 1  # Contabiliza os pixels

# Criar CDF (soma acumulada do histograma)
cdf = np.cumsum(histograma)


# Encontrar o primeiro valor não zero da CDF
cdf_min = cdf[cdf > 0].min()

# Normalizar a CDF para o intervalo [0, 255]
cdf_normalizado = ((cdf - cdf_min) / (m * n - cdf_min)) * 255

# Converter para uint8
cdf_normalizado = np.round(cdf_normalizado).astype(np.uint8)

# Aplicar a equalização na imagem
img_new = cdf_normalizado[img]

# Salvar a imagem equalizada
cv2.imwrite('equalizado.tif', img_new)

# Plotar os histogramas para ver a diferença
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
plt.title("Histograma Original")

plt.subplot(1, 2, 2)
plt.hist(img_new.ravel(), bins=256, range=(0, 256), color='red', alpha=0.7)
plt.title("Histograma Equalizado")

plt.show()
