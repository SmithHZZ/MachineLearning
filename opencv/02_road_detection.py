import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
img_src = cv2.imread('../images/road.jpg')
# 彩色转为灰度图像
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# 使用阈值将灰度图像转换为二值图像
_, img_bin = cv2.threshold(img_gray, 185, 255, cv2.THRESH_BINARY)
# 将二值图像取反
# img_bin = cv2.bitwise_not(img_bin)

_, contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    ratio = w / h
    if 100 < contours[i].size < 275 and ratio < 2.5:

        # 计算剩下的线的斜率，画出连线
        data = contours[i]

        jmi = 0
        mi = 10000000
        jma = 0
        ma = 0

        for j in range(len(data)):
            if data[j][0][1] > ma:
                ma = data[j][0][1]
                jma = j
            if data[j][0][0] < mi:
                mi = data[j][0][1]
                jmi = j

        cv2.line(img_src, (data[jma][0][0], data[jma][0][1]), (data[jmi][0][0], data[jmi][0][1]), (0, 0, 255), 10)

        # cv2.drawContours(img_src, contours, i, (0, 0, 255), -1)

cv2.imshow("img_src", img_src)

cv2.waitKey(0)


