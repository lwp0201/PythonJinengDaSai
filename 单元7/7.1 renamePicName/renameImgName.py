"""
📸 ================================================
    文件处理实战 - 学生照片批量重命名系统
================================================

📝 功能说明：
    实现学生照片的批量重命名功能
    根据CSV文件中的学生信息，将照片文件名从学号格式
    重命名为"班级_姓名"格式，提高文件管理的便利性

🔧 主要知识点：
    • CSV文件处理 (csv模块)
    • 文件系统操作 (os模块)
    • 字典数据结构和应用
    • 文件路径处理 (os.path)
    • 字符串操作和格式化
    • 文件扩展名处理 (splitext)
    • 文件重命名操作 (rename)
    • 模块化函数设计
    • 数据匹配和查找算法
    • 批量文件处理技术

🎯 学习目标：
    掌握CSV文件的读取和处理
    理解文件系统操作的基本方法
    学会设计批量处理程序
    掌握数据结构和算法应用
    理解文件路径和扩展名处理
    学会模块化编程设计

💡 扩展思考：
    可以添加文件备份功能
    可以支持更多图片格式
    可以添加重命名日志记录
    可以设计图形化界面
    可以添加批量预览功能
    可以支持自定义命名规则

🛠️ 技术要点：
    • 使用字典提高查找效率
    • 文件扩展名大小写不敏感处理
    • 安全的文件路径组合
    • 数据验证和错误处理
    • 模块化设计提高代码复用性

📁 处理流程：
    1. 读取CSV文件获取学生信息
    2. 扫描图片文件夹获取文件列表
    3. 匹配学号并生成新文件名
    4. 执行批量重命名操作
"""

# -*- coding: utf-8 -*-
import csv  # 导入csv模块，用于处理CSV文件
import os

csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\studentInfo.csv'  # 定义CSV文件路径
imageFolderPath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\imagefiles'  # 图片文件夹路径

def getStudentInfo(csvFilePath):
    studentInfo = {}  # 创建一个空字典，用于存储学生信息
    # 读取CSV文件，提取学号、班级和姓名
    with open(csvFilePath,"r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)  # 创建CSV读取器对象
        next(reader)  # 跳过CSV文件的标题行
        for row in reader:
            admissionTicketNumber = row[0]  # 提取学号
            className = row[1]  # 提取班级
            studentName = row[2]  # 提取姓名
            studentInfo[admissionTicketNumber] = (className, studentName)  # 将学号作为键，班级和姓名作为值存入字典
    return studentInfo

def getImageFiles(imageFolderPath):
    fileNameList=[]                 # 保存照片文件名
    imageFiles = os.listdir(imageFolderPath)

    for fileName in imageFiles:     # 遍历所有文件
        stuCode, extension = os.path.splitext(fileName)     # 获取文件名和扩展名
        if extension.lower() in ('.jpg','.jpeg','.gif','.bmp'): # 判断是否为图片
            fileNameList.append((stuCode, extension))
    return fileNameList


def renameImgName(fileNameList,studentInfo):
    for stuCode, extension in fileNameList:
        # 检查是否在CSV中有匹配的学号
        if stuCode in studentInfo:
            className, studentName = studentInfo[stuCode]
            # 使用班级和姓名创建新的文件名
            newName = "{}_{}{}".format(className, studentName, extension)
            # 组合旧文件的完整路径
            oldFilePath = os.path.join(imageFolderPath, stuCode + extension)
            # 组合新文件的完整路径
            newFilePath = os.path.join(imageFolderPath, newName)
            # 重命名文件
            os.rename(oldFilePath, newFilePath)

fileNameList=getImageFiles(imageFolderPath)
studentInfo=getStudentInfo(csvFilePath)
renameImgName(fileNameList,studentInfo)