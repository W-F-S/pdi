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
    total_px = img.shape[0] * img.shape[1]
    cdf = np.zeros(256, dtype=int) #256 possiveis valores para cada pixel
    eq = np.zeros_like(img)


    cdf[0] = hst[0]
    for i in range(1, total_px):
        cdf[i] = cdf[i - 1] + hst[i] # frequência atual do histograma + valor acumulado anterior.

    cdf_min = 1
    for val in cdf:
        if val > 0:
            if cdf_min is None or val < cdf_min:
                cdf_min = val

    cdf_escalado = ((cdf - cdf_min) / (total_px - cdf_min)) * 255


    cdf_norm = np.round(cdf_escalado).astype(np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            eq[i,j] = cdf_norm[img[i, j]]
    return eq


def navegando(img, passos = 5):
    blocos = []
    for i in range(0, img.shape[0] - passos + 1, passos):
        for j in range(0, img.shape[1] - passos + 1, passos):
            blocos.append(img[i:i + passos, j:j + passos])

    return blocos



def reconstruir_imagem(blocos, shape, passos=5):
    # Calcula quantos blocos existem por linha e coluna
    num_blocos_linha = shape[1] // passos
    num_blocos_coluna = shape[0] // passos

    linhas_reconstruidas = []
    # Para cada linha de blocos
    for i in range(num_blocos_coluna):
        # Seleciona os blocos da linha i
        blocos_linha = blocos[i * num_blocos_linha : (i + 1) * num_blocos_linha]
        # Concatena os blocos horizontalmente para formar uma linha da imagem
        linha = np.concatenate(blocos_linha, axis=1)
        linhas_reconstruidas.append(linha)

    # Concatena todas as linhas verticalmente para reconstruir a imagem completa
    imagem_reconstruida = np.concatenate(linhas_reconstruidas, axis=0)
    return imagem_reconstruida


img1 = cv2.imread('../Fig0222(b)(cameraman).tif', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../pratica_2_1_2.png', cv2.IMREAD_GRAYSCALE)

blocos_img1_5 = navegando(img1, 5)
blocos_img2_5 = navegando(img1, 5)
blocos_img1_7 = navegando(img1, 7)
blocos_img2_7 = navegando(img1, 7)

for i in range(len(blocos_img1_5)):
    blocos_img1_5.append(qualizacao_img(blocos_img1_5[i]))

for i in range(len(blocos_img2_5)):
    blocos_img2_5.append(qualizacao_img(blocos_img2_5[i]))

for i in range(len(blocos_img1_7)):
    blocos_img1_7.append(qualizacao_img(blocos_img1_7[i]))

for i in range(len(blocos_img2_7)):
    blocos_img2_7.append(qualizacao_img(blocos_img1_7[i]))

eq_img1_5 = reconstruir_imagem(blocos_img1_5,img1.shape,5)
eq_img2_5 = reconstruir_imagem(blocos_img2_5,img2.shape,5)
eq_img1_7 = reconstruir_imagem(blocos_img1_7,img1.shape,7)
eq_img2_7 = reconstruir_imagem(blocos_img2_7,img2.shape,7)






"""
imagens não parecem diferentes, não faço ideia qual é o problema
"""
cv2.imwrite('Fig0222(b)(cameraman)_equalizada_local_5.tif', eq_img1_5)
cv2.imwrite('Fig0222(b)(cameraman)_equalizada_local_7.tif', eq_img2_5)
cv2.imwrite('pratica_2_1_2_equalizada_local_5.png', eq_img1_7)
cv2.imwrite('pratica_2_1_2_equalizada_local_7.png', eq_img2_7)


