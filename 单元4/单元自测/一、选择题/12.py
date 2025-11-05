lst = [55, 24, 33, 46, 67, 88]
for i in range(5):
    for j in range(5 - i):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst[-3])
