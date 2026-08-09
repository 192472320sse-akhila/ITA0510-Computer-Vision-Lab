import cv2
img1 = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture1.jpg")
img2 = cv2.imread(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\Picture2.jpg")
if img1 is None or img2 is None:
    print("Image not found")
    exit()
crop = img1[50:200, 50:200]
h, w = img2.shape[:2]
x, y = 20, 20
available_h = h - y
available_w = w - x
new_h = min(crop.shape[0], available_h)
new_w = min(crop.shape[1], available_w)
crop = cv2.resize(crop, (new_w, new_h))
img2[y:y+new_h, x:x+new_w] = crop
cv2.imshow("Cropped Image", crop)
cv2.imshow("Final Image", img2)
cv2.imwrite("Cropped_Image.jpg", crop)
cv2.imwrite("Copy_Paste_Output.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
