def welcome():
    print("志存高远，脚踏实地，欢迎新生！")
    print("梦想照亮未来，开启美好篇章！")
welcome()

def selectnum(n):
    for i in range(n):
        if i%2==0:
            print(i,end=",")
    print()
selectnum(21)
selectnum(35)

def add(x,y):
    z=x+y
    return z
k=add(1,2)
print(k)