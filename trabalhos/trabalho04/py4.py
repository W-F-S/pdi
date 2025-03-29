import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
varrer a imagem para pegar a a menor

ASSUMIR f COMO INTENSIDADE DE UM DOS PÍXELS x,y DA IMAGEM

fazer
a = 255/log(1+f_max)



fazer todas essas transformacoes:
g=a * f^2
g=negativo
g=T[f(x,y)]=a * log(f+i)
g=a * (e^f - 1)
g=a * raiz(f)


"""

img = cv2.imread('sample.jpg')

#econtrando esse a
a = 255/(np.log(1 + np.max(img)))

print(a)
exit()


transformacao_log = a * np.log(1 + img)
transformacao_log = np.array(transformacao_log, dtype = np.uint8)

for i in range(m):
    for j in range(n):
        img_new[i, j] = transformacao_log[i,j]

print(img_new)
cv2.imwrite('equalizado.tif', img_new)
