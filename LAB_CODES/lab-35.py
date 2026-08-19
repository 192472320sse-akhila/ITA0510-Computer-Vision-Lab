import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Black Hat", black_hat)
cv2.imwrite("Black_Hat_Output.jpg", black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
