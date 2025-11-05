"""
🎮 ================================================
    游戏开发实战 - 传统节日对对碰游戏
================================================

📝 功能说明：
    使用pygame库开发一个传统节日主题的配对消除游戏
    玩家需要点击匹配相同的节日图片来消除它们
    展示了游戏开发的核心技术和交互设计

🔧 主要知识点：
    • pygame游戏开发框架
    • 游戏窗口创建和设置
    • 图片加载和缩放处理
    • 游戏网格系统设计
    • 鼠标事件处理
    • 游戏状态管理
    • 碰撞检测算法
    • 游戏逻辑控制
    • 时间计算和显示
    • 游戏结束条件判断
    • 字体渲染和文本显示
    • 游戏循环和事件处理

🎯 学习目标：
    掌握pygame游戏开发基础
    理解游戏循环和事件处理
    学会设计游戏交互逻辑
    掌握图片处理和显示技术
    理解游戏状态管理
    学会实现游戏算法

💡 扩展思考：
    可以添加音效和背景音乐
    可以设计更多游戏关卡
    可以添加计分系统
    可以实现游戏存档功能
    可以添加多人对战模式
    可以设计更复杂的游戏规则

🎨 游戏设计要点：
    • 清晰的游戏界面设计
    • 流畅的用户交互体验
    • 合理的游戏难度设置
    • 美观的视觉效果
    • 完整的游戏流程控制

🏆 技术亮点：
    • 模块化的代码结构
    • 高效的图片管理
    • 精确的碰撞检测
    • 流畅的游戏体验
    • 完整的游戏生命周期管理
"""

import pygame
import sys
import os
import random
import time
pygame.init()
screenWidth, screenHeight = 800, 800
# 创建一个	800x800的窗口
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("传统节日对对碰")  # 设置窗口标题

bgcolor = (199, 224, 203)  # 定义背景色

# 获取图片路径并加载图片
imageFolder = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.3 festival\images'
tileSize = 200 #图片的大小200像素
# 为组1创建图片路径列表，图片命名为 'imageA1.png',  ... 'imageA8.png'



imagePathsGroup1 = []
for i in range(8):
    #通过循环生成图片路径
    imagePath = os.path.join(imageFolder, f'imageA{i + 1}.png')
    # 将路径加入到imagePathsGroup1列表中
    imagePathsGroup1.append(imagePath)

# 从组1中加载图片并调整为指定的tile大小
imagesGroup1 = []
for imgPath in imagePathsGroup1:
    image = pygame.image.load(imgPath)  # 加载图片
    # 调整图片大小
    scaledImage = pygame.transform.scale(image, (tileSize, tileSize))    		# 将调整后的图片添加到imagesGroup1列表中
    imagesGroup1.append(scaledImage)


imagePathsGroup2 = []
for i in range(8):
    #通过循环生成图片路径
    imagePath = os.path.join(imageFolder, f'imageB{i + 1}.png')
    # 将路径加入到imagePathsGroup1列表中
    imagePathsGroup2.append(imagePath)

# 从组1中加载图片并调整为指定的tile大小
imagesGroup2 = []
for imgPath in imagePathsGroup2:
    image = pygame.image.load(imgPath)  # 加载图片
    # 调整图片大小
    scaledImage = pygame.transform.scale(image, (tileSize, tileSize))    		# 将调整后的图片添加到imagesGroup1列表中
    imagesGroup2.append(scaledImage)


# 创建图片配对
imagePairs = []  # 用于存放配对的图片
for img1, img2 in zip(imagesGroup1, imagesGroup2):
    # 将组1的图片与组2的图片配对，并添加到 imagePairs 列表
    imagePairs.append((img1, img2))

# 创建图片池，将每对配对的图片分开，同时为每张图片分配唯一的 id
imagePool = []  # 用于存放图片池
for i, pair in enumerate(imagePairs):
    img1, img2 = pair  # 解包图片对
    # 将组1的图片和其对应的 id 添加到图片池
    imagePool.append((img1, i))
    # 将组2的图片和其对应的 id 添加到图片池
    imagePool.append((img2, i))

# 检查图片池是否足够填满整个网格
gridRows, gridCols = 4, 4  # 定义网格为 4x4
totalTiles = gridRows * gridCols  # 计算网格中的总 Tile 数量
if len(imagePool) < totalTiles:
    # 如果图片池数量不足，则进行扩展
    imagePool *= (totalTiles // len(imagePool)) + 1
# 保证图片池中的图片数量等于网格总数
imagePool = imagePool[:totalTiles]
# 打乱图片池的顺序
random.shuffle(imagePool)

# 初始化空的网格列表
grid = []
# 遍历行和列，将图片按位置分配到网格中
for row in range(gridRows):  # 遍历每一行
    for col in range(gridCols):  # 遍历每一列
        # 根据行列的索引计算出要使用的图片，模运算确保图片能够循环使用
        # image = imagesGroup1[(row * gridCols + col) % len(imagesGroup1)]
        image, imageId = imagePool.pop()  # 从图片池中取出图片
        # 将图片及其计算出的坐标加入到网格列表中

        grid.append((image, imageId,(col * tileSize, row * tileSize)))
# 绘制网格，将每个图片按照计算出的坐标绘制到屏幕上2
def drawGrid():
    screen.fill(bgcolor)  # 填充背景色
    for image, imageId,position in grid:  # 遍历网格中的每个图片
        if image is not None:  # 确保图片不为空
            screen.blit(image, position)  # 将图片绘制到指定的位置

# 处理用户输入事件
def handleEvents(grid, selected):
    for event in pygame.event.get():  # 遍历所有用户输入事件
        if event.type == pygame.QUIT:  # 处理退出事件
            return False, selected  # 游戏结束
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 处理鼠标点击事件
            pos = pygame.mouse.get_pos()  # 获取鼠标点击的位置
#处理点击的图片
            selected = processMouseClick(grid, pos, selected)
    return True, selected  # 返回游戏继续运行的标志和当前选择状态
def processMouseClick(grid, pos, selected):
    """
    处理鼠标点击事件，并执行图片匹配逻辑。
    参数:
    - grid: 当前游戏网格，包含所有图片及其位置的信息
    - pos: 鼠标点击的屏幕坐标 (x, y)
    - selected: 当前已选中的图片索引，如果为 None 则表示没有选中的图片
    返回:
    - selected: 返回已选择的图片索引，如果点击匹配则返回 None
    """
    # 遍历网格中的每个图片
    for index, (image, id, (x, y)) in enumerate(grid):
        # 检查鼠标点击是否在图片范围内
        if image and x <= pos[0] <= x + tileSize and y <= pos[1] <= y + tileSize:
            if selected is None:
                return index  # 记录第一次点击的图片索引
            else:
                # 检查是否点击的是不同图片且匹配
                if selected != index and grid[selected][1] == grid[index][1]:
                    # 移除匹配成功的图片
                    grid[selected] = (None, grid[selected][1], grid[selected][2])
                    grid[index] = (None, grid[index][1], grid[index][2])
                return None  # 重置选中的图片
    return selected

def allMatched(grid):
    """
    检查网格中是否所有图片都已匹配
    """
    for image, imageId, position in grid:
        if image is not None:  # 如果有图片未被匹配，则返回 False
            return False
    return True  # 如果所有图片均为 None，表示匹配完成

def displayWinMessage(elapsedTime):
    font = pygame.font.SysFont('SimHei', 58)  # 使用系统字体“SimHei”，字体大小为58
    text = font.render("恭喜通关", True, (255, 0, 0))  # 渲染显示“恭喜通关”字样，颜色为红色
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2))  # 将文字显示在屏幕中央
    # 显示完成时间
    timeText = font.render(f"时间: {elapsedTime:.2f} 秒", True, (255, 0, 0))
    screen.blit(timeText, (screenWidth // 2 - timeText.get_width() // 2, screenHeight // 2 + 50))
def checkWinCondition(grid, startTime, elapsedTime):
    # 如果所有图片都已匹配
    if allMatched(grid):
        if elapsedTime == 0:  # 如果尚未记录时间
            elapsedTime = time.time() - startTime  # 计算经过的时间
        displayWinMessage(elapsedTime)  # 显示胜利信息
    return elapsedTime  # 返回更新后的游戏时间
def main():
    selected=None
    running = True
    startTime = time.time()  # 记录游戏开始时间
    elapsedTime = 0  # 初始化游戏时间为0
    while running:
        drawGrid()
        # 事件检测与处理
        running, selected = handleEvents(grid, selected)  # 处理玩家输入，包括鼠标点击和退出事件
        elapsedTime = checkWinCondition(grid, startTime, elapsedTime)  # 检查游戏是否完成，并更新经过的时间

        # 检查图片池是否足够填满整个网格
        pygame.display.flip()  # 更新屏幕
    # 退出Pygame
    pygame.quit()  # 退出Pygame，释放资源
    sys.exit()  # 终止程序运行
if __name__ == "__main__":
    main()