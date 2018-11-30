# -*- coding: utf-8 -*-

from PIL import Image
import subprocess


def cleanFile(filePath, newFilePath):
    # 获取照片
    image = Image.open(filePath)

    # 对图片进行阈值过滤（低于143为黑色，否则为白色）
    image = image.point(lambda x: 0 if x < 143 else 255)

    # 重新保存过滤后的照片
    image.save(newFilePath)

    # 调用系统的tesseract命令对图片进行ORC识别
    subprocess.call(["tesseract", newFilePath, "result"])

    # 打开文件读取的结果
    with open('result.txt', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    cleanFile('test2.jpg', r'E:\python\14_tesseract\test2clean.png')
