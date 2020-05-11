# coding=utf-8
# @Time     :2020/5/11 0011 12:20
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_6.py
# @Software :PyCharm

import cv2 as cv
import numpy as np


# 均值模糊，卷积核值都为1
def blur_demo(image):
    # (1, 3)设置blur的卷积核大小(x, y)方向，该方向上卷积核的size越大，模糊效果越强
    dst = cv.blur(image, (5, 5))
    cv.namedWindow('mean_blur_demo', cv.WINDOW_AUTOSIZE)
    cv.imshow('mean_blur_demo', dst)


# 中值模糊，对椒盐噪声去噪
def median_demo(*image):
    src = cv.imread('image/cv_data/images/lena.jpg')
    dst = cv.medianBlur(src, 5)
    cv.namedWindow('median_blur', cv.WINDOW_AUTOSIZE)
    cv.imshow('median_blur', dst)


# 自定义卷积核
def custom_blur_demo(*image):
    # 5*5的全1卷积核去卷积图像，极限状态就是25个位置全身255，这样卷积结果为255*25，为了保证不会溢出，所以除以25
    # kernel = np.ones([5, 5], np.float32) / 25
    # 1.自定义均值模糊,实际上就是9个像素都为1/9的卷积核，也就是新的像素等于其周围9个像素的
    # 最简单的权重均为1/9的加权平均值，得到均值模糊
    # kernel = np.array([[1, 1, 1], [1, 1, 1, ], [1, 1, 1]], np.float32) / 9
    # 2。自定义锐化算子，周边9个像素的权重有所不同，自己本身的权重最大，得到锐化
    kernel = np.array([[0, -1, 0], [-1, 5, -1, ], [0, -1, 0]], np.float32)
    if not image:
        image = cv.imread('image/cv_data/images/lena.jpg')
    else:
        image = cv.imread(image)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.namedWindow('custom_blur', cv.WINDOW_AUTOSIZE)
    cv.imshow('custom_blur', dst)


print('Hi Python!')
src = cv.imread('image\girl.jpg')
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', src)
# blur_demo(src)
# median_demo()
custom_blur_demo()

cv.waitKey(0)
cv.destroyAllWindows()
