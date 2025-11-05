"""
📊 ================================================
    数据可视化实战 - 班级学生数量柱状图
================================================

📝 功能说明：
    读取CSV文件中的学生信息，统计各班级学生数量
    使用matplotlib库创建美观的柱状图进行数据可视化
    展示了数据分析和可视化的完整流程

🔧 主要知识点：
    • CSV文件读取和处理 (csv模块)
    • 数据统计和计数 (count, set)
    • 字典数据结构的应用
    • matplotlib数据可视化库
    • 柱状图绘制 (plt.bar)
    • 图表样式设置 (颜色、大小、字体)
    • 中文字体支持配置
    • 图表标题和轴标签设置
    • 数据标注和文本显示
    • 图表保存和显示

🎯 学习目标：
    掌握数据可视化的基本方法
    理解matplotlib库的使用
    学会处理中文显示问题
    掌握数据统计和分析技巧
    学会设计美观的图表样式
    理解数据到图表的转换过程

💡 扩展思考：
    可以尝试其他图表类型（饼图、折线图）
    可以添加更多数据维度
    可以设计交互式图表
    可以添加数据筛选功能
    可以生成多种格式的图表
    可以添加数据趋势分析

🎨 可视化要点：
    • 选择合适的图表类型
    • 设置清晰的标题和标签
    • 使用合适的颜色和样式
    • 添加数据标注提高可读性
    • 处理中文字体显示问题
    • 保存高质量的输出文件

📈 应用场景：
    • 教育数据统计分析
    • 业务数据可视化
    • 学术研究报告
    • 管理决策支持
"""

# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt


# 读取CSV文件
csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.2 dataChart\示例名单.csv'  # CSV文件路径
getClass = []  # 初始化存储班级名称的列表

with open(csvFilePath, "r", encoding='utf-8') as csvfile:  # 以读取模式打开CSV文件
    reader = csv.reader(csvfile)  # 创建CSV读取器对象
    next(reader)  # 跳过标题行
    for row in reader:  # 遍历CSV文件中的每一行
        getClass.append(row[1])  # 将每行的第二列（班级名称）添加到getClass列表

# 统计每个班级的学生数量
classCounts = {}
for className in set(getClass):
    classCounts[className] = getClass.count(className)

print(classCounts)

# 创建显示各班级学生数量的柱状图，并标注具体数值
plt.figure(figsize=(10, 8))  # 创建一个大小为10x8英寸的图
x=classCounts.keys()      #X轴为班级名称
y=classCounts.values()    #Y轴为学生数量
plt.bar(x, y,width=0.5,color='r')  # 使用matplotlib创建柱状图
plt.rcParams['font.sans-serif']=['SimHei'] #设置中文字体
plt.title('示例名单中各班级学生数量')  # 设置图表标题
plt.xlabel('班级名称')  # 设置X轴标签
plt.ylabel('学生数量')  # 设置Y轴标签

# 在柱状图上方添加具体数值
for index, value in enumerate(classCounts.values()):  # 遍历每个班级的学生数量
    plt.text(index, value + 0.05, value, ha='center')  # 在柱状图的上方添加文本标签，显示具体数值

plt.savefig('示例名单中各班级学生数量.png')  # 保存图表为png文件
plt.show()  # 显示图表