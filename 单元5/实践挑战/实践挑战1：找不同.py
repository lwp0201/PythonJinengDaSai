import random
def createPic(n,str1,str2):
    rani = random.randint(1,n)
    ranj = random.randint(1, n)
    for i in range(n):
        for j in range(n):
            if rani==i and ranj==j:
                print(str2,end="")
            else:
                print(str1,end="")
        print()
    return rani,ranj

print("## 开始创建找不同游戏 ##")
try:
    n=int(input("请输入n值："))
    str1=input("请输入字符1（相同的字符）：")
    str2=input("请输入字符2（不同的字符）：")
except:
    print("数据输入有误，请重新输入")
else:
    i,j=createPic(n,str1,str2)

while True:
    try:
        useri=int(input("请输入行数："))-1
        userj=int(input("请输入列数："))-1
        if useri==i and userj==j:
            print("恭喜你，找到了！")
            break
        else:
            print("找错了，请重新寻找")
    except:
        print("输入有误，请重新输入")

print("## 游戏结束 ##")




'''
找不同可以锻炼学生的xxx
解决本任务需要用到的主要知识点、技能点。
随机模块：random
自定义函数：createPic
异常处理：判断是否正确输入数据
'''