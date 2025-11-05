t = eval(input("请输入登机前剩余时间："))
if t > 40:
    print("您可以：喝咖啡+逛机场+候机")
elif 20 <= t <= 40:
    print("您可以：逛机场+候机")
else:
    print("您可以：候机")
