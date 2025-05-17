import cv2 as cv
import numpy as np

# Caminho da imagem
imagem_path = "./img.png"

# Parâmetros de operação
operacao = 'erosion'  # ou 'dilation'

"""
POssíveis shapes:
        'rect': cv.MORPH_RECT,
        'cross': cv.MORPH_CROSS,
        'ellipse': cv.MORPH_ELLIPSE
"""

shape = cv.MORPH_ELLIPSE  # opções: 'rect', 'cross', 'ellipse'
kernel_size = 5  # tamanho ímpar, ex: 3, 5, 7...



src = cv.imread(imagem_path)
if src is None:
    print(f"Imagem não encontrada: {imagem_path}")
    exit(1)

"""
shape	Element shape that could be one of MorphShapes
ksize	Size of the structuring element.
anchor	Anchor position within the element. The default value (−1,−1) means that the anchor is at the center. Note that only the shape of a cross-shaped element depends on the anchor position. In other cases the anchor just regulates how much the result of the morphological operation is shifted.
"""
element = cv.getStructuringElement(shape, (kernel_size, kernel_size), (-1, -1))


result1 = cv.erode(src, element)
output_path = f"./resultado_erosao.png"
cv.imwrite(output_path, result1)

result2 = cv.dilate(src, element)
output_path = f"./resultado_dilatacao.png"
cv.imwrite(output_path, result2)
