import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel_x = np.array([[-1, 0, 1],
                     [-2, 0, 2],
                     [-1, 0, 1]], dtype=np.float32)
kernel_y = np.array([[-1, -2, -1],
                     [ 0,  0,  0],
                     [ 1,  2,  1]], dtype=np.float32)
grad_x = cv2.filter2D(gray, cv2.CV_32F, kernel_x)
grad_y = cv2.filter2D(gray, cv2.CV_32F, kernel_y)
grad_x = cv2.convertScaleAbs(grad_x)
grad_y = cv2.convertScaleAbs(grad_y)
gradient = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Masking", gradient)
cv2.imwrite("Gradient_Masking_Output.jpg", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
