import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture5.jpg")
if img is None:
    print("Image not found. Check the file path.")
    exit()
kernel = np.ones((5,5), np.uint8)
eroded_img = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)
cv2.imwrite("eroded_image.jpg", eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
