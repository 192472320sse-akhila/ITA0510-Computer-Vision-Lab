import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
rows, cols = img.shape[:2]
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 250],
                   [300, 250]])
pts2 = np.float32([[0, 0],
                   [300, 0],
                   [0, 300],
                   [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, M, (300, 300))
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformation", result)
cv2.imwrite("perspective_output.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
