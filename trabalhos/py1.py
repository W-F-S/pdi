# Python code to read image
import numpy as np
import cv2
from matplotlib import pyplot as plt

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("Imagens/Lena.tif", cv2.IMREAD_COLOR)
assert img is not None, "file could not be read, check with os.path.exists()"


print(img)



#cv2.imshow("image", img)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

