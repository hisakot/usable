import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    exit()
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = capture.read()
    if ret == False:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, dsize=(1920, 1080))
    cv2.imshow('mirror', frame)
    cv2.moveWindow('mirror', 0, 0)
    key = cv2.waitKey(1) & 0xFF
    if key == 13:
        break

capture.release()
cv2.destroyAllWindows()
