lst1 = [i for i in range(1, 11)]
for k in range(10):
    lst1[k] = lst1[9 - k] * 2
print(lst1[2] + k)
