import cv2

img = cv2.imread("./ImagensHDR/hw1_atrium.hdr",flags=cv2.IMREAD_UNCHANGED)

cv2.imshow('Original', img)
cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
