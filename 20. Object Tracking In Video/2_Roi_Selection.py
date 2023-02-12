
import cv2

track_type = ['BOOSTING', 'MIL', 'KCF', 'TLD',
              'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker = cv2.legacy.TrackerBoosting_create()


path = 'Media/logoMotion.mp4'
cap = cv2.VideoCapture(path)

ret, frame = cap.read()
bbox = cv2.selectROI(frame, True)
ret = tracker.init(frame, bbox)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:

        cv2.imshow("logo Video", frame)
        cv2.waitKey(1)

    else:
        break

cap.release()

cv2.destroyAllWindows()
