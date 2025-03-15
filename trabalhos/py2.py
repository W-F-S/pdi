import cv2
import numpy as np

img = cv2.imread('Imagens/Lena.tif', 0) #lendo em escala de cinza


def filtro_media(img):
	# pegando proporcoes da imagem
	m, n = img.shape

	img_new = np.zeros([m, n], dtype = int)
	temp = []

	for i in range(1, m-1):
		for j in range(1, n-1):
			temp.append(img[i-1, j-1])
			temp.append(img[i-1, j])
			temp.append(img[i-1, j+1])
			temp.append(img[i, j-1])
			temp.append(img[i, j])
			temp.append(img[i, j+1])
			temp.append(img[i+1, j-1])
			temp.append(img[i+1, j])
			temp.append(img[i+1, j+1])

			tmp = (temp[3] +  temp[4]) / 2

			temp = []

			img_new[i, j]= tmp



	img_new = img_new.astype(np.uint8)
	cv2.imwrite('out.tif', img_new)


filtro_media(img)
