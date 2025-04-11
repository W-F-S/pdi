import cv2
import numpy as np

#img[i-3:i+4, j-3:j+4]  pegar a regiao 7x7

def filtro_media(img):
	m = img.shape[0]
	n = img.shape[1]


	mascara = np.ones([3, 3], dtype = int)
	mascara = mascara / 9


	img_new = np.zeros([m, n])

	for i in range(1, m-1):
		for j in range(1, n-1):
			temp = img[i-1, j-1]*mascara[0, 0] + img[i-1, j]*mascara[0, 1] + img[i-1, j + 1] * mascara[0, 2] + img[i, j-1]*mascara[1, 0] + img[i, j]*mascara[1, 1] + img[i, j + 1]*mascara[1, 2] + img[i + 1, j-1]*mascara[2, 0] + img[i + 1, j]*mascara[2, 1] + img[i + 1, j + 1]*mascara[2, 2]

			img_new[i, j]= temp

	img_new = img_new.astype(np.uint8)
	return img_new

def filtro_media_7x7(img):
    m, n = img.shape
    img_new = np.zeros((m, n), dtype=np.float32)


    mascara = np.ones((7, 7), dtype=np.float32) / 49.0


    for i in range(3, m - 3):
        for j in range(3, n - 3):
            bloco = img[i-3:i+4, j-3:j+4]
            img_new[i, j] = np.sum(bloco * mascara)


    img_new = np.clip(img_new, 0, 255).astype(np.uint8)
    return img_new



def filtro_min(img):
	m, n = img.shape
	img_new = np.zeros([m, n])
	array_tmp=[]
	min_tmp = 0

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


def filtro_min_7x7(img):
    m, n = img.shape
    img_new = np.zeros((m, n), dtype=np.uint8)

    for i in range(3, m - 3):
        for j in range(3, n - 3):
            bloco = img[i-3:i+4, j-3:j+4]
            min_tmp = np.min(bloco)
            img_new[i, j] = min_tmp

    return img_new




def filtro_mediana(img):
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
			tmp = (temp[4])

			temp = []
			#ordenar array


			img_new[i, j]= tmp


	return img_new


def filtro_mediana_7x7(img):
    m, n = img.shape
    img_new = np.zeros((m, n), dtype=np.uint8)

    for i in range(3, m - 3):
        for j in range(3, n - 3):
            bloco = img[i-3:i+4, j-3:j+4]
            mediana = np.median(bloco)
            img_new[i, j] = mediana

    return img_new


def filtro_max(img):
	m, n = img.shape
	img_new = np.zeros([m, n])
	array_tmp=[]
	min_tmp = 0

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


def filtro_max_7x7(img):
    m, n = img.shape
    img_new = np.zeros((m, n), dtype=np.uint8)

    for i in range(3, m - 3):
        for j in range(3, n - 3):
            bloco = img[i-3:i+4, j-3:j+4]
            max_tmp = np.max(bloco)
            img_new[i, j] = max_tmp

    return img_new




img = cv2.imread('img.png',cv2.IMREAD_GRAYSCALE)

out_media_3x3 = filtro_media(img)
out_media_7x7 = filtro_media_7x7(img)

out_mediana_3x3 = filtro_mediana(img)
out_mediana_7x7 = filtro_mediana_7x7(img)

out_min_3x3 = filtro_min(img)
out_min_7x7 = filtro_min_7x7(img)

out_max_3x3 = filtro_max(img)
out_max_7x7 = filtro_max_7x7(img)

cv2.imwrite('saida_media_3x3.png', out_media_3x3)
cv2.imwrite('saida_media_7x7.png', out_media_7x7)

cv2.imwrite('saida_mediana_3x3.png', out_mediana_3x3)
cv2.imwrite('saida_mediana_7x7.png', out_mediana_7x7)

cv2.imwrite('saida_min_3x3.png', out_min_3x3)
cv2.imwrite('saida_min_7x7.png', out_min_7x7)

cv2.imwrite('saida_max_3x3.png', out_max_3x3)
cv2.imwrite('saida_max_7x7.png', out_max_7x7)


