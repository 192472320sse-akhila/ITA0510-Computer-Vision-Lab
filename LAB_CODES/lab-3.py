import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture3.jpg")
if img is None:
    print("Image not found. Check the file path.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Image", edges)
cv2.imwrite("canny_output.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
