import pygame
import os
import sys
import random
# 初始化 Pygame
pygame.init()

# 屏幕尺寸设置
screenWidth, screenHeight = 800, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("传统节日对对碰")

# 颜色定义
bgcolor =  (199, 224, 203)

# 图片文件夹路径和Tile大小
imageFolder = r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元7\7.3 festival\images'
tileSize = 200
gridRows, gridCols = 4, 4  # 定义网格为4行4列

# 加载图片并调整大小
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
grid = []
# 遍历行和列，将图片按位置分配到网格中
for row in range(gridRows):  # 遍历每一行
    for col in range(gridCols):  # 遍历每一列
        # 根据行列的索引计算出要使用的图片，模运算确保图片能够循环使用
        # image = imagesGroup1[(row * gridCols + col) % len(imagesGroup1)]
        image, imageId = imagePool.pop()  # 从图片池中取出图片
        # 将图片及其计算出的坐标和图片的ID值加入到网格列表中
        grid.append((image, imageId ,(col * tileSize, row * tileSize)))
# 主循环

def drawGrid():
    screen.fill(bgcolor)  # 填充背景色
    for image,imageId ,position in grid:  # 遍历网格中的每个图片
        if image is not None:  # 确保图片不为空
            screen.blit(image, position)  # 将图片绘制到指定的位置
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



running = True
selected = None

while running:
    drawGrid()
    # 事件检测与处理
    running, selected = handleEvents(grid, selected)  # 处理玩家输入，包括
    pygame.display.flip()  # 更新屏幕
# 退出Pygame
pygame.quit()
sys.exit()
