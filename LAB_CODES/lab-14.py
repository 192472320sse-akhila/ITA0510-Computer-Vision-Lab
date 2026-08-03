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
    [0, 0],
    [350, 30],
    [50, 350],
    [300, 300]
])
H, status = cv2.findHomography(src_pts, dst_pts)
result = cv2.warpPerspective(img, H, (400, 400))
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", result)
cv2.imwrite("homography_output.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
