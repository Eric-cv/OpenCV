# coding=utf-8
# @Time     :2020/5/10 0010 21:36
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_3.py
# @Software :PyCharm

import cv2 as cv
import numpy as np


def extract_object_demo():
    capture = cv.VideoCapture('Journey to the Inside.mp4')
    while True:
        ret, frame = capture.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 使用cv.inRange取hsv空间中的颜色对象，lower_hsv和upper_hsv是hsv空间颜色的范围
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        # 生成mask
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        # ret是返回值，读到帧数会返回True
        if ret == False:
            break
        cv.imshow('video', frame)
        # 显示mask
        cv.imshow('mask', mask)
        c = cv.waitKey(40)
        # 27对应的是ESC
        if c == 27:
            break


def color_space_demo(image):
    # 色彩空间相互转换API
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    cv.imshow('yuv', yuv)


print('------Hello Python-------')
src = cv.imread('image\girl.jpg')  # blue, green, red
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)

# 通道数分离
b, g, r = cv.split(src)
cv.imshow('blue', b)  # 蓝色通道，0通道是0-255;1,2通道都是0(黑色)
cv.imshow('green', g)  # 绿色通道，1通道是0-255;0,2通道都是0(黑色)
cv.imshow('red', r)  # 红色通道，2通道是0-255;0,1通道都是0(黑色)
# 通道合并
src = cv.merge([b, g, r])  # 三通道都是0-255
cv.imshow('changed image', src)

# 将最后一个通道变为0,红色通道为0
src[:, :, 2] = 0  # 2通道变为0; 0,1通道是0-255
cv.imshow('without red', src)

# 读取图像，图像颜色追踪
# extract_object_demo()

cv.waitKey(0)
cv.destroyAllWindows()
