import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(binary, kernel, iterations=1)
cv2.imshow("Original Binary Image", binary)
cv2.imshow("Erosion", erosion)
cv2.imwrite("Erosion_Output.jpg", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
