'''
验证答案是否正确，递归函数
f(n)=f(n-1)*2+1
f(0)=3
求f(6),f(12)
'''
def func(n):
    if n>0:
        return func(n-1)*2+1
    else:
        return 3
while True:
    n=int(input("请输入n值："))
    print("f({})的值：{}".format(n,func(n)))

# 其他：尽量不讲解斐波那契数列，因为学生听不懂，阶乘算法