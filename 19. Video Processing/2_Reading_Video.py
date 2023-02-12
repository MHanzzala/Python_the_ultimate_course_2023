import cv2

path = 'Media/logoMotion.mp4'

cap = cv2.VideoCapture(path)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Logo Video", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()
