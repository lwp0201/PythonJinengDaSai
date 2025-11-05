"""
🔷 ================================================
    Turtle图形绘制进阶 - 六边形绘制
================================================

📝 功能说明：
    绘制一个填充的六边形，展示了坐标定位和正多边形绘制技巧
    包含了海龟隐藏、画笔控制等高级功能

🔧 主要知识点：
    • 海龟隐藏 (hideturtle)
    • 画笔粗细设置 (pensize)
    • 双色设置 (边框色和填充色)
    • 坐标定位 (goto)
    • 正六边形绘制 (60度转向)
    • 画笔控制 (penup, pendown)

🎯 学习目标：
    掌握正多边形的绘制方法
    学会使用坐标系统定位
    理解画笔控制的重要性
    掌握海龟图标的隐藏技巧

💡 扩展思考：
    可以尝试绘制其他正多边形
    可以修改起始位置和大小
    可以添加多个六边形组成图案
"""

import turtle
turtle.hideturtle()            # 隐藏海龟图标
turtle.pensize(8)              # 设置画笔宽度（粗细）
turtle.color("blue", "pink")   # 设置画笔颜色蓝色，填充颜色为粉色
turtle.penup()                 # 提笔
turtle.goto(-50, -50)          # 光标移到（-50，-50）坐标
turtle.pendown()               # 落笔
turtle.begin_fill()            # 开始填充
for x in range(6):             # 重复6次
    turtle.forward(100)        # 前移100像素
    turtle.left(60)            # 左转60度
turtle.end_fill()              # 结束填充
turtle.done()
