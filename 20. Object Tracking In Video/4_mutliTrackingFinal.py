
import cv2

track_type = ['BOOSTING', 'MIL', 'KCF', 'TLD',
              'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']


path = 'Media/twoLogoMotion.mp4'
cap = cv2.VideoCapture(path)


bboxes = []
ret, frame = cap.read()

bbox = cv2.selectROI(frame, True)
bboxes.append(bbox)
bbox = cv2.selectROI(frame, True)
bboxes.append(bbox)
print(bboxes)

# ret = tracker.init(frame, bbox)
multiTracker = cv2.legacy.MultiTracker_create()
for b in bboxes:
    tracker = cv2.legacy.TrackerMOSSE_create()
    multiTracker.add(tracker, frame, b)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        ok, box = multiTracker.update(frame)
        print(len(box))

        if ok:
            for i, b in enumerate(box):

                p1 = (int(b[0]), int(b[1]))
                p2 = (int(b[0]+b[2]), int(b[1]+b[3]))
                cv2.rectangle(frame, p1, p2, (255, 0, 80), 2, 1)

        cv2.imshow("Logo Video", frame)
        cv2.waitKey(1)

    else:
        break

cap.release()

cv2.destroyAllWindows()
