'''
教育局为了解学校学生的体质情况，需要随机抽查学校的1个班级进行体质检测，
以下代码实现了上述功能，请输入到计算机中，运行并观察输出的结果，理解该代码的含义
'''
import random
classlist=["1班","2班","3班","4班","5班"]
classname=random.choice(classlist)
print("体质测试班级：{}".format(classname))

# 运行后，屏幕输出为：
# 体质测试班级：3班