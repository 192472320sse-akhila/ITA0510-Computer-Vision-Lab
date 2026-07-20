import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()
print("Press 's' for Slow Motion")
print("Press 'f' for Fast Motion")
print("Press 'n' for Normal Motion")
print("Press 'q' to Quit")
delay = 30   
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        break
    cv2.imshow("Webcam Video", frame)
    key = cv2.waitKey(delay) & 0xFF
    if key == ord('s'):
        delay = 100      # Slow Motion
    elif key == ord('f'):
        delay = 5        # Fast Motion
    elif key == ord('n'):
        delay = 30       # Normal Motion
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
