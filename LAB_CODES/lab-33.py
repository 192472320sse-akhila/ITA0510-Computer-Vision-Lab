import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original Binary Image", binary)
cv2.imshow("Morphological Gradient", gradient)
cv2.imwrite("Morphological_Gradient.jpg", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
