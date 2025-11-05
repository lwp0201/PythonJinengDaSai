'''
每次考试结束，教师都需要做一次简单的成绩分析，
包括获取本次考试的最高分，最低分，平均分，前3名学生成绩和最后3名学生成绩
以下代码实现了上述功能，请输入到计算机中，运行并观察输出的结果，理解该代码的含义。
'''

def get_result(lst):
    result=[]
    result.append(max(lst))
    result.append(min(lst))
    result.append(round(sum(lst)/len(lst)))
    lst.sort()
    result.append(lst[:3])
    result.append(lst[-3:])
    return result
socre=[96,86,58,94,83,66,78,79,74,85]
r=get_result(socre)
print("最高分：{}，最低分；{}，平均分：{}".format(r[0],r[1],r[2]))
print("最低的三个分数是{}，最高的三个分数是：{}".format(r[3],r[4]))

# 在关键点拨中，讲解为什么要使用自定义函数
# 什么是自定义函数，语法格式，参数，返回值等

# 通过max函数，获取最大值，并添加到列表result中
# 通过min函数，获取最小值，并添加到列表result中
# 通过sum函数获取总分，通过len函数获取个数，通过除法运算符计算品骏，获取最小值，并添加到列表result中