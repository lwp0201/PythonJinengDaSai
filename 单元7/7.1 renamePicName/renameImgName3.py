# -*- coding: utf-8 -*-
import os
import csv  # 导入csv模块，用于处理CSV文件

csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\studentInfo.csv'  # 定义CSV文件路径
studentInfo = {}  # 创建一个空字典，用于存储学生信息
# 读取CSV文件，提取学号、班级和姓名
with open(csvFilePath,"r",encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)  # 创建CSV读取器对象
    next(reader)  # 跳过CSV文件的标题行
    for row in reader:
        admissionTicketNumber = row[0]  # 提取学号
        className = row[1]  # 提取班级
        studentName = row[2]  # 提取姓名
        studentInfo[admissionTicketNumber] = (className, studentName)  # 将学号作为键，班级和姓名作为值存入字典

print("学号提取完成。")  # 打印提示信息，表示学号提取完成
print(studentInfo)

imageFolderPath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\imagefiles'  # 图片文件夹路径


fileNameList=[]                 # 保存照片文件名
imageFiles = os.listdir(imageFolderPath)

for fileName in imageFiles:     # 遍历所有文件
    stuCode, extension = os.path.splitext(fileName)     # 获取文件名和扩展名
    if extension.lower() in ('.jpg','.jpeg','.gif','.bmp'): # 判断是否为图片
        fileNameList.append((stuCode, extension))

print(fileNameList) #打印列表中的数据

for stuCode,extension in fileNameList:

    # 检查是否在CSV中有匹配的学号
    if stuCode in studentInfo:
        className, studentName = studentInfo[stuCode]
        # 使用班级和姓名创建新的文件名
        newName = "{}_{}{}".format(className,studentName,extension)
        # 组合旧文件的完整路径
        oldFilePath = os.path.join(imageFolderPath, stuCode+extension)
        # 组合新文件的完整路径
        newFilePath = os.path.join(imageFolderPath, newName)
        # 重命名文件
        os.rename(oldFilePath, newFilePath)

