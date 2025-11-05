'''
没有异常处理的除法运算代码

'''
while True:
    a=int(input("请输入被除数a："))
    b=int(input("请输入除数b："))
    if b==0:
        print("提示：除数不可以为0")
        continue
    c=a/b
    print("{}除以{}的商是:{}".format(a,b,c))
    print("== 本次除法运算结束，开始下一题 ==")
