#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 13:11

'利用canny算法提取边缘'

__author__ = 'Judgement'

import cv2
import numpy as np
from perspective import transform


def getOutline(img_src):
    # 输入图像路径，返回透视后轮廓的图形数组

    img = cv2.imread(img_src)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 去噪
    blur = cv2.GaussianBlur(gray, (5, 5), sigmaX=0)
    # 二值化边缘
    binary = cv2.Canny(blur, threshold1=30, threshold2=120)

    # 腐蚀
    erode = cv2.erode(binary, kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1)))
    # 膨胀
    dilate = cv2.dilate(erode, kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))

    # 轮廓提取
    contours, hierarchy = cv2.findContours(dilate, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # 初始轮廓
    outline = cv2.multiply(img, 0)
    cv2.drawContours(outline, contours, 0, (255, 255, 255), 2)
    outline = cv2.cvtColor(outline, cv2.COLOR_RGB2GRAY)

    # 再提取
    contours, hierarchy = cv2.findContours(outline, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    outline = cv2.multiply(img, 0)
    cv2.drawContours(outline, contours, 0, (255, 255, 255), 2)

    arcLength = cv2.arcLength(contours[0], True)
    points = cv2.approxPolyDP(contours[0], 0.02 * arcLength, True)
    res = cv2.multiply(img, 0)
    points = points.reshape(4, 2)
    cv2.drawContours(res, [points], -1, (255, 255, 255), 2)
    res = transform.four_point_transform(img, points)

    return res


if __name__ == '__main__':
    outline = getOutline("../img/12.png")
    cv2.imshow("outline", outline)
    cv2.waitKey()
