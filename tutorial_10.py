# coding=utf-8
# @Time     :2020/5/12 0012 10:32
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_10.py
# @Software :PyCharm

import cv2 as cv
import numpy as np


# 直方图均衡化是图像增强的一个手段：调整图像对比度
# 全局的直方图均衡化
def equalHist_demo(image):
    # 直方图均衡化都是基于灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 自动调整图像的对比度，提供图像清晰度
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo', dst)


# 局部自适应直方图均衡化
def clahe_demo(image):
    # 直方图均衡化都是基于灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 局部调整图像的对比度，提高图像清晰度.clipLimit是调节对比度的参数，
    # 越大对比度越大，titleGridSize是局部窗口
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clane_demo', dst)


def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbhist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int((b / bsize)) * 16 * 16 + np.int((g / bsize)) * 16 + np.int(r / bsize)
            rgbhist[np.int(index), 0] = rgbhist[np.int(index), 0] + 1
    return rgbhist


def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴氏距离：%s, 相关性：%s, 卡方：%s ' % (match1, match2, match3))


src = cv.imread(r'image\cv_data\images\noise_rice.png')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', src)
# equalHist_demo(src)
# clahe_demo(src)

image1 = cv.imread(r'image\cv_data\images\lena.jpg')
image2 = cv.imread(r'image\cv_data\images\lena.jpg')

# image2 = cv.imread(r'image\cv_data\images\example.png')
cv.imshow('image1', image1)
cv.imshow('image2', image2)
hist_compare(image1, image2)

cv.waitKey(0)
cv.destroyAllWindows()
