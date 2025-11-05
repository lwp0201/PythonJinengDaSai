'''
下列2段代码是用于统计体质测试过程中班级前十位学生引体向上的个数，请输入到计算机中，
运行并观察输出的结果，思考这两段代码的作用及其区别
'''
# 代码段1
sportnums=[12,0,6,23,9,16,2,8,5,10]                 # 学生引体向上的个数
total=0
for i in sportnums:
    total=total+i
print("引体向上总数：{}".format(total))
# 代码段2
sportnums=[12,0,6,23,9,16,2,8,5,10]        # 总学生引体向上的个数
total=sum(sportnums)
print("引体向上总数：{}".format(total))

# 运行后，屏幕输出为：
# 引体向上总数：91
# 引体向上总数：91