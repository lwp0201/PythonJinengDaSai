'''
编写自定义函数，实现从列表中筛选出偶数的元素并返回只有偶数的列表。
并调用这个函数，筛选出以下三个列表中的奇数：
[4,2,1,6,5,7,9,3]
[8,2,6,5,1,2]
[6,2,4,3,1,5,7]
'''

def get_value(lst):
    lst1=[]
    for i in lst:
        if i%2==0:
            lst1.append(i)
    return lst1
print(get_value([4,2,1,6,5,7,9,3]))
print(get_value([8,2,6,5,1,2]))
print(get_value([6,2,4,3,1,5,7]))