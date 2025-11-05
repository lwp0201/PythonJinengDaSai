# 求素数-素数筛选
'''
题目: 求素数相关的算法，包括判断素数、筛选素数、孪生素数等
要求掌握求素数的基本编程方法

例如：
1. 判断一个数是否为素数
2. 求1到n之间的所有素数
3. 求第n个素数
4. 求孪生素数对
'''

def is_prime(n):
    """
    判断一个数是否为素数
    :param n: int，待判断的数
    :return: bool，是否为素数
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需要检查到sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    """
    优化的素数判断（6k±1优化）
    :param n: int，待判断的数
    :return: bool，是否为素数
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 6k±1优化：所有素数（除了2和3）都可以表示为6k±1的形式
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve_of_eratosthenes(n):
    """
    埃拉托斯特尼筛法求1到n之间的所有素数
    :param n: int，上限
    :return: list，素数列表
    """
    if n < 2:
        return []
    
    # 创建布尔数组，初始都为True
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = is_prime_list[1] = False
    
    # 从2开始筛选
    for i in range(2, int(n**0.5) + 1):
        if is_prime_list[i]:
            # 将i的倍数标记为非素数
            for j in range(i * i, n + 1, i):
                is_prime_list[j] = False
    
    # 收集所有素数
    primes = []
    for i in range(2, n + 1):
        if is_prime_list[i]:
            primes.append(i)
    
    return primes

def sieve_of_eratosthenes_optimized(n):
    """
    优化的埃拉托斯特尼筛法
    :param n: int，上限
    :return: list，素数列表
    """
    if n < 2:
        return []
    
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = is_prime_list[1] = False
    
    # 只处理奇数
    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime_list[i]:
            # 从i*i开始，步长为2*i（只处理奇数倍数）
            for j in range(i * i, n + 1, 2 * i):
                is_prime_list[j] = False
    
    primes = [2]  # 2是唯一的偶素数
    for i in range(3, n + 1, 2):
        if is_prime_list[i]:
            primes.append(i)
    
    return primes

def nth_prime(n):
    """
    求第n个素数
    :param n: int，素数的序号
    :return: int，第n个素数
    """
    if n <= 0:
        return -1
    if n == 1:
        return 2
    
    count = 1
    candidate = 3
    
    while count < n:
        if is_prime_optimized(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 2  # 只检查奇数
    
    return candidate

def twin_primes(n):
    """
    求1到n之间的孪生素数对
    孪生素数：相差2的素数对
    :param n: int，上限
    :return: list，孪生素数对列表
    """
    primes = sieve_of_eratosthenes(n)
    twin_pairs = []
    
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_pairs.append((primes[i], primes[i + 1]))
    
    return twin_pairs

def prime_factors(n):
    """
    求一个数的所有质因数
    :param n: int，待分解的数
    :return: list，质因数列表
    """
    if n < 2:
        return []
    
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

def prime_factors_count(n):
    """
    求一个数的质因数个数（包括重复）
    :param n: int，待分解的数
    :return: int，质因数个数
    """
    if n < 2:
        return 0
    
    count = 0
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 1
    
    if n > 1:
        count += 1
    
    return count

def goldbach_conjecture(n):
    """
    哥德巴赫猜想：验证偶数是否可以表示为两个素数之和
    :param n: int，偶数
    :return: tuple，两个素数，如果不存在返回None
    """
    if n < 4 or n % 2 != 0:
        return None
    
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    
    for p in primes:
        if p > n // 2:
            break
        if (n - p) in prime_set:
            return (p, n - p)
    
    return None

# 测试代码
if __name__ == "__main__":
    # 测试素数判断
    test_numbers = [2, 3, 4, 5, 17, 25, 29, 97, 100]
    print("素数判断测试:")
    for num in test_numbers:
        print(f"{num}: {is_prime(num)} (优化版: {is_prime_optimized(num)})")
    
    # 测试素数筛选
    n = 50
    print(f"\n1到{n}之间的所有素数:")
    primes1 = sieve_of_eratosthenes(n)
    primes2 = sieve_of_eratosthenes_optimized(n)
    print(f"标准筛法: {primes1}")
    print(f"优化筛法: {primes2}")
    print(f"素数个数: {len(primes1)}")
    
    # 测试第n个素数
    print(f"\n前10个素数:")
    for i in range(1, 11):
        print(f"第{i}个素数: {nth_prime(i)}")
    
    # 测试孪生素数
    print(f"\n1到{n}之间的孪生素数对:")
    twins = twin_primes(n)
    for pair in twins:
        print(f"({pair[0]}, {pair[1]})")
    
    # 测试质因数分解
    test_factor = 60
    print(f"\n{test_factor}的质因数分解:")
    factors = prime_factors(test_factor)
    print(f"质因数: {factors}")
    print(f"质因数个数: {prime_factors_count(test_factor)}")
    
    # 测试哥德巴赫猜想
    print(f"\n哥德巴赫猜想验证:")
    even_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
    for even in even_numbers:
        result = goldbach_conjecture(even)
        if result:
            print(f"{even} = {result[0]} + {result[1]}")
        else:
            print(f"{even}: 无法表示为两个素数之和")
    
    # 性能测试
    import time
    
    print(f"\n性能测试:")
    n_large = 100000
    
    start_time = time.time()
    primes_large = sieve_of_eratosthenes(n_large)
    time1 = time.time() - start_time
    
    start_time = time.time()
    primes_large_opt = sieve_of_eratosthenes_optimized(n_large)
    time2 = time.time() - start_time
    
    print(f"标准筛法 (n={n_large}): {time1:.6f}秒，找到{len(primes_large)}个素数")
    print(f"优化筛法 (n={n_large}): {time2:.6f}秒，找到{len(primes_large_opt)}个素数")
    print(f"优化筛法比标准筛法快 {time1/time2:.2f} 倍")
