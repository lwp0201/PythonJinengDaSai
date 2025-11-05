try:
    a=10
    b=0
    c=10/0
except:
    print("除数不能为0")

try:
    lst1=["apple","orange"]
    lst1.insert(4,"banana")
except:
    print("数据插入错误")
else:
    print("数据插入成功")
finally:
    print(lst1)