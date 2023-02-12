
import cv2

path = 'Media/logoMotion.mp4'

cap = cv2.VideoCapture(path)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame= cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # 0: xaxis , 1# y axis, #-1 x y
       # frame = cv2.flip(frame,-1 )
        value = 80
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        frame = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()
