import random  # 第1行

lst = [random.randint(10, 50) for i in range(10)]  # 第2行
print(lst)  # 第3行
print("从小到大排序,注意:头尾两个数不排")  # 第4行
for i in range(0, 7):  # 第5行
    for j in range(1, 8 - i):  # 第6行
        if lst[j] > lst[j + 1]:  # 第7行
            lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 第8行
print(lst)  # 第9行
