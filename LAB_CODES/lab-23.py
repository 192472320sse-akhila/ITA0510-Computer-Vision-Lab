import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
mask = cv2.subtract(gray, blurred)
sharpened = cv2.add(gray, mask)
cv2.imshow("Original Image", gray)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Unsharp Mask", mask)
cv2.imshow("Sharpened Image", sharpened)
cv2.imwrite("Unsharp_Masking_Output.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
