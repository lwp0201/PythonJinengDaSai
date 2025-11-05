# 累加累乘-数列求和
'''
题目: 计算数列的和，包括等差数列、等比数列、阶乘数列等
要求掌握累加和累乘的基本编程方法

例如：
1. 计算1到n的自然数之和
2. 计算1到n的平方和
3. 计算1到n的阶乘和
4. 计算等比数列的和
'''

def sum_natural_numbers(n):
    """
    计算1到n的自然数之和
    :param n: int，自然数上限
    :return: int，自然数之和
    """
    # 方法一：循环累加
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += i
    return sum_result

def sum_natural_numbers_formula(n):
    """
    计算1到n的自然数之和（数学公式法）
    :param n: int，自然数上限
    :return: int，自然数之和
    """
    # 数学公式：1+2+...+n = n*(n+1)/2
    return n * (n + 1) // 2

def sum_squares(n):
    """
    计算1到n的平方和
    :param n: int，自然数上限
    :return: int，平方和
    """
    # 方法一：循环累加
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += i * i
    return sum_result

def sum_squares_formula(n):
    """
    计算1到n的平方和（数学公式法）
    :param n: int，自然数上限
    :return: int，平方和
    """
    # 数学公式：1²+2²+...+n² = n*(n+1)*(2n+1)/6
    return n * (n + 1) * (2 * n + 1) // 6

def factorial(n):
    """
    计算n的阶乘
    :param n: int，自然数
    :return: int，n的阶乘
    """
    if n <= 1:
        return 1
    
    # 累乘法
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_factorials(n):
    """
    计算1到n的阶乘和
    :param n: int，自然数上限
    :return: int，阶乘和
    """
    sum_result = 0
    current_factorial = 1
    
    for i in range(1, n + 1):
        current_factorial *= i  # 累乘计算阶乘
        sum_result += current_factorial  # 累加阶乘
    return sum_result

def geometric_series_sum(a, r, n):
    """
    计算等比数列的和
    :param a: int，首项
    :param r: int，公比
    :param n: int，项数
    :return: int，等比数列和
    """
    if r == 1:
        return a * n
    
    # 方法一：循环累加
    sum_result = 0
    current_term = a
    for i in range(n):
        sum_result += current_term
        current_term *= r
    return sum_result

def geometric_series_sum_formula(a, r, n):
    """
    计算等比数列的和（数学公式法）
    :param a: int，首项
    :param r: int，公比
    :param n: int，项数
    :return: int，等比数列和
    """
    if r == 1:
        return a * n
    # 数学公式：S = a*(r^n - 1)/(r - 1)
    return a * (r**n - 1) // (r - 1)

def arithmetic_series_sum(a, d, n):
    """
    计算等差数列的和
    :param a: int，首项
    :param d: int，公差
    :param n: int，项数
    :return: int，等差数列和
    """
    # 方法一：循环累加
    sum_result = 0
    current_term = a
    for i in range(n):
        sum_result += current_term
        current_term += d
    return sum_result

def arithmetic_series_sum_formula(a, d, n):
    """
    计算等差数列的和（数学公式法）
    :param a: int，首项
    :param d: int，公差
    :param n: int，项数
    :return: int，等差数列和
    """
    # 数学公式：S = n*(2a + (n-1)*d)/2
    return n * (2 * a + (n - 1) * d) // 2

# 测试代码
if __name__ == "__main__":
    n = 10
    
    print(f"计算1到{n}的自然数之和:")
    print(f"循环法: {sum_natural_numbers(n)}")
    print(f"公式法: {sum_natural_numbers_formula(n)}")
    
    print(f"\n计算1到{n}的平方和:")
    print(f"循环法: {sum_squares(n)}")
    print(f"公式法: {sum_squares_formula(n)}")
    
    print(f"\n计算{n}的阶乘:")
    print(f"结果: {factorial(n)}")
    
    print(f"\n计算1到{n}的阶乘和:")
    print(f"结果: {sum_factorials(n)}")
    
    print(f"\n计算首项为2，公比为3，共{n}项的等比数列和:")
    print(f"循环法: {geometric_series_sum(2, 3, n)}")
    print(f"公式法: {geometric_series_sum_formula(2, 3, n)}")
    
    print(f"\n计算首项为1，公差为2，共{n}项的等差数列和:")
    print(f"循环法: {arithmetic_series_sum(1, 2, n)}")
    print(f"公式法: {arithmetic_series_sum_formula(1, 2, n)}")
    
    # 性能对比测试
    import time
    
    n_large = 100000
    print(f"\n性能测试 (n={n_large}):")
    
    start_time = time.time()
    result1 = sum_natural_numbers(n_large)
    time1 = time.time() - start_time
    
    start_time = time.time()
    result2 = sum_natural_numbers_formula(n_large)
    time2 = time.time() - start_time
    
    print(f"循环法耗时: {time1:.6f}秒，结果: {result1}")
    print(f"公式法耗时: {time2:.6f}秒，结果: {result2}")
    print(f"公式法比循环法快 {time1/time2:.2f} 倍")

