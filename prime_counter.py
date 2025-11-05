def is_prime(n):
    """
    判断一个数是否为素数
    
    参数:
        n (int): 要判断的数
    
    返回:
        bool: 是否为素数
    """
    if n < 2:
        return False
    
    # 只需要检查到sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def count_prime(a, b):
    """
    统计指定范围内素数的个数
    
    参数:
        a (int): 范围起始值
        b (int): 范围结束值
    
    返回:
        int: 闭区间[a,b]内素数的个数
    """
    # 处理异常情况：a > b
    if a > b:
        return 0
    
    count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            count += 1
    
    return count


def main():
    """主函数测试用例"""
    print("=== 素数统计测试 ===")
    
    # 基本测试
    test_ranges = [(1, 10), (10, 20), (1, 100)]
    
    for a, b in test_ranges:
        count = count_prime(a, b)
        print(f"范围 [{a}, {b}]: {count} 个素数")
    
    # 异常情况测试
    print(f"范围 [10, 5] (a > b): {count_prime(10, 5)} 个素数")


if __name__ == "__main__":
    main()
