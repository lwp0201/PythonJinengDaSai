import random  # 第1行 导入随机函数库
password = ""  # 第2行
while len(password) < 6:  # 第3行 当前密码个数6个以下
    c = random.randint(0, 9)  # 第4行 随机生成1个0-9整数
    if str(c) not in password:  # 第5行 c不在password中
        password = password + str(c)  # 第6行 c添加到password
print("随机生成的密码为:", password)  # 第7行 输出结果
