'''
当前有一个学生成绩统计程序，功能为依次输入学生成绩，
当输入-1时，结束输入，统计并输出最高分，最低分和平均分，
程序代码如下，请调试并完善相应代码。
'''
lst=[]
while True:
    score=int(input("请输入学生成绩："))
    lst.append(score)
    if score==-1:
        break
print("最高分为：{}".format(max(lst)))              # 输出最高分
print("最低分为：{}".format(min(lst)))              # 输出最低分
print("平均分为：{:.1f}".format(sum(lst)/len(lst))) # 输出平均分