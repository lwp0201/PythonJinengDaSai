import random

lst = [random.randint(10, 99) for i in range(10)]
print("排序前:", lst)
for i in range(9):
    for j in range(9 - i):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("排序后:", lst)
