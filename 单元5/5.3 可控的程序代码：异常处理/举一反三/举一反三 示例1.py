"""
📊 ================================================
    异常处理应用 - 智能成绩录入系统
================================================

📝 功能说明：
    实现一个智能的成绩录入系统
    使用异常处理机制确保数据输入的准确性和程序的稳定性
    展示了异常处理在实际应用中的重要作用

🔧 主要知识点：
    • 异常处理机制 (try-except-else)
    • 数据类型转换和验证 (float, round)
    • 条件判断和范围检查 (if-elif)
    • 循环控制 (while, continue, break)
    • 列表操作 (append)
    • 用户输入验证
    • 错误信息处理和显示

🎯 学习目标：
    掌握异常处理的基本语法和应用
    理解程序健壮性的重要性
    学会设计用户友好的输入验证
    掌握数据范围检查的方法
    理解程序流程控制技巧

💡 扩展思考：
    可以添加成绩统计分析功能
    可以保存成绩到文件
    可以添加成绩修改和删除功能
    可以生成成绩报告
    可以添加数据可视化

⚠️ 异常处理要点：
    • try块：可能出错的代码
    • except块：处理异常情况
    • else块：正常执行时的代码
    • 确保程序不会因输入错误而崩溃
"""
i=1
scorelist=[]
while True:
    try:
        score=float(input("请输入第{}位同学的成绩：".format(i)))
        score=round(score,1)
        if score==-1:
            break
        if score<0:
            print("第{}位成绩小于0，请重新录入".format(i))
            continue
        if score>100:
            print("第{}位成绩大于100，请重新录入".format(i))
            continue
    except Exception as err:
        print("第{}位成绩录入错误，请重新录入".format(i))
        print("错误原因：{}".format(err))
    else:
        scorelist.append(score)
        i = i + 1
print("当前共{}位学生，成绩列表：{}".format(i-1,scorelist))
