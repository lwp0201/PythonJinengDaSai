lst = [23, 19, 5, 32, 18]
print(lst)
n = len(lst)  # 元素个数
for i in range(n - 1):  # 找n-1个最大值
    for j in range(n - 1 - i):  # n-1-i 对相邻元素
        if lst[j] > lst[j + 1]:  # 最后结果:前小后大
            lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换
print(lst)
