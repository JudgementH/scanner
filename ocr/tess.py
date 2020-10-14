#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 13:26

'用pytesseract进行ocr'

__author__ = 'Judgement'

from PIL import Image
import numpy as np
import cv2
import pytesseract
from edge import edge

pytesseract.pytesseract.tesseract_cmd = r"E:\Program Files\Tesseract-OCR\tesseract.exe"


def image_to_string(img_src):
    # 得到正位图形
    img = edge.getOutline(img_src)
    # 灰度
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 锐化
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    img = cv2.filter2D(img, -1, kernel=kernel)
    # 二值化
    ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    # 开
    # morphology_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # img = cv2.morphologyEx(img, cv2.MORPH_OPEN, morphology_kernel)

    img = cv2.medianBlur(img, 1)

    content = pytesseract.image_to_string(img, lang='chi_sim')
    cv2.imshow('origin', img)
    cv2.waitKey(0)
    return content


if __name__ == '__main__':
    url = r"../img/12.png"
    print(image_to_string(url))
