'''
斐波那契数列，又称黄金分割数列，数学家莱昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”，该数列在数学上定义为
'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
while True:
    n=int(input("请输入n值："))
    print("斐波那契数列第{}项的值：{}".format(n,fib(n)))

# def check(n):
#     if n%2==1:
#         print("奇数")
#     else:
#         print("偶数")
