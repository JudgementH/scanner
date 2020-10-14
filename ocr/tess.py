#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 13:26

'用pytesseract进行ocr'

__author__ = 'Judgement'

from PIL import Image
import cv2
import pytesseract

url = r"F:\bills\231.jpg"
img_origin = cv2.imread(url)
cv2.imshow('origin', img_origin)
img_median = cv2.medianBlur(img_origin, ksize=3)
cv2.imshow('median', img_median)

img = Image.open(url)
pytesseract.pytesseract.tesseract_cmd = r"E:\Program Files\Tesseract-OCR\tesseract.exe"
content = pytesseract.image_to_string(img, lang='chi_sim')
print(content)

cv2.waitKey(0)
