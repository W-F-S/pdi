import cv2
import numpy as np

img = cv2.imread('Lena.tif', 0) #lendo em escala de cinza

def filtro_media(img):
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





def filtro_min(img):
	m, n = img.shape
	img_new = np.zeros([m, n])
	array_tmp=[]
	min_tmp = 0

	print(img)
	for i in range(1, m-1):
		for j in range(1, n-1):
			array_tmp.append(img[i-1, j-1])
			array_tmp.append(img[i-1, j])
			array_tmp.append(img[i-1, j+1])
			array_tmp.append(img[i, j-1])
			array_tmp.append(img[i, j])
			array_tmp.append(img[i, j+1])
			array_tmp.append(img[i+1, j-1])
			array_tmp.append(img[i+1, j])
			array_tmp.append(img[i+1, j+1])

			min_tmp = min(array_tmp)
			array_tmp = []

			img_new[i, j] = min_tmp


	return img_new

def filtro_mediana(img):
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
			temp.sort()
			print(temp)
			tmp = (temp[4])

			temp = []
			#ordenar array


			img_new[i, j]= tmp


	return img_new

def filtro_max(img):
	m, n = img.shape
	img_new = np.zeros([m, n])
	array_tmp=[]
	min_tmp = 0

	print(img)
	for i in range(1, m-1):
		for j in range(1, n-1):
			array_tmp.append(img[i-1, j-1])
			array_tmp.append(img[i-1, j])
			array_tmp.append(img[i-1, j+1])
			array_tmp.append(img[i, j-1])
			array_tmp.append(img[i, j])
			array_tmp.append(img[i, j+1])
			array_tmp.append(img[i+1, j-1])
			array_tmp.append(img[i+1, j])
			array_tmp.append(img[i+1, j+1])

			min_tmp = max(array_tmp)
			array_tmp = []

			img_new[i, j] = min_tmp


	return img_new



new_img = filtro_mediana(img)
new_img = new_img.astype(np.uint8)
cv2.imwrite('mediana.tif', new_img)


new_img = filtro_max(img)
new_img = new_img.astype(np.uint8)
cv2.imwrite('max.tif', new_img)



new_img = filtro_min(img)
new_img = new_img.astype(np.uint8)
cv2.imwrite('min.tif', new_img)



