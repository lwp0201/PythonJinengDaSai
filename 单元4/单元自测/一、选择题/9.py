lst1 = [2, 4, 5, 7, 6, 4, 2]
s = 0
for i in range(7):
    if i % 2 == 0:
        continue
    s += lst1[i]
print(s)
