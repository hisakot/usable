import numpy as np
import math

GAZE_CSV = "./gaze.csv"
INF_GAZE_CSV1_3 = "./gaze1_hand_resnet_3ch.csv"
INF_GAZE_CSV1_1 = "./gaze1_hand_resnet_1ch.csv"
INF_GAZE_CSV3 = "./gaze3_tool_resnet.csv"
INF_GAZE_CSV5 = "./gaze5_hand_tool_resnet.csv"
INF_GAZE_CSV7 = "./gaze7_multi_tool_resnet.csv"
MR_SATO_GAZE = "./MrSato_gaze.csv"

def calc(gt, inf):
    gaze_points = np.loadtxt(gt, delimiter=",", skiprows=1, usecols=(1, 2))
    inf_gaze_points = np.loadtxt(inf, delimiter=",")

    diff = 0
    n = 0
    for i, gaze_point in enumerate(gaze_points):
        if gaze_point[0] == 0 and gaze_point[1] == 0:
            continue
        dx2 = (gaze_point[0] - inf_gaze_points[i][0])**2 #* 256 / 337
        dy2 = (gaze_point[1] - inf_gaze_points[i][1])**2 #* 81 / 337

        diff += dx2 + dy2
        n += 1

    return diff / n

def mid(gt):
    gaze_points = np.loadtxt(gt, delimiter=",", skiprows=1, usecols=(1, 2))
    diff = 0
    n = 0
    for gaze_point in gaze_points:
        if gaze_point[0] == 0 and gaze_point[1] == 0:
            continue
        dx2 = (0.5 - gaze_point[0])**2 * 256 / 337
        dy2 = (0.5 - gaze_point[1])**2 * 81 / 337
        diff += dx2 + dy2
        n += 1
    return diff / n

def aae(gt, inf):
    gaze_points = np.loadtxt(gt, delimiter=",", skiprows=1, usecols=(1, 2))
    inf_gaze_points = np.loadtxt(inf, delimiter=",")

    gaze_points *= np.array([1920, 1980])
    inf_gaze_points *= np.array([1920, 1980])

    dpp_x = 1920 / 82 # pix per deg
    dpp_y = 1080 / 52

    n = 0
    deg = 0
    for i, gaze_point in enumerate(gaze_points):
        if gaze_point[0] == 0 and gaze_point[1] == 0:
            continue
        deg_x2 = ((gaze_point[0] - inf_gaze_points[i][0]) / dpp_x) **2
        deg_y2 = ((gaze_point[1] - inf_gaze_points[i][1]) / dpp_y) **2
        deg += math.sqrt(deg_x2 + deg_y2)
        n += 1

    return deg / n



print("1 hand ResNet 3ch (Tobii-predict)  : ", calc(GAZE_CSV, INF_GAZE_CSV1_3))
print("1 hand ResNet 1ch (Tobii-predict)  : ", calc(GAZE_CSV, INF_GAZE_CSV1_1))
print("3 tool ResNet (Tobii-predict)      : ", calc(GAZE_CSV, INF_GAZE_CSV3))
print("5 hand tool ResNet (Tobii-predict) : ", calc(GAZE_CSV, INF_GAZE_CSV5))
print("7 multitool ResNet (Tobii-predict) : ", calc(GAZE_CSV, INF_GAZE_CSV7))
print("0 (Tobii-(0.5,0.5))                : ", mid(GAZE_CSV))
print("8 Mr.Sato Gaze (Tobii-predict)     : ", calc(GAZE_CSV, MR_SATO_GAZE))

print("1 hand ResNet 1ch AAE       : ", aae(GAZE_CSV, INF_GAZE_CSV1_1))
print("3 tool ResNet 1ch AAE       : ", aae(GAZE_CSV, INF_GAZE_CSV3))
print("5 hand_tool ResNet 1ch AAE  : ", aae(GAZE_CSV, INF_GAZE_CSV5))
print("7 multitool ResNet 10ch AAE : ", aae(GAZE_CSV, INF_GAZE_CSV7))
print("8 Mr.Sato Gaze AAE          : ", aae(GAZE_CSV, MR_SATO_GAZE))
