import cv2

track_type = ['BOOSTING', 'MIL', 'KCF', 'TLD',
              'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker = cv2.legacy.TrackerMOSSE_create()


path = 'Media/logoMotion.mp4'
cap = cv2.VideoCapture(path)

ret, frame = cap.read()
bbox = cv2.selectROI(frame, True)
ret = tracker.init(frame, bbox)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        ok, bbox = tracker.update(frame)

        if ok:

            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 80), 1)

        cv2.imshow("Logo Video", frame)
        cv2.waitKey(1)

    else:
        break

cap.release()

cv2.destroyAllWindows()
