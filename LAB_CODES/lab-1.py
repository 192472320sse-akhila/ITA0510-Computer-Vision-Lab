import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_img)
cv2.imwrite("gray_image.jpg", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
