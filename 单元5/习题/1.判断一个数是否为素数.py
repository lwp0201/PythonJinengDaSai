import random


def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 生成1到100之间的随机整数
random_num = random.randint(1, 100)

# 判断该数是否为素数
if is_prime(random_num):
    print(f"{random_num} 是一个素数。")
else:
    print(f"{random_num} 不是一个素数。")