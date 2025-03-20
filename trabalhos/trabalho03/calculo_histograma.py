import cv2
import numpy as np

img = cv2.imread('einstein.tif', 0) #lendo em escala de cinza

histograma = {}


m, n = img.shape
img_new = np.zeros([m, n])
array_tmp=[]
intensidade_max = 0
intensidade_min = 255


for i in range(1, m-1):
	for j in range(1, n-1):
		tmp = int(img[i][j])
		if tmp in histograma:
			histograma[tmp] += 1
		else:
			histograma[tmp] = 1


print(histograma)
#new_img = filtro_min(img)
#new_img = new_img.astype(np.uint8)
#cv2.imwrite('min.tif', new_img)
