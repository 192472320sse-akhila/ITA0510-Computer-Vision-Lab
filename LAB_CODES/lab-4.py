import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture4.jpg")
if img is None:
    print("Image not found. Check the file path.")
    exit()
kernel = np.ones((5,5), np.uint8)
dilated_img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_img)
cv2.imwrite("dilated_image.jpg", dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
