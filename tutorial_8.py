# coding=utf-8
# @Time     :2020/5/11 0011 23:26
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_8.py
# @Software :PyCharm

import cv2 as cv
import numpy as np

# EPF 边缘保留滤波
# 高斯双边滤波
'''
def bilateralFilter(src: Any,
                    d: Any,
                    sigmaColor: Any,
                    sigmaSpace: Any,
                    dst: Any = None,
                    borderType: Any = None) -> None
'''
# 同时考虑空间和色彩
# 两个sigma，一般sigmaColor取大一点，目的是让小的差异模糊掉，把噪声去掉，
# sigmaSpace空间差异取小一点，整个核的大小就会小一点，让主要的差异保留下来
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow('bi_demo', dst)

# 均值迁移滤波
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow('bi_demo', dst)

# src = cv.imread('image/sar.png')
src = cv.imread('image/cv_data/images/example.png')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
# bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
#test git
