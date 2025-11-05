'''
完善以下代码，实现每隔3秒输出5到12之间的随机数
'''
import random                       # 导入random模块
import time
while True:
    n=random.randint(5,12)    # 随机生成5到12之间的整数
    print(n)
    time.sleep(3)                   # 暂停3秒
