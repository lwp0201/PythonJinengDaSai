"""
🎨 ================================================
    Turtle图形绘制进阶 - 同心圆绘制
================================================

📝 功能说明：
    绘制两个同心圆，外圆为红色，内圆为黄色
    展示了填充、画笔控制、坐标移动等高级功能

🔧 主要知识点：
    • 图形填充 (begin_fill, end_fill)
    • 画笔控制 (penup, pendown)
    • 坐标移动 (goto)
    • 多色图形绘制
    • 同心圆绘制技巧

🎯 学习目标：
    掌握turtle的填充功能
    学会控制画笔的抬起和落下
    理解坐标系统在图形绘制中的应用
    学会绘制复合图形

💡 扩展思考：
    可以尝试绘制更多层的同心圆
    可以添加不同的填充颜色
    可以绘制其他几何图形组合
"""

import turtle
turtle.color("red")          # 设置绘制第一个圆时的画笔颜色
turtle.begin_fill()          # 开始填充
turtle.circle(100)           # 绘制半径100像素的圆
turtle.end_fill()            # 结束填充
turtle.penup()               # 提笔，不做绘画
turtle.goto(0, 40)           # 光标移到(0,40)的位置
turtle.pendown()             # 落笔，可以绘画
turtle.color("yellow")       # 设置绘制第二个圆时的画笔颜色
turtle.begin_fill()          # 第二次开始填充
turtle.circle(65)            # 绘制半径65像素的圆
turtle.end_fill()            # 结束填充
turtle.done()
