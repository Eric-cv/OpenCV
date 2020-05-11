# coding=utf-8
# @Time     :2020/5/11 0011 14:43
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_7.py
# @Software :PyCharm

import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            # random.normal(loc,scale,(size))
            # #从指定正态分布中随机抽取样本，均值为loc，标准差为scale
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.namedWindow('noise_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('noise_image', image)


print('Hi Python!')
src = cv.imread('image\girl.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)

# t1 = cv.getTickCount()
# gaussian_noise(src)
# t2 = cv.getTickCount()
# time = (t2 - t1) / cv.getTickFrequency()
# print('time consume:%s' % (time * 1000))

# 使用高斯模糊api, 卷积核size x 和标准差sigma设置一个就可以，设置一个另外一个就不会起作用
# test git
dst = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow('gauss_blur', dst)
cv.waitKey(0)
cv.destroyAllWindows()
