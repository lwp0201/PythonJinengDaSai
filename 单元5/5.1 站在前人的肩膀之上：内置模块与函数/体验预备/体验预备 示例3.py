'''
以下是一个简单的秒表程序，用于记录学生50米的速度。
请完成部分代码的填空，并请输入到计算机中，运行并观察输出的结果，理解该代码的含义
'''
import time
input("预备(按任意字符表示跑步开始)")
start_time  =  time.time()#记录开始时间
input("跑步中...(按任意字符表示跑步结束)")
end_time  =  time.time()#记录结束时间
use_time = end_time - start_time
print("跑步结束，学生50米跑步所用时间：{:.2f}秒".format(use_time))

# 运行后，屏幕输出为：
# 体质测试班级：3班