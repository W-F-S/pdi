import cv2
import numpy as np

img = cv2.imread('Imagens/Lena.tif', 0) #lendo em escala de cinza

# pegando proporcoes da imagem
m, n = img.shape

# criando mascara
mascara = np.ones([3, 3], dtype = int)
mascara = mascara / 9


img_new = np.zeros([m, n])

for i in range(1, m-1):
	for j in range(1, n-1):
		temp = img[i-1, j-1]*mascara[0, 0] + img[i-1, j]*mascara[0, 1] + img[i-1, j + 1] * mascara[0, 2] + img[i, j-1]*mascara[1, 0] + img[i, j]*mascara[1, 1] + img[i, j + 1]*mascara[1, 2] + img[i + 1, j-1]*mascara[2, 0] + img[i + 1, j]*mascara[2, 1] + img[i + 1, j + 1]*mascara[2, 2]

		img_new[i, j]= temp

img_new = img_new.astype(np.uint8)
cv2.imwrite('out.tif', img_new)
