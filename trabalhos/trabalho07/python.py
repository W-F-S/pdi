import numpy as np
import cv2

#fontes: https://msameeruddin.hashnode.dev/image-erosion-explained-in-depth-using-numpy
# https://stackoverflow.com/questions/69740199/erosion-operation-without-using-opencv
def erosao(image, structuring_element):

    if image.dtype != np.uint8:
        image = image.astype(np.uint8)


    """
        binarizando a imagem
    """
    img_height, img_width = image.shape
    binary_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(img_height):
        for j in range(img_width):
            if image[i, j] == 255:
                binary_image[i, j] = 1



    # Get dimensions of the image and structuring element
    img_height, img_width = binary_image.shape
    se_height, se_width = structuring_element.shape

    pad_h = se_height // 2
    pad_w = se_width // 2

    #pad para evitar acessar pontos fora da imagem,
    padded_image = np.pad(binary_image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=False)


    for i in range(img_height):
        for j in range(img_width):

            # criando o kernel temporário com base na imagem
            temp_kernel = padded_image[i:i + se_height, j:j + se_width]

            fits = 1
            for r in range(se_height):
                for c in range(se_width):
                    if temp_kernel[r, c] == 0: # ver se o pixel visinho é totalmente preto, se sim, encontramos a borda
                        fits = 0
                        break
                if fits == 0:
                    break

            binary_image[i, j] = fits


    return binary_image.astype(np.uint8) * 255


def dilatacao(image, structuring_element):
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)

    img_height, img_width = image.shape
    binary_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(img_height):
        for j in range(img_width):
            if image[i, j] == 255:
                binary_image[i, j] = 1


    img_height, img_width = binary_image.shape
    se_height, se_width = structuring_element.shape

    """
        encontrando meio kernel
    """
    pad_h = se_height // 2
    pad_w = se_width // 2

    padded_image = np.pad(binary_image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=False)

    for i in range(img_height):
        for j in range(img_width):
            borda = 0

            for r in range(se_height):
                for c in range(se_width):
                    #se a borda é 1, adiciona 1 ao vizinho (kernel) da borda
                    if padded_image[i + r, j + c] == 1:
                        borda = 1
                        break

                if borda == 1:
                    break

            binary_image[i, j] = borda

    return binary_image.astype(np.uint8) * 255

if __name__ == "__main__":
    image_path = "./img.png"

    input_image_raw = cv2.imread(image_path)
    input_image_gray = cv2.cvtColor(input_image_raw, cv2.COLOR_BGR2GRAY)

    size = 5
    se_square = np.ones((size, size), dtype=np.uint8)

    imagem_erosao = erosao(input_image_gray, se_square)
    imagem_dilatacao = dilatacao(input_image_gray, se_square)


    imagem_fechamento = dilatacao(imagem_erosao, se_square)
    imagem_abertura = erosao(imagem_dilatacao, se_square)



    cv2.imwrite(f'imagem_fechamento{se_square.shape[0]}x{se_square.shape[1]}.png', imagem_fechamento)
    cv2.imwrite(f'imagem_abertura_{se_square.shape[0]}x{se_square.shape[1]}.png', imagem_abertura)
