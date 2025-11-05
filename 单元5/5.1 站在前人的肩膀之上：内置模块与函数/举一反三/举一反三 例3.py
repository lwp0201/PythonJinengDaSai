'''
锻炼作为一种长期性的过程，唯有持之以恒，方能收获持久的效果。
如果三天打鱼两天晒网，意味着没有规律，没有计划，没有坚持，锻炼的效果就会大打折扣。
因此，要想收获健康的体魄，根据个人实际状况，需要制定适宜的锻炼计划，并按计划坚持不懈进行锻炼。

为了了解自身的身体状态，在每次运动过程中，需要记录即时心率，当心率超过160时，要及时停止运动并休息
请利用Python的time模块，编写代码，要求如下：
1.运动前输入运动项目，同时自动记录开始时间
2.运动时，每隔2秒模拟生成心率情况
3.当运动心率超过160，停止运动
4.自动记录结束时间，计算运动时长
4.运动后，输入运动状态
5.输出本次运动情况
'''

import time
import random
# 1. 运动前输入运动项目，同时自动记录开始时间
sport = input("请输入运动项目: ")
start_time = time.time()
print("开始 {}...".format(sport))
# 2. 运动时，每隔2秒记录记录心率情况
while True:
    heart_rate = random.randint(60, 180)
    print("当前心率: {} BPM".format(heart_rate))
    # 3.当运动心率超过160，停止运动
    if heart_rate>160:
        break
    time.sleep(2)  # 暂停2秒
# 4.自动记录结束时间，计算运动时长
end_time = time.time()
dur = end_time - start_time
dur_minutes = int(dur / 60)
dur_seconds = int(dur % 60)
# 5.运动后输入运动状态
sport_feedback = input("请输入运动之后的状态（如：感觉良好/有些累/非常累）: ")
# 5. 输出运动情况
# 将时间戳转换为本地时间元组
local_time = time.localtime(end_time)
# 将本地时间元组格式化为字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
# 输出格式化后的当前日期和时间
print("当前日期和时间是:{}".format(formatted_time))
print("{} 结束!".format(sport))
print("本次运动时长: {} 分钟 {} 秒".format(dur_minutes,dur_seconds))
print("运动之后的状态: {}".format(sport_feedback))