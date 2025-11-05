# 本程序假设年龄最大的旅客只有一人
ages = [56, 45, 34, 70, 54, 60]
names = ['张三', '李四', "王五", "孙六", "刘七", "庞八"]
maxAge = ages[0]
maxName = names[0]
for i in range(1, 6):
    if ages[i] > maxAge:
        maxName = names[i]
        maxAge = ages[i]
print("幸运嘉宾:", maxName)
print("年龄:", maxAge)
