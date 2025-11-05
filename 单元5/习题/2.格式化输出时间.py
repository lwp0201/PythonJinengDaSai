import time

# 获取当前时间的时间戳
current_time = time.time()

# 将时间戳转换为本地时间并格式化
local_time = time.localtime(current_time)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# 打印格式化后的时间
print(formatted_time)