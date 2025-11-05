# -*- coding: utf-8 -*-
import csv  # 导入csv模块，用于处理CSV文件

csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.1 renamePicName\studentInfo.csv'  # 定义CSV文件路径
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

print("学号提取完成。")  # 打印提示信息，表示学号提取完成
print(studentInfo)

