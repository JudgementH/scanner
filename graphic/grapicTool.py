#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 23:47

'图片处理工具'

__author__ = 'Judgement'

import cv2

from graphic import edge


def resize_vat(img):
    height, width = img.shape[:2]
    # 准增值税发票版式240mmX140mm来设定
    height_resize = 1400
    width_resize = 2400
    radio = height_resize / height
    img = cv2.resize(img, dsize=(width_resize, height_resize))
    return img


def crop(img, x, y, width, height):
    crop = img[y:y + height, x:x + width]
    return crop


if __name__ == '__main__':
    url = r"..\img\originImage.jpg"
    img = edge.getOutline(url)
    resize_vat(img)
