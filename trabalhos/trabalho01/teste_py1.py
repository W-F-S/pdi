import cv2
import numpy as np
from matplotlib import pyplot as plt

# Constants
CONST_X = CONST_Y = 3
KERNEL_CONST = 1 / 9

# Read image in grayscale
img = cv2.imread("Imagens/Lena.tif", cv2.IMREAD_GRAYSCALE)
assert img is not None, "File could not be read, check with os.path.exists()"

# Get image dimensions (height=y, width=x)
y, x = img.shape

# Initialize output image (8-bit grayscale)
filtered_img = np.zeros((y, x), dtype=np.uint8)

# Apply manual convolution
for i in range(1, y - 1):
    for j in range(1, x - 1):
        new_pixel = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                new_pixel += img[i + di, j + dj]

        # Normalize, clip, and convert
        filtered_img[i, j] = np.clip(new_pixel * KERNEL_CONST, 0, 255).astype(np.uint8)

# Display images
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(filtered_img, cmap='gray'), plt.title('Filtered')
plt.show()
