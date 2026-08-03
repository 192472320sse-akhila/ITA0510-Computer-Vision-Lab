import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y Edge Detection", sobely)
cv2.imwrite("Sobel_Y_Output.jpg", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
