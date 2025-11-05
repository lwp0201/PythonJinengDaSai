s = input("请输入密码:")
x1 = 0  # 字母大写
x2 = 0  # 字母小写
x3 = 0  # 数字
x4 = 0  # 特殊字符
for char in s:
    if "A" <= char <= "Z":
        x1 = 1
    elif "a" <= char <= "z":
        x2 = 1
    elif "0" <= char <= "9":
        x3 = 1
    else:
        x4 = 1
v = x1 + x2 + x3 + x4
if v == 1:
    print("密码强度：弱")
elif v == 2:
    print("密码强度：中")
else:
    print("密码强度：强")
