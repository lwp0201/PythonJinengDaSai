"""
🎮 ================================================
    游戏开发入门 - Pygame基础窗口创建
================================================

📝 功能说明：
    使用pygame库创建基础的游戏窗口
    展示pygame的基本初始化和窗口管理
    为后续游戏开发奠定基础

🔧 主要知识点：
    • pygame库的导入和初始化
    • 游戏窗口创建和设置
    • 屏幕尺寸和标题配置
    • 颜色定义和使用
    • 游戏主循环结构
    • 事件检测和处理
    • 屏幕更新和显示
    • 程序退出和资源清理

🎯 学习目标：
    掌握pygame的基本使用方法
    理解游戏窗口的创建过程
    学会设计游戏主循环
    掌握事件处理的基本概念
    理解游戏程序的完整生命周期

💡 扩展思考：
    可以添加更多游戏元素
    可以设计用户交互功能
    可以添加音效和背景音乐
    可以创建更复杂的游戏场景
    可以添加游戏状态管理

🎨 游戏开发要点：
    • 正确的库初始化和清理
    • 合理的事件处理机制
    • 流畅的屏幕更新
    • 良好的程序结构设计
"""

import pygame  # 导入Pygame库
import sys  # 导入系统模块
# 初始化Pygame
pygame.init()
# 设置屏幕尺寸和窗口标题
screenWidth, screenHeight = 800, 800  # 定义屏幕的宽度和高度
screen = pygame.display.set_mode((screenWidth, screenHeight))  # 创建一个800x800的游戏窗口
pygame.display.set_caption("传统节日对对碰")  # 设置窗口标题
# 颜色定义
bgcolor =  (199, 224, 203) # 定义背景色
# 游戏主循环
running = True
while running:
    screen.fill(bgcolor)  # 将屏幕背景色
    # 事件检测与处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 如果点击关闭按钮，则退出游戏循环
    pygame.display.flip()  # 更新屏幕
# 退出Pygame
pygame.quit()
sys.exit()
