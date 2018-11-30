# -*- coding: utf-8 -*-

'''
安装过程曲折：
1、首先安装tesseract的时候可以提前导入中文包也就是chi-sim这个
2、安装完成后切记 配置环境变量
    * 用户的环境变量和系统的环境变量 Path中新建 你的passeract的文件夹的位置
    * 新建环境变量 ： TESSDATA_PREFIX = 'tesseract文件夹'
3、用pycharm使用pytesseract失败：
    * 打开python安装目录下的lib/site-packages/pytesseract/pytesseract.py文件
    修改 tesseract_cmd = r'E:\install\Tesseract-OCR\tesseract.exe'
'''

import pytesseract
from PIL import Image

# 打开并加载图片
image = Image.open('test.jpg')
# 调用转成字符串的方法
text = pytesseract.image_to_string(image)

print(text)


