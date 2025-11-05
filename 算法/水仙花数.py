# 水仙花数
def is_narcissistic_number(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i])**3
    return sum == num
