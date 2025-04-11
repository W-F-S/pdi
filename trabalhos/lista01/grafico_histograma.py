import cv2
import matplotlib.pyplot as plt

# Leitura das imagens em escala de cinza
img = cv2.imread('Fig0222(b)(cameraman).tif', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('pratica_2_1_2.png', cv2.IMREAD_GRAYSCALE)

def plot_histograma(imagem, titulo):
    # Calcula o histograma manualmente
    histograma = {}
    m, n = imagem.shape
    for i in range(m):
        for j in range(n):
            intensidade = imagem[i, j]
            histograma[intensidade] = histograma.get(intensidade, 0) + 1

    valores_intensidade = list(histograma.keys())
    frequencias = list(histograma.values())

    # Plota o histograma
    plt.bar(valores_intensidade, frequencias, width=1.0)
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")

# Cria uma figura com 2 subplots para exibir os histogramas lado a lado
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_histograma(img, "Histograma - Cameraman")

plt.subplot(1, 2, 2)
plot_histograma(img2, "Histograma - Prática 2.1.2")

plt.tight_layout()
plt.show()
