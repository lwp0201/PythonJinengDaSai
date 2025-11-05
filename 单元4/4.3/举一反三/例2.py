# 八家美食店编号ABCDEFGH
# 近十天 旅客数量
Names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
tourists = [1210, 980, 3300, 3650, 2450, 4414, 5300, 3880]
print("八家美食店:", Names)
for i in range(7):
    for j in range(7 - i):
        if tourists[j] < tourists[j + 1]:
            tourists[j], tourists[j + 1] = tourists[j + 1], tourists[j]
            Names[j], Names[j + 1] = Names[j + 1], Names[j]
print("美食一条街近期最受欢迎店铺排名前3：")
for i in range(3):
    print(f"店铺名:{Names[i]}")
