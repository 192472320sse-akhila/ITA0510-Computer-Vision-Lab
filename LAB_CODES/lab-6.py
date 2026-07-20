import cv2
video = cv2.VideoCapture(r"C:\Users\Akhila\OneDrive\Desktop\ITA0510-LAB\video.mp4")
if not video.isOpened():
    print("Error opening video file")
    exit()
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    key = cv2.waitKey(30)
    if key == ord('s'):
        cv2.waitKey(100)   
    elif key == ord('f'):
        cv2.waitKey(5)     
    elif key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
