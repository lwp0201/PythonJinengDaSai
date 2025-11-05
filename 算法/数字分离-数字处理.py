# 数字分离-数字处理
'''
题目: 数字分离和处理相关的算法
要求掌握数字分离的基本编程方法

例如：
1. 分离一个数的各位数字
2. 判断一个数是否为回文数
3. 计算一个数的各位数字之和
4. 判断一个数是否为水仙花数
5. 数字反转
'''

def separate_digits(n):
    """
    分离一个数的各位数字
    :param n: int，待分离的数
    :return: list，各位数字列表
    """
    if n == 0:
        return [0]
    
    digits = []
    n = abs(n)  # 处理负数
    
    while n > 0:
        digits.append(n % 10)
        n //= 10
    
    return digits[::-1]  # 反转得到正确顺序

def separate_digits_string(n):
    """
    使用字符串方法分离数字
    :param n: int，待分离的数
    :return: list，各位数字列表
    """
    return [int(digit) for digit in str(abs(n))]

def sum_of_digits(n):
    """
    计算一个数的各位数字之和
    :param n: int，待计算的数
    :return: int，各位数字之和
    """
    total = 0
    n = abs(n)
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

def sum_of_digits_recursive(n):
    """
    递归计算各位数字之和
    :param n: int，待计算的数
    :return: int，各位数字之和
    """
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits_recursive(n // 10)

def is_palindrome(n):
    """
    判断一个数是否为回文数
    :param n: int，待判断的数
    :return: bool，是否为回文数
    """
    if n < 0:
        return False
    
    original = n
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    
    return original == reversed_num

def is_palindrome_string(n):
    """
    使用字符串方法判断回文数
    :param n: int，待判断的数
    :return: bool，是否为回文数
    """
    s = str(n)
    return s == s[::-1]

def reverse_number(n):
    """
    反转一个数字
    :param n: int，待反转的数
    :return: int，反转后的数
    """
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    
    return -reversed_num if is_negative else reversed_num

def is_armstrong_number(n):
    """
    判断一个数是否为水仙花数（阿姆斯特朗数）
    水仙花数：一个n位数，它的每个位上的数字的n次幂之和等于它本身
    :param n: int，待判断的数
    :return: bool，是否为水仙花数
    """
    if n < 0:
        return False
    
    original = n
    digits = separate_digits(n)
    power = len(digits)
    
    total = 0
    for digit in digits:
        total += digit ** power
    
    return total == original

def find_armstrong_numbers(start, end):
    """
    查找指定范围内的所有水仙花数
    :param start: int，起始值
    :param end: int，结束值
    :return: list，水仙花数列表
    """
    armstrong_numbers = []
    
    for n in range(start, end + 1):
        if is_armstrong_number(n):
            armstrong_numbers.append(n)
    
    return armstrong_numbers

def digital_root(n):
    """
    计算数字根（数位根）
    数字根：反复计算各位数字之和，直到得到一位数
    :param n: int，待计算的数
    :return: int，数字根
    """
    n = abs(n)
    
    while n >= 10:
        n = sum_of_digits(n)
    
    return n

def digital_root_formula(n):
    """
    使用数学公式计算数字根
    :param n: int，待计算的数
    :return: int，数字根
    """
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def count_digits(n):
    """
    计算一个数的位数
    :param n: int，待计算的数
    :return: int，位数
    """
    if n == 0:
        return 1
    
    count = 0
    n = abs(n)
    
    while n > 0:
        count += 1
        n //= 10
    
    return count

def count_digits_log(n):
    """
    使用对数计算位数
    :param n: int，待计算的数
    :return: int，位数
    """
    import math
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1

def is_harshad_number(n):
    """
    判断一个数是否为哈沙德数（尼文数）
    哈沙德数：能被其各位数字之和整除的数
    :param n: int，待判断的数
    :return: bool，是否为哈沙德数
    """
    if n <= 0:
        return False
    
    digit_sum = sum_of_digits(n)
    return n % digit_sum == 0

def find_harshad_numbers(start, end):
    """
    查找指定范围内的所有哈沙德数
    :param start: int，起始值
    :param end: int，结束值
    :return: list，哈沙德数列表
    """
    harshad_numbers = []
    
    for n in range(start, end + 1):
        if is_harshad_number(n):
            harshad_numbers.append(n)
    
    return harshad_numbers

# 测试代码
if __name__ == "__main__":
    # 测试数字分离
    test_number = 12345
    print(f"数字 {test_number} 的各位数字:")
    print(f"循环法: {separate_digits(test_number)}")
    print(f"字符串法: {separate_digits_string(test_number)}")
    
    # 测试各位数字之和
    print(f"\n数字 {test_number} 的各位数字之和:")
    print(f"循环法: {sum_of_digits(test_number)}")
    print(f"递归法: {sum_of_digits_recursive(test_number)}")
    
    # 测试回文数判断
    palindrome_tests = [121, 12321, 12345, 1221, 123]
    print(f"\n回文数判断测试:")
    for num in palindrome_tests:
        print(f"{num}: {is_palindrome(num)} (字符串法: {is_palindrome_string(num)})")
    
    # 测试数字反转
    reverse_tests = [12345, 12321, -12345, 0]
    print(f"\n数字反转测试:")
    for num in reverse_tests:
        print(f"{num} -> {reverse_number(num)}")
    
    # 测试水仙花数
    print(f"\n水仙花数判断测试:")
    armstrong_tests = [153, 371, 407, 123, 9474]
    for num in armstrong_tests:
        print(f"{num}: {is_armstrong_number(num)}")
    
    print(f"\n1到1000之间的水仙花数:")
    armstrong_numbers = find_armstrong_numbers(1, 1000)
    print(armstrong_numbers)
    
    # 测试数字根
    digital_root_tests = [12345, 98765, 123, 999]
    print(f"\n数字根测试:")
    for num in digital_root_tests:
        print(f"{num}: {digital_root(num)} (公式法: {digital_root_formula(num)})")
    
    # 测试位数计算
    digit_count_tests = [12345, 0, 1, 123456789]
    print(f"\n位数计算测试:")
    for num in digit_count_tests:
        print(f"{num}: {count_digits(num)} 位 (对数法: {count_digits_log(num)} 位)")
    
    # 测试哈沙德数
    print(f"\n哈沙德数判断测试:")
    harshad_tests = [12, 18, 20, 21, 24, 27, 30, 36, 40, 42]
    for num in harshad_tests:
        print(f"{num}: {is_harshad_number(num)}")
    
    print(f"\n1到50之间的哈沙德数:")
    harshad_numbers = find_harshad_numbers(1, 50)
    print(harshad_numbers)
    
    # 综合测试
    print(f"\n综合测试 - 数字 {test_number}:")
    print(f"各位数字: {separate_digits(test_number)}")
    print(f"各位数字之和: {sum_of_digits(test_number)}")
    print(f"位数: {count_digits(test_number)}")
    print(f"数字根: {digital_root(test_number)}")
    print(f"是否为回文数: {is_palindrome(test_number)}")
    print(f"是否为水仙花数: {is_armstrong_number(test_number)}")
    print(f"是否为哈沙德数: {is_harshad_number(test_number)}")
    print(f"反转后: {reverse_number(test_number)}")

