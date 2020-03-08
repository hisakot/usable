import cv2
import numpy as np

import os
import re
import time

BG_SIZE = 540
WIDTH = 120
img_dir = './flags/'
flag_list = r'[A-Z0-9]'

def ready_flags(img_files):
    fore_ground = np.zeros((len(img_files) * 70, WIDTH - 10, 3))
    fore_ground.fill(1)
    for i, img_file in enumerate(img_files):
        cap = cv2.VideoCapture(img_file)
        ret, frame = cap.read()
        f_h, f_w = frame.shape[:2]
        flag = np.zeros((f_h, f_w, 3))
        flag = frame / 255

        top = i * 70 + 10
        bottom = top + f_h
        left = 0
        right = left + f_w
        fore_ground[top:bottom, left:right, :] = flag

    return fore_ground

def raise_flags(flags_img):
    f_h, f_w = flags_img.shape[:2]

    cv2.namedWindow("sky", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("sky", WIDTH, BG_SIZE)

    for h in range(10, BG_SIZE, 10):
        back_ground = np.zeros((BG_SIZE, WIDTH, 3))
        back_ground.fill(1)
        cv2.line(back_ground, (6, 0), (6, BG_SIZE), (0, 0, 0), thickness=3)
        if h < f_h:
            back_ground[BG_SIZE - h:BG_SIZE, 10:10 + f_w, :] = flags_img[0:h, :, :]
        else:
            back_ground[BG_SIZE - h:BG_SIZE - h + f_h, 10:10 + f_w, :] = flags_img
        cv2.imshow("sky", back_ground)
        cv2.waitKey(15)
        if h % 70 == 0:
            time.sleep(1)
        if h == BG_SIZE - 10:
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == '__main__':
    words = input()
    words = words.upper()

    img_files = []
    for char in words:
        match = re.search(flag_list, char)
        if match is None:
            continue
        img_file = img_dir + char + '.gif'
        img_files.append(img_file)

    flags_img = ready_flags(img_files)
    raise_flags(flags_img)
    
