import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture4.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)
laplacian = cv2.filter2D(gray, -1, kernel)
sharpened = cv2.subtract(gray, laplacian)
cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image", sharpened)
cv2.imwrite("Laplacian_Negative_Output.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
