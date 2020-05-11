# coding=utf-8
# @Time     :2020/5/9 0009 23:11
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tutorial_1.py
# @Software :PyCharm

import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break

# 打印图像信息
def get_image_info(image):
    print(type(image))  # <class 'numpy.ndarray'>
    print(image.shape)  # (500, 500, 3)
    print(image.size)  # 750000
    print(image.dtype)  # uint8
    pixel_data = np.array(image)
    print(pixel_data)


print('------Hello Python-------')
# 读取图像，cv.imread(path)
src = cv.imread('image\girl.jpg')
# 显示图像，cv.imshow()，结合cv.namedWindow
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
get_image_info(src)

# 保存图像到指定路径
cv.imwrite('image\girl01.png', src)

# 保存为灰度图像
gray = cv.cvtColor(src, cv.COLOR_BAYER_BG2GRAY)
cv.imwrite('image\girl02.png', gray)

# 无限期等待输入按键
cv.waitKey(0)
# 关闭所有打开的窗口
cv.destroyAllWindows()
