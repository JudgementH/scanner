#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 13:11

'利用canny算法提取边缘'

__author__ = 'Judgement'

import cv2

img = cv2.imread("../img/bill2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 去噪
blur = cv2.GaussianBlur(gray, (5, 5), 1)

edge = cv2.Canny(blur, 50, 150)

print(edge.shape)
cv2.imshow("canny", edge)
cv2.waitKey()
#