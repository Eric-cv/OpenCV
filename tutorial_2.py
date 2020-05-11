# coding=utf-8
# @Time     :2020/5/10 0010 0:10
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_2.py
# @Software :PyCharm

import cv2 as cv
import torch
import numpy as np


def access_pixels(image):
    print(type(src))  # <class 'numpy.ndarray'>
    print(image.shape)  # (500, 500, 3)
    height = image.shape[0]
    wdith = image.shape[1]
    channel = image.shape[2]
    print('width: %s, height:%s ,channnel:%s' % (height, wdith, channel))
    for row in range(height):
        for col in range(wdith):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow('pixel_demo', image)


def creat_image():
    '''
    # np.zeros初始化，黑色；np.ones*m初始化，自定义颜色(可以用fill填充)
    # 初始化三通道图像
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400])*255
    img[:, :, 1] = np.ones([400, 400]) * 255
    img[:, :, 2] = np.ones([400, 400]) * 255

    '''
    '''
    # 初始化单通道图像
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127  # 灰度图像
    # img = img * 255  # 白色图像
    # img = img * 0  # 黑色图像
    cv.imshow('new_image', img)
    cv.imwrite('./image.png', img)
    '''
    # np数组简单操作
    m1 = np.ones([3, 3], np.float32)
    # 对数组进行填充
    m1.fill(12222.388)
    print(m1)
    # reshape
    m2 = m1.reshape([1, 9])
    print(m2)
    # 自定义数组
    m3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.uint8)
    m3.fill(9)
    print(m3)


print('------Hello Python-------')
# 读取图像，cv.imread(path)
src = cv.imread('image\girl.jpg')  # blue, green, red
# tensor = torch.from_numpy(src)
# 显示图像，cv.imshow()，结合cv.namedWindow
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
creat_image()

# 测试代码运行时间，cv.getTickCount是毫秒
# t1 = cv.getTickCount()
# access_pixels(src)
# t2 = cv.getTickCount()
# cv.imshow('input_image', src)
# print('time:%s' % ((t2 - t1) / cv.getTickCount())*1000)
cv.waitKey(0)

cv.destroyAllWindows()
