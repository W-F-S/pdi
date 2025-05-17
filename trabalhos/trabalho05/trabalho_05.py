import cv2
import numpy as np
from scipy.signal import butter, filtfilt

# https://nehajirafe.medium.com/using-fft-to-analyse-and-cleanse-time-series-data-d0c793bb82e3
#o filtro é indicado para sinais 1-D
def butter_lowpass_filter(data, cutoff, fs, order):
    nyq = 0.5 * fs  # Frequência de Nyquist
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

img = cv2.imread("./Lena.tif", cv2.IMREAD_GRAYSCALE).astype(float)

M, N = img.shape
cutoff = 20.0  # Frequência de corte
order = 2
fs = N

#aplicando para colunas e linhas
img_lp = img.copy()
for i in range(M):
    img_lp[i, :] = butter_lowpass_filter(img[i, :], cutoff, fs, order)

for j in range(N):
    img_lp[:, j] = butter_lowpass_filter(img_lp[:, j], cutoff, fs, order)

# 4) Pós-processamento
img_lp = np.clip(img_lp, 0, 255).astype(np.uint8)

# 5) Salvar ou mostrar
cv2.imwrite("lena_lowpass_spatial.tif", img_lp)
