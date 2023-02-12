import cv2


def HSVchange(frame, value, key):
    lim = 255 - value
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsvFrame)
    if key == "h":
        h[h > lim] = 255
        h[h <= lim] += value

    if key == "s":
        s[s > lim] = 255
        s[s <= lim] += value

    if key == "v":
        v[v > lim] = 255
        v[v <= lim] += value

    hsvFrame = cv2.merge((h, s, v))
    frame = cv2.cvtColor(hsvFrame, cv2.COLOR_HSV2BGR)
    return frame


path = 'Media/logoMotion.mp4'

cap = cv2.VideoCapture(path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('Media/output.mp4', fourcc, 20.0, (width, height))
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame= cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # 0: xaxis , 1# y axis, #-1 x y
        # frame = cv2.flip(frame,-1 )
        frame = HSVchange(frame, 100, "v")
        out.write(frame)

        cv2.imshow("Logo Video", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
