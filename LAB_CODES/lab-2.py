import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture2.jpg")
if img is None:
    print("Image not found. Check the file path.")
    exit()
blur_img = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur_img)
cv2.imwrite("blur_image.jpg", blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
