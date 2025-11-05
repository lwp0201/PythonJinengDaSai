heights = [167, 178, 172, 180, 172, 175]  # 第1行
print(heights)  # 第2行
for i in range(6):  # 第3行
    for j in range(6 - i):  # 第4行
        if heights[j] > heights[j + 1]:  # 第5行
            heights[j], heights[j + 1] = heights[j + 1], heights[j]  # 第6行
print(heights)  # 第7行
