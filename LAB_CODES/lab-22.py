import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)
sharpened = cv2.filter2D(gray, -1, kernel)
cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image", sharpened)
cv2.imwrite("Laplacian_Positive_Output.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
