import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
if img is None:
    print("Image not found")
    exit()
text = "MY IMAGE"
position = (30, 50)
cv2.putText(img, text, position,
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)
cv2.imshow("Watermarked Image", img)
cv2.imwrite("Watermarked_Image.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
