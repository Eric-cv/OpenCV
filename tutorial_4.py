# coding=utf-8
# @Time     :2020/5/10 0010 22:33
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_4.py
# @Software :PyCharm


import cv2 as cv
import numpy as np


# 像素相加
def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo', dst)


# 像素相减
def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow('subtract_demo', dst)


# 像素相除
def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('divide_demo', dst)


# 像素相乘
def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('multiply_demo', dst)


# 输出三通道的均值，方差 BGR
def others(m1, m2):
    '''
    #计算均值
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)
    cv.meanStdDev()
    print(M1)  # (15.0128125, 15.0128125, 15.0128125, 0.0) BGR
    print(M2)  # (128.05269531250002, 109.60858072916668, 62.55748697916667, 0.0)  BGR
    '''
    # 同时求均值和方差
    M1, dev1 = cv.meanStdDev(m1)
    '''
    # mean 越小，该通道整体的色彩偏暗
    [[15.0128125]
    [15.0128125]
    [15.0128125]];
    # variance 越小，该通道的对比度越小
    [[58.14062149]
    [58.14062149]
    [58.14062149]]
    '''
    M2, dev2 = cv.meanStdDev(m2)
    print(M1, dev1, sep='\n')
    print(M2, dev2, sep='\n')


# 逻辑运算，与或非
# 与 0&0=1 1&1=1 0&1=0
# 或 0|0=0 1|1=1 0|1=1
# 非 ~0=1 ~1=0
def logic_demo(m1, m2):
    # 与运算
    dst = cv.bitwise_and(m1, m2)  # 只有两个都不为0的区域才会有输出
    cv.imshow('logic_demo', dst)
    # 或运算
    dst = cv.bitwise_or(m1, m2)  # 只要是非0的区域都会有输出
    cv.imshow('logic_demo', dst)
    # 非运算
    dst = cv.bitwise_not(m1)
    cv.imshow('logc_demo', dst)  # 按位取反, m 变为 255-m


# 调整对比度c和亮度度b
def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)

    '''
    def addWeighted(src1: Any,
                alpha: Any,
                src2: Any,
                beta: Any,
                gamma: Any,
                dst: Any = None,
                dtype: Any = None) -> None
    '''
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    cv.imshow('con_bri_demo', dst)


src1 = cv.imread('image\cv_data\images\linux.jpg')
src2 = cv.imread('image\cv_data\images\windows.jpg')
print(src1.shape)  # (240, 320, 3)
print(src2.shape)  # (240, 320, 3)

# cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
# cv.imshow('image1', src1)
# cv.imshow('image2', src2)

# 像素运算（加减乘除；与或非逻辑运算）
# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# others(src1, src2)
# logic_demo(src1, src2)


yifei = cv.imread('image\cv_data\images\yifei.jpg')
cv.imshow('image_yifei', yifei)
# 调整对比度1.5，对比度是把像素值的差异变大，是相乘操作
# 亮度20，亮度是把像素值像255白色靠近，是相加操作
contrast_brightness_demo(yifei, 1.5, 20)
cv.waitKey(0)
cv.destroyAllWindows()
