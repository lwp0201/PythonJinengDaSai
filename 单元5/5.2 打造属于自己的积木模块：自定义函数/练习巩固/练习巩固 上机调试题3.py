
'''
编写自定义函数，实现输入n值，可以输出nn乘法表
'''
def cfb(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("{}*{}={:<3}".format(i,j,i*j),end="")
        print()
while True:
    n=int(input("请输入n的值："))
    cfb(n)
