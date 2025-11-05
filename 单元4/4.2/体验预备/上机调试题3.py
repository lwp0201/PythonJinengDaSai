import random  # 第1行 导入随机函数库
password = ""  # 第2行
while True:  # 第3行
    c = random.randint(0, 9)  # 第4行:随机生成1个0-9之间数字，存放到变量c
    password = password + str(c)  # 第5行
    if len(password) == 5:  # 第6行 password长度为5
        break                       #第7行
password = password + "!"  # 第8行后面加一个"!"
print("随机生成的密码为:", password)  # 第9行
