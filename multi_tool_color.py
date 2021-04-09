
import cv2
import numpy as np
import random

color = [[0, 255, 0], [0, 255, 255], [255, 255, 0], [80, 70, 180], [180, 40, 250], [245, 145, 50], [70, 150, 250], [50, 190, 190]]
CLASS = ["forceps", "tweezers", "electrical-scalpel", "scalpel", "hook", "syringe", "needle-holder", "pen"]

size = (440, 800, 3)

img = np.zeros(size, dtype=np.uint8)

img = cv2.rectangle(img, (0, 0), (800, 55), color[0], cv2.FILLED)
img = cv2.rectangle(img, (0, 55), (800, 110), color[1], cv2.FILLED)
img = cv2.rectangle(img, (0, 110), (800, 165), color[2], cv2.FILLED)
img = cv2.rectangle(img, (0, 165), (800, 220), color[3], cv2.FILLED)
img = cv2.rectangle(img, (0, 220), (800, 275), color[4], cv2.FILLED)
img = cv2.rectangle(img, (0, 275), (800, 330), color[5], cv2.FILLED)
img = cv2.rectangle(img, (0, 330), (800, 385), color[6], cv2.FILLED)
img = cv2.rectangle(img, (0, 385), (800, 440), color[7], cv2.FILLED)

cv2.putText(img, CLASS[0], (0, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[1], (0, 95), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[2], (0, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[3], (0, 205), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[4], (0, 260), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[5], (0, 315), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[6], (0, 370), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)
cv2.putText(img, CLASS[7], (0, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2)

cv2.imshow("img", img)
cv2.waitKey(0)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("cvt_img", img)
# cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("./multi_tool_color.png", img)
