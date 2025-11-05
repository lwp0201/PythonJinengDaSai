import random  # 第1行 导入随机函数库
password = ""  # 第2行
for i in range(1, 7):  # 第3行
    c = random.randint(0, 9)  # 第4行:随机生成1个0-9之间数字，存放到变量c
    password = password + str(c)  # 第5行
print("随机生成的密码为:", password)  # 第6行
