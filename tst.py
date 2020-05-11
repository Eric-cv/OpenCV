# coding=utf-8
# @Time     :2020/5/9 0009 23:00
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tst.py
# @Software :PyCharm

import cv2 as cv
import numpy as np

print('Hi Python!')
src = cv.imread('image\girl.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()
