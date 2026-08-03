import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture3.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X Edge Detection", sobelx)
cv2.imwrite("Sobel_X_Output.jpg", sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
