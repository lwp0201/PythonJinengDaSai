usr = input("请输入用户名：")
password = input("密码：")
pass2 = input("随机生成码：")
if usr == "user1" and password == "123456" and pass2 == "abc123":
    print("登录成功！欢迎您的到来！")
else:
    print("用户名或密码或随机生成码错误，请重新输入")
