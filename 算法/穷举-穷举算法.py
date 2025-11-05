# 穷举-穷举算法
'''
题目: 穷举算法相关的题目
要求掌握穷举的基本编程方法

例如：
1. 百钱百鸡问题
2. 水仙花数
3. 完数
4. 回文数
5. 质数的和与积
6. 数字组合问题
'''

def hundred_chicken_problem():
    """
    百钱百鸡问题
    公鸡5钱一只，母鸡3钱一只，小鸡1钱三只
    用100钱买100只鸡，问公鸡、母鸡、小鸡各多少只？
    """
    print("=== 百钱百鸡问题 ===")
    print("公鸡5钱一只，母鸡3钱一只，小鸡1钱三只")
    print("用100钱买100只鸡，问公鸡、母鸡、小鸡各多少只？")
    
    solutions = []
    
    # 穷举所有可能的组合
    for cock in range(0, 21):  # 公鸡最多20只
        for hen in range(0, 34):  # 母鸡最多33只
            chick = 100 - cock - hen  # 小鸡数量
            if chick >= 0 and chick % 3 == 0:  # 小鸡必须是3的倍数
                cost = cock * 5 + hen * 3 + chick // 3
                if cost == 100:
                    solutions.append((cock, hen, chick))
    
    print(f"共有 {len(solutions)} 种解决方案：")
    for i, (cock, hen, chick) in enumerate(solutions, 1):
        print(f"方案{i}: 公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")
    
    return solutions

def narcissistic_numbers(start=100, end=999):
    """
    水仙花数（阿姆斯特朗数）
    一个n位数，它的每个位上的数字的n次幂之和等于它本身
    """
    print(f"\n=== {start}到{end}之间的水仙花数 ===")
    
    narcissistic_list = []
    
    for num in range(start, end + 1):
        # 分离各位数字
        digits = []
        temp = num
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10
        
        # 计算各位数字的n次幂之和
        power_sum = sum(digit ** len(digits) for digit in digits)
        
        if power_sum == num:
            narcissistic_list.append(num)
    
    print(f"找到 {len(narcissistic_list)} 个水仙花数：{narcissistic_list}")
    return narcissistic_list

def perfect_numbers(limit=10000):
    """
    完数（完美数）
    一个数等于它的所有真因数（除了自身以外的因数）之和
    """
    print(f"\n=== {limit}以内的完数 ===")
    
    perfect_list = []
    
    for num in range(2, limit + 1):
        # 找出所有真因数
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        
        # 检查是否为完数
        if sum(factors) == num:
            perfect_list.append(num)
            print(f"完数: {num}, 真因数: {factors}")
    
    print(f"找到 {len(perfect_list)} 个完数：{perfect_list}")
    return perfect_list

def palindrome_numbers(start=100, end=999):
    """
    回文数
    正读和反读都相同的数
    """
    print(f"\n=== {start}到{end}之间的回文数 ===")
    
    palindrome_list = []
    
    for num in range(start, end + 1):
        # 将数字转换为字符串
        num_str = str(num)
        # 检查是否为回文
        if num_str == num_str[::-1]:
            palindrome_list.append(num)
    
    print(f"找到 {len(palindrome_list)} 个回文数：{palindrome_list}")
    return palindrome_list

def prime_sum_product(limit=100):
    """
    质数的和与积
    找出所有质数，计算它们的和与积
    """
    print(f"\n=== {limit}以内质数的和与积 ===")
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    
    prime_sum = sum(primes)
    prime_product = 1
    for prime in primes:
        prime_product *= prime
    
    print(f"质数列表: {primes}")
    print(f"质数个数: {len(primes)}")
    print(f"质数和: {prime_sum}")
    print(f"质数积: {prime_product}")
    
    return primes, prime_sum, prime_product

def number_combinations():
    """
    数字组合问题
    用1,2,3,4四个数字，能组成多少个互不相同且无重复数字的三位数？
    """
    print("\n=== 数字组合问题 ===")
    print("用1,2,3,4四个数字，能组成多少个互不相同且无重复数字的三位数？")
    
    digits = [1, 2, 3, 4]
    combinations = []
    
    # 穷举所有可能的三位数组合
    for i in digits:
        for j in digits:
            for k in digits:
                if i != j and j != k and i != k:  # 确保无重复数字
                    number = i * 100 + j * 10 + k
                    combinations.append(number)
    
    print(f"共有 {len(combinations)} 个符合条件的三位数：")
    print(combinations)
    
    return combinations

def equation_solutions():
    """
    方程求解
    求解方程 x + y + z = 100，其中 x, y, z 都是正整数
    """
    print("\n=== 方程求解 ===")
    print("求解方程 x + y + z = 100，其中 x, y, z 都是正整数")
    
    solutions = []
    
    for x in range(1, 99):  # x 从1到98
        for y in range(1, 100 - x):  # y 从1到99-x
            z = 100 - x - y
            if z > 0:
                solutions.append((x, y, z))
    
    print(f"共有 {len(solutions)} 组解")
    print("前10组解：")
    for i, (x, y, z) in enumerate(solutions[:10]):
        print(f"解{i+1}: x={x}, y={y}, z={z}")
    
    return solutions

def password_crack():
    """
    密码破解（简单版本）
    假设密码是4位数字，从0000到9999
    """
    print("\n=== 简单密码破解 ===")
    print("假设密码是4位数字，从0000到9999")
    
    import random
    
    # 随机生成一个4位数字密码
    target_password = random.randint(0, 9999)
    print(f"目标密码: {target_password:04d}")
    
    attempts = 0
    found = False
    
    # 穷举所有可能的密码
    for password in range(10000):
        attempts += 1
        if password == target_password:
            found = True
            break
    
    if found:
        print(f"密码破解成功！尝试了 {attempts} 次")
    else:
        print("密码破解失败")
    
    return attempts

def magic_square():
    """
    三阶幻方
    在3x3的格子中填入1-9的数字，使每行、每列、每条对角线上的数字之和都相等
    """
    print("\n=== 三阶幻方 ===")
    print("在3x3的格子中填入1-9的数字，使每行、每列、每条对角线上的数字之和都相等")
    
    from itertools import permutations
    
    magic_squares = []
    numbers = list(range(1, 10))
    
    # 穷举所有可能的排列
    for perm in permutations(numbers):
        # 将排列转换为3x3矩阵
        matrix = [perm[i:i+3] for i in range(0, 9, 3)]
        
        # 检查是否为幻方
        magic_sum = sum(matrix[0])  # 第一行的和作为幻和
        
        # 检查所有行
        if not all(sum(row) == magic_sum for row in matrix):
            continue
        
        # 检查所有列
        if not all(sum(matrix[i][j] for i in range(3)) == magic_sum for j in range(3)):
            continue
        
        # 检查对角线
        if (sum(matrix[i][i] for i in range(3)) != magic_sum or
            sum(matrix[i][2-i] for i in range(3)) != magic_sum):
            continue
        
        magic_squares.append(matrix)
    
    print(f"找到 {len(magic_squares)} 个三阶幻方：")
    for i, square in enumerate(magic_squares[:3]):  # 只显示前3个
        print(f"幻方 {i+1}:")
        for row in square:
            print(f"  {row}")
        print(f"  幻和: {sum(square[0])}")
    
    return magic_squares

def subset_sum():
    """
    子集和问题
    给定一个数组和目标值，找出所有子集使其和等于目标值
    """
    print("\n=== 子集和问题 ===")
    print("给定数组 [1, 2, 3, 4, 5]，找出所有子集使其和等于目标值")
    
    arr = [1, 2, 3, 4, 5]
    target = 8
    
    def find_subsets(arr, target):
        from itertools import combinations
        subsets = []
        
        # 穷举所有可能的子集
        for r in range(1, len(arr) + 1):
            for subset in combinations(arr, r):
                if sum(subset) == target:
                    subsets.append(list(subset))
        
        return subsets
    
    subsets = find_subsets(arr, target)
    
    print(f"数组: {arr}")
    print(f"目标值: {target}")
    print(f"找到 {len(subsets)} 个子集：")
    for i, subset in enumerate(subsets):
        print(f"子集 {i+1}: {subset}, 和: {sum(subset)}")
    
    return subsets

def main():
    """
    主函数，演示各种穷举算法
    """
    print("=== 穷举算法综合演示 ===")
    
    # 各种穷举算法演示
    hundred_chicken_problem()
    narcissistic_numbers()
    perfect_numbers()
    palindrome_numbers()
    prime_sum_product()
    number_combinations()
    equation_solutions()
    password_crack()
    magic_square()
    subset_sum()
    
    print("\n=== 穷举算法总结 ===")
    print("穷举算法的特点：")
    print("1. 遍历所有可能的解")
    print("2. 适用于解空间较小的问题")
    print("3. 保证找到所有解")
    print("4. 时间复杂度通常较高")
    print("5. 适用于组合优化问题")

if __name__ == "__main__":
    main()

