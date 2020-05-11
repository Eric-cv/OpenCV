# coding=utf-8
# @Time     :2020/5/11 0011 10:22
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_5.py
# @Software :PyCharm

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 使用matplotlib画图
# yifei = plt.imread('image\cv_data\images\yifei.jpg')
# plt.figure(figsize=(10, 8), dpi=80)
# plt.imshow(yifei)
# plt.show()

# 泛洪填充
def fill_color_demo(image):
    copying = image.copy()
    h, w = image.shape[:2]
    # mask必须是这样的尺寸和数据类型，泛洪填充opencv的mask规定就是这样
    mask = np.zeros([h + 2, w + 2], np.uint8)
    # (100, 100)填充起始位置; (0, 255, 255)填充颜色;
    # 填充颜色范围：
    # 最低值：当前(100, 100)这个像素的值，减去(100, 100, 100)
    # 最高值：当前(100, 100)这个像素的值，加上(50, 50, 50)
    # 填充方法：全部填充
    # 从(100, 100)像素点开始搜索全图，把填充范围内的像素点全部填充为黄色
    cv.floodFill(copying, mask, (100, 100), (0, 255, 255),
                 (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copying)

# 二值填充
def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.namedWindow('ori_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('ori_image', image)
    # 注意mask是不为1的地方才可以填充
    mask = np.ones([402, 402], np.uint8)
    mask[101:301, 101: 301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.namedWindow('fill_binary', cv.WINDOW_AUTOSIZE)
    cv.imshow('fill_binary', image)





print('Hi Python!')
src = cv.imread('image\cv_data\images\yifei.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', src)
'''
# 裁剪脸部,用numpy裁剪ROI区域
face = src[100:400, 100:400]
# cv.imshow('face', face)
# BGR2gray
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
cv.namedWindow('face2gray', cv.WINDOW_AUTOSIZE)
cv.imshow('face2gray', gray)
# gray2BGR
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.namedWindow('gray2BGR', cv.WINDOW_AUTOSIZE)
cv.imshow('gray2BGR', backface)
#
src[100:400, 100:400] = backface
cv.namedWindow('src_gray2BGR_face', cv.WINDOW_AUTOSIZE)
cv.imshow('src_gray2BGR_face', src)
'''

# fill_color_demo(src)
fill_binary()

cv.waitKey(0)
cv.destroyAllWindows()
