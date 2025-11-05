# -*- coding: utf-8 -*-
import os

imageFolderPath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\imagefiles'  # 图片文件夹路径

fileNameList=[]                 # 保存照片文件名
imageFiles = os.listdir(imageFolderPath)

for fileName in imageFiles:     # 遍历所有文件
    stuCode, extension = os.path.splitext(fileName)     # 获取文件名和扩展名
    if extension.lower() in ('.jpg','.jpeg','.gif','.bmp'): # 判断是否为图片
        fileNameList.append((stuCode, extension))

print(fileNameList) #打印列表中的数据
