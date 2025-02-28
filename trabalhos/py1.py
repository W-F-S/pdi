import cv2
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread("Imagens/Lena.tif", cv2.IMREAD_GRAYSCALE)
assert img is not None, "File could not be read, check with os.path.exists()"

# Get image dimensions
height, width = img.shape

# Define a 3x3 mean filter kernel (for reference)
kernel = [[1/9 for _ in range(3)] for _ in range(3)]

# Create an output image (all zeros)
filtered_img = [[0 for _ in range(width)] for _ in range(height)]

# Apply the kernel manually (excluding borders)
for i in range(1, height - 1):  # Ignore borders
    for j in range(1, width - 1):
        # Apply convolution manually
        new_pixel = 0
        for ki in range(3):
            for kj in range(3):
                # Get the corresponding image pixel
                pixel_value = img[i + ki - 1, j + kj - 1]
                # Multiply with kernel value
                new_pixel += pixel_value * kernel[ki][kj]

        # Clip pixel value to 0-255 range
        filtered_img[i][j] = int(max(0, min(255, new_pixel)))

# Convert the result back to a format OpenCV can display
filtered_img_cv2 = cv2.merge([cv2.UMat(filtered_img)])[0]

# Display the images
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(filtered_img_cv2, cmap='gray'), plt.title('Manually Filtered')
plt.show()
