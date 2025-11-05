# 阶乘
def factorial(n):
    """
    计算正整数n的阶乘
    :param n: 正整数
    :return: n的阶乘
    """
    if n < 0:
        raise ValueError("n必须是正整数")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
