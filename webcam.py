import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    exit()

while True:
    ret, frame = capture.read()
    if ret == False:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, dsize=(1300, 975))
    cv2.imshow('mirror', frame)
    cv2.moveWindow('mirror', 300, 0)
    key = cv2.waitKey(1) & 0xFF
    if key == 13:
        break

capture.release()
cv2.destroyAllWindows()
