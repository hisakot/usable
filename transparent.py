import cv2

img1 = cv2.imread('../../Pictures/Photos/kobe_kazaminoyakata.jpeg')
img2 = cv2.imread('../../Pictures/Photos/pink flag3.jpg')
img1 = cv2.resize(img1, (int(img1.shape[1] / 5), int(img1.shape[0] / 5)))

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.imshow('img2', img2)
cv2.waitKey(0)

img3 = cv2.addWeighted(img1[0:img2.shape[0], 0:img2.shape[1]], 0.5, img2, 0.5, 0)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.imwrite('./img3.jpg', img3)

img4 = cv2.addWeighted(img1[0:img2.shape[0], 0:img2.shape[1]], 0.8, img2, 0.2, 0)
cv2.imshow('img4', img4)
cv2.waitKey(0)
cv2.imwrite('./img4.jpg', img4)

img5 = cv2.addWeighted(img1[0:img2.shape[0], 0:img2.shape[1]], 0.4, img2, 0.4, 0.2)
cv2.imshow('img5', img5)
cv2.waitKey(0)
cv2.imwrite('./img5.jpg', img5)

img6 = img1.copy()
img6[0:img2.shape[0], 0:img2.shape[1]] = img3
cv2.imshow('img6', img6)
cv2.waitKey(0)
cv2.imwrite('./img6.jpg', img6)

roi = img1[0:img2.shape[0], 0:img2.shape[1]]
cv2.imshow('roi', roi)
cv2.waitKey(0)
cv2.imwrite('./roi.jpg', roi)

f_roi = cv2.bitwise_and(roi, img2)
cv2.imshow('f_roi', f_roi)
cv2.waitKey(0)
cv2.imwrite('./f_roi.jpg', f_roi)

img7 = img1.copy()
img7[0:img2.shape[0], 0:img2.shape[1]] = f_roi
cv2.imshow('img7', img7)
cv2.waitKey(0)
cv2.imwrite('./img7.jpg', img7)

cv2.destroyAllWindows()
