import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
src_pts = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])
dst_pts = np.float32([
    [20, 30],
    [320, 40],
    [40, 320],
    [300, 300]
])
H, mask = cv2.findHomography(src_pts, dst_pts, method=0)
result = cv2.warpPerspective(img, H, (400, 400))
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", result)
cv2.imwrite("DLT_Output.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
