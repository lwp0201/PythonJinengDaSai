"""
🥧 ================================================
    数据可视化实战 - 男女生比例饼图
================================================

📝 功能说明：
    读取CSV文件中的学生信息，统计男女生比例
    使用matplotlib库创建美观的饼图进行数据可视化
    展示了分类数据可视化的方法和技巧

🔧 主要知识点：
    • CSV文件读取和处理 (csv模块)
    • 数据统计和计数 (count)
    • matplotlib饼图绘制 (plt.pie)
    • 饼图样式设置 (explode, colors, startangle)
    • 标签和百分比显示 (labels, autopct)
    • 中文字体支持配置
    • 图表标题和保存设置
    • 数据分类和比例计算

🎯 学习目标：
    掌握饼图绘制的技巧
    理解分类数据的可视化方法
    学会设置饼图的视觉效果
    掌握数据比例的计算和显示
    理解图表美化的要点

💡 扩展思考：
    可以尝试其他分类维度（班级、年龄等）
    可以添加更多颜色和样式
    可以设计交互式饼图
    可以添加图例和说明
    可以生成多种格式的图表
    可以添加动画效果

🎨 可视化要点：
    • 选择合适的颜色搭配
    • 设置清晰的标签和百分比
    • 使用explode增加视觉层次
    • 合理设置起始角度
    • 处理中文字体显示问题
    • 保存高质量的输出文件

📈 应用场景：
    • 人口统计分析
    • 市场调研数据
    • 用户画像分析
    • 教育数据统计
"""

import csv  # 导入csv库，用于读取CSV文件
import matplotlib.pyplot as plt  # 导入matplotlib库，用于绘制图表

# 读取CSV文件
csvFilePath = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.2 dataChart\示例名单.csv'  # CSV文件路径
getGender = []  # 初始化存储性别的列表

with open(csvFilePath, "r", encoding='utf-8') as csvfile:  # 以读取模式打开CSV文件
    reader = csv.reader(csvfile)  # 创建CSV读取器对象
    next(reader)  # 跳过标题行
    for row in reader:  # 遍历CSV文件的每一行
        getGender.append(row[3])  # 将每行的第四列（性别）添加到getGender列表

# 统计男女生比例
maleCount = getGender.count('男')  # 统计男生数量
femaleCount = getGender.count('女')  # 统计女生数量

# 创建男女生比例的饼图，并标注具体数值
plt.figure(figsize=(8, 8))  # 创建一个大小为8x8英寸的图
patches, texts, autotexts = plt.pie(
    [maleCount, femaleCount],  # 使用性别数量数据创建饼图
    explode=[0.1, 0.1],  # 设置每一块离开中心的距离，使得饼图更具美观性
    labels=[f'男 {maleCount}人', f'女 {femaleCount}人'],  # 创建标签，包含性别和人数
    autopct='%1.1f%%',  # 显示百分比，保留一位小数
    startangle=140,  # 起始角度为140度
    colors=['g','b']
)
plt.rcParams['font.sans-serif']=['SimHei'] #设置中文字体
plt.title('包粽子比赛男女生比例')  # 设置图表标题
plt.savefig('包粽子比赛男女生比例.png')  # 保存图表为png文件
plt.show()  # 显示图表