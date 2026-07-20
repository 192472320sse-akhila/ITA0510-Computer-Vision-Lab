import cv2
img = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture2.jpg")
if img is None:
    print("Image not found.")
    exit()
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)
cv2.imwrite("clockwise.jpg", clockwise)
cv2.imwrite("counter_clockwise.jpg", counter_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
