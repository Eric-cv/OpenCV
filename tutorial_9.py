# coding=utf-8
# @Time     :2020/5/12 0012 9:53
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_9.py
# @Software :PyCharm

from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np


# 图像的直方图
# 256是bin的大小，[0 256]是color range
# image.ravel是统计频次的函数，统计成256个bin，统计的范围是颜色[0, 255]
def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

# opencv中的api
def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        # [image]:输入图像本身；[i]：输入的通道；[256]:bin；[0, 256]:color_range
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread('image\girl.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
# plot_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()
#