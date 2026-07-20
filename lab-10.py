import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture3.jpg")
if img is None:
    print("Image not found.")
    exit()
rows, cols = img.shape[:2]
tx = 100   
ty = 50    
M = np.float32([[1, 0, tx],
                [0, 1, ty]])
translated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)
cv2.imwrite("translated_image.jpg", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
