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
                    if structuring_element[r, c] == 1:
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
    binary_image = np.ones(image.shape, dtype=np.uint8)
    for i in range(img_height):
        for j in range(img_width):
            if image[i, j] == 0:
                binary_image[i, j] = 0
    binary_image[2, 2] = 0

    print(binary_image)

    img_height, img_width = binary_image.shape
    se_height, se_width = structuring_element.shape

    """
        encontrando meio kernel
    """
    pad_h = se_height // 2
    pad_w = se_width // 2

    padded_image = np.pad(binary_image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=2)


    print(padded_image)

    for i in range(2, img_height):
        for j in range(2, img_width):
            borda = 0

            for r in range(se_height):
                for c in range(se_width):


                    if structuring_element[r, c] == 1:
                        #se a borda é 1, adiciona 1 ao vizinho (kernel) da borda
                        print(f"i: {i} r:{r}, j:{j} c:{c}, pixel_visto{padded_image[i + r, j + c]}, pixel_visto{padded_image[i, j]}")

                        if padded_image[i + r, j + c] == 0:
                            print("pixel ja colocado, detectando borda 1")
                            break

                        if padded_image[i + r, j + c] == 1:
                            borda = 0
                            break



                if borda == 0:
                    break
            print(binary_image)

            binary_image[i, j] = borda


    return binary_image.astype(np.uint8) * 255

if __name__ == "__main__":
    image_path = "./layer1.png"

    input_image_raw = cv2.imread(image_path)
    input_image_gray = cv2.cvtColor(input_image_raw, cv2.COLOR_BGR2GRAY)

    size = 3
    se_cross = np.zeros((size, size), dtype=np.uint8)
    se_cross[size // 2 , :] = 1
    se_cross[:, size // 2] = 1

    imagem_dilatacao = dilatacao(input_image_gray, se_cross)

    cv2.imwrite(f'imagem_abertura_{se_cross.shape[0]}x{se_cross.shape[1]}.png', imagem_dilatacao)
