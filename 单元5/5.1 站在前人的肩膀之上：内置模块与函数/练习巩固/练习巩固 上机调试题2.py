'''
当前有一个猜数字小程序，功能为依随机产生一个1到20之间的整数a，用户通过键盘输入整数b，如果b大于a，则提示“偏大”，
如果b小于a，则提示“偏小”，如果相同，则提示“恭喜你，猜对了！”
程序代码如下，请调试并完善相应代码。
'''
import random
a=random.randint(1,20)         # 随机生成1到20之间的整数
b=int(input("请输入整数："))
while True:
    if b>a:                          # 判断b大于a
        print("偏大")
        b = int(input("请输入整数："))   # 提示，请输入整数
    elif b<a:
        print("偏小")
        b = int(input("请输入整数："))
    else:
        print("恭喜你，猜对了！")
        break                           # 跳出循环

