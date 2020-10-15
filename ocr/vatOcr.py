#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 23:25

'针对增值税发票的识别'

__author__ = 'Judgement'

import cnocr
import cv2

from graphic import edge, grapicTool


def get_text(img, code):
    ocr = cnocr.CnOcr(name='all')
    ocr_number = cnocr.CnOcr(name='number', cand_alphabet='0123456789')
    ocr_UpperSerial = cnocr.CnOcr(name='UpperSerial',
                                  cand_alphabet='0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ')
    if code == 0:
        text = ocr.ocr_for_single_line(img)
    elif code == 1:
        text = ocr_number.ocr_for_single_line(img)
    elif code == 2:
        text = ocr_UpperSerial.ocr_for_single_line(img)
    text = "".join(text)
    text = text.replace('o', '0')
    return text


def vat_to_string(img_src):
    # 增值税发票的常量
    # 截取图片中部分区域图像-名称
    crop_range_list_name = ['发票代码', '发票号码', '开票日期',
                            '校验码', '销售方名称', '销售方纳税人识别号',
                            '销售方地址电话', '销售方开户行及账号', '价税合计',
                            '备注']

    # 截取图片中部分区域图像-坐标
    crop_range_list_data = [[1870, 40, 380, 38], [1867, 104, 380, 38], [1866, 166, 380, 50],
                            [1867, 230, 450, 50], [421, 1046, 933, 46], [419, 1091, 933, 48],
                            [420, 1145, 933, 47], [421, 1193, 933, 40], [1892, 976, 414, 48],
                            [1455, 1045, 325, 38]]

    # 截取图片中部分区域图像-使用ocr的类型，0：混合字符，1：纯数字，2：编号
    crop_range_list_type = [1, 1, 0,
                            1, 0, 2,
                            0, 0, 0,
                            0]

    img = edge.getOutline(img_src)
    img = grapicTool.resize_vat(img)

    texts = []
    for i in range(len(crop_range_list_data)):
        x, y, width, height = crop_range_list_data[i]
        crop = grapicTool.crop(img, x, y, width, height)
        text = get_text(crop, crop_range_list_type[i])
        print(text)
        texts.append(texts)

    return texts


if __name__ == '__main__':
    url = r"..\img\originImage.jpg"
    print(vat_to_string(url))
