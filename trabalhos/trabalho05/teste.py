import cv2
import numpy as np
import numpy as np
import cv2
import matplotlib.pyplot as plt



    #perguntar, qual tipo de transformação aplicar quando tranformar a imagem em sinal?

def gaussian_low_pass(shape, cutoff):
    """
    Retorna uma máscara de filtro passa-baixas Gaussiano.
    shape: tupla (M, N) com dimensões da imagem
    cutoff: frequência de corte (desvio padrão)
    """
    M, N = shape
    cx, cy = M // 2, N // 2

    u = np.arange(M).reshape(-1, 1)
    v = np.arange(N).reshape(1, -1)
    D = np.sqrt((u - cx)**2 + (v - cy)**2)

    # Fórmula Gaussiana: e^(-D^2 / (2 * cutoff^2))
    H = np.exp(-(D**2) / (2 * (cutoff**2)))
    return H

# 1) Ler imagem em escala de cinza
img = cv2.imread("./Lena.tif", cv2.IMREAD_GRAYSCALE)



f = np.fft.fft2(img)
f_shift = np.fft.fftshift(f)  # desloca o zero (freq. baixa) para o centro




# 3) Criar a máscara do filtro Gaussiano
M, N = img.shape  # dimensões
cutoff = 30.0
H = gaussian_low_pass((M, N), cutoff)

# 4) Aplicar o filtro (multiplicação no domínio da frequência)
f_filtered = f_shift * H



# 5) Inverter o shift
f_inv_shift = np.fft.ifftshift(f_filtered)

# 6) Transformada Inversa para voltar ao domínio espacial
img_filtered_complex = np.fft.ifft2(f_inv_shift)
# O resultado é complexo (por causa da FFT); pegamos o módulo
img_filtered = np.abs(img_filtered_complex)

# 7) Visualizar o resultado
plt.figure()
plt.title("Imagem Original")
plt.imshow(img, cmap="gray")

plt.figure()
plt.title("Imagem Filtrada (Gaussiana - cutoff=30)")
plt.imshow(img_filtered, cmap="gray")
plt.show()
