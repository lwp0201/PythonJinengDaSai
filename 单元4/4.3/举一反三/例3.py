name = [1, 2, 3, 4, 5, 6, 7]  # 充电站名称
d = [1, 0.6, 3, 2.5, 2, 1, 0.5]  # 距离
n = len(name)  # 充电站个数
for i in range(n - 1):  # 冒泡排序
    for j in range(n - 1 - i):
        if d[j] > d[j + 1]:  # 从小到大排序
            d[j], d[j + 1] = d[j + 1], d[j]  # 交换距离
            name[j], name[j + 1] = name[j + 1], name[j]  # 交换对应名称
print("离您最近的两个充电站：")
print(f"充电站：{name[0]} , 距离：{d[0]}")
print(f"充电站：{name[1]} , 距离：{d[1]}")
