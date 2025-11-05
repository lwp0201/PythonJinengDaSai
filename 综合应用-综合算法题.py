# 综合应用-综合算法题
'''
题目: 综合应用各种编程基本方法的算法题
要求掌握累加、累乘、求最值、穷举、求素数、数字分离、字符处理、排序等方法的综合应用

例如：
1. 综合数字处理
2. 综合字符串处理
3. 综合排序应用
4. 综合数学计算
5. 综合算法优化
'''

def comprehensive_number_processing():
    """
    综合数字处理
    """
    print("=== 综合数字处理 ===")
    
    def process_number(n):
        """
        综合处理一个数字
        """
        print(f"\n处理数字: {n}")
        
        # 1. 数字分离
        digits = []
        temp = n
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10
        digits.reverse()
        print(f"各位数字: {digits}")
        
        # 2. 累加各位数字
        digit_sum = sum(digits)
        print(f"各位数字之和: {digit_sum}")
        
        # 3. 累乘各位数字
        digit_product = 1
        for digit in digits:
            digit_product *= digit
        print(f"各位数字之积: {digit_product}")
        
        # 4. 求最值
        max_digit = max(digits)
        min_digit = min(digits)
        print(f"最大数字: {max_digit}, 最小数字: {min_digit}")
        
        # 5. 判断是否为回文数
        is_palindrome = digits == digits[::-1]
        print(f"是否为回文数: {is_palindrome}")
        
        # 6. 判断是否为水仙花数
        power = len(digits)
        armstrong_sum = sum(digit ** power for digit in digits)
        is_armstrong = armstrong_sum == n
        print(f"是否为水仙花数: {is_armstrong}")
        
        # 7. 判断是否为完数
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        is_perfect = sum(factors) == n
        print(f"是否为完数: {is_perfect}")
        if is_perfect:
            print(f"真因数: {factors}")
        
        return {
            'digits': digits,
            'digit_sum': digit_sum,
            'digit_product': digit_product,
            'max_digit': max_digit,
            'min_digit': min_digit,
            'is_palindrome': is_palindrome,
            'is_armstrong': is_armstrong,
            'is_perfect': is_perfect
        }
    
    # 测试多个数字
    test_numbers = [123, 121, 153, 28, 496, 9474]
    results = []
    
    for num in test_numbers:
        result = process_number(num)
        results.append((num, result))
    
    return results

def comprehensive_string_processing():
    """
    综合字符串处理
    """
    print("\n=== 综合字符串处理 ===")
    
    def process_string(s):
        """
        综合处理一个字符串
        """
        print(f"\n处理字符串: '{s}'")
        
        # 1. 字符统计
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        print(f"字符统计: {char_count}")
        
        # 2. 字符类型统计
        upper_count = sum(1 for c in s if c.isupper())
        lower_count = sum(1 for c in s if c.islower())
        digit_count = sum(1 for c in s if c.isdigit())
        space_count = sum(1 for c in s if c.isspace())
        other_count = len(s) - upper_count - lower_count - digit_count - space_count
        
        print(f"字符类型统计:")
        print(f"  大写字母: {upper_count}")
        print(f"  小写字母: {lower_count}")
        print(f"  数字: {digit_count}")
        print(f"  空格: {space_count}")
        print(f"  其他字符: {other_count}")
        
        # 3. 字符串反转
        reversed_s = s[::-1]
        print(f"反转后: '{reversed_s}'")
        
        # 4. 判断是否为回文
        is_palindrome = s.lower().replace(" ", "") == reversed_s.lower().replace(" ", "")
        print(f"是否为回文: {is_palindrome}")
        
        # 5. 单词统计
        words = s.split()
        word_count = len(words)
        print(f"单词数: {word_count}")
        
        # 6. 最长单词
        if words:
            longest_word = max(words, key=len)
            print(f"最长单词: '{longest_word}' (长度: {len(longest_word)})")
        
        # 7. 字符排序
        sorted_chars = sorted(s)
        print(f"字符排序: {sorted_chars}")
        
        return {
            'char_count': char_count,
            'upper_count': upper_count,
            'lower_count': lower_count,
            'digit_count': digit_count,
            'space_count': space_count,
            'other_count': other_count,
            'reversed': reversed_s,
            'is_palindrome': is_palindrome,
            'word_count': word_count,
            'longest_word': longest_word if words else None,
            'sorted_chars': sorted_chars
        }
    
    # 测试多个字符串
    test_strings = ["Hello World", "racecar", "Python Programming", "12345", "A man a plan a canal Panama"]
    results = []
    
    for s in test_strings:
        result = process_string(s)
        results.append((s, result))
    
    return results

def comprehensive_sorting_application():
    """
    综合排序应用
    """
    print("\n=== 综合排序应用 ===")
    
    # 学生成绩数据
    students = [
        {"name": "张三", "chinese": 85, "math": 92, "english": 78},
        {"name": "李四", "chinese": 92, "math": 88, "english": 85},
        {"name": "王五", "chinese": 78, "math": 95, "english": 90},
        {"name": "赵六", "chinese": 88, "math": 82, "english": 88},
        {"name": "钱七", "chinese": 95, "math": 90, "english": 92}
    ]
    
    print("原始学生数据:")
    for student in students:
        total = student["chinese"] + student["math"] + student["english"]
        avg = total / 3
        print(f"  {student['name']}: 语文{student['chinese']}, 数学{student['math']}, 英语{student['english']}, 总分{total}, 平均分{avg:.1f}")
    
    # 1. 按总分排序（冒泡排序）
    print("\n1. 按总分排序（冒泡排序）:")
    students_by_total = students.copy()
    n = len(students_by_total)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            total1 = students_by_total[j]["chinese"] + students_by_total[j]["math"] + students_by_total[j]["english"]
            total2 = students_by_total[j + 1]["chinese"] + students_by_total[j + 1]["math"] + students_by_total[j + 1]["english"]
            if total1 < total2:
                students_by_total[j], students_by_total[j + 1] = students_by_total[j + 1], students_by_total[j]
    
    for i, student in enumerate(students_by_total, 1):
        total = student["chinese"] + student["math"] + student["english"]
        print(f"  第{i}名: {student['name']} (总分: {total})")
    
    # 2. 按数学成绩排序（选择排序）
    print("\n2. 按数学成绩排序（选择排序）:")
    students_by_math = students.copy()
    n = len(students_by_math)
    
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if students_by_math[j]["math"] > students_by_math[max_index]["math"]:
                max_index = j
        
        if max_index != i:
            students_by_math[i], students_by_math[max_index] = students_by_math[max_index], students_by_math[i]
    
    for i, student in enumerate(students_by_math, 1):
        print(f"  第{i}名: {student['name']} (数学: {student['math']})")
    
    # 3. 多条件排序
    print("\n3. 多条件排序（先按总分，再按数学成绩）:")
    students_multi = students.copy()
    
    def compare_students(s1, s2):
        total1 = s1["chinese"] + s1["math"] + s1["english"]
        total2 = s2["chinese"] + s2["math"] + s2["english"]
        if total1 != total2:
            return total1 > total2
        return s1["math"] > s2["math"]
    
    # 使用冒泡排序进行多条件排序
    n = len(students_multi)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not compare_students(students_multi[j], students_multi[j + 1]):
                students_multi[j], students_multi[j + 1] = students_multi[j + 1], students_multi[j]
    
    for i, student in enumerate(students_multi, 1):
        total = student["chinese"] + student["math"] + student["english"]
        print(f"  第{i}名: {student['name']} (总分: {total}, 数学: {student['math']})")

def comprehensive_math_calculation():
    """
    综合数学计算
    """
    print("\n=== 综合数学计算 ===")
    
    def calculate_statistics(numbers):
        """
        计算统计信息
        """
        if not numbers:
            return None
        
        # 1. 累加
        total = sum(numbers)
        print(f"累加和: {total}")
        
        # 2. 累乘
        product = 1
        for num in numbers:
            product *= num
        print(f"累乘积: {product}")
        
        # 3. 求最值
        max_val = max(numbers)
        min_val = min(numbers)
        print(f"最大值: {max_val}, 最小值: {min_val}")
        
        # 4. 平均值
        average = total / len(numbers)
        print(f"平均值: {average:.2f}")
        
        # 5. 中位数
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            median = sorted_numbers[n // 2]
        else:
            median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        print(f"中位数: {median}")
        
        # 6. 方差和标准差
        variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
        std_dev = variance ** 0.5
        print(f"方差: {variance:.2f}")
        print(f"标准差: {std_dev:.2f}")
        
        # 7. 素数统计
        prime_count = 0
        primes = []
        for num in numbers:
            if num > 1:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_count += 1
                    primes.append(num)
        
        print(f"素数个数: {prime_count}")
        print(f"素数列表: {primes}")
        
        return {
            'total': total,
            'product': product,
            'max': max_val,
            'min': min_val,
            'average': average,
            'median': median,
            'variance': variance,
            'std_dev': std_dev,
            'prime_count': prime_count,
            'primes': primes
        }
    
    # 测试数据
    test_numbers = [12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 17, 23, 29, 31, 37]
    print(f"测试数据: {test_numbers}")
    
    result = calculate_statistics(test_numbers)
    
    return result

def comprehensive_algorithm_optimization():
    """
    综合算法优化
    """
    print("\n=== 综合算法优化 ===")
    
    def find_common_elements(arr1, arr2):
        """
        找两个数组的公共元素（优化版本）
        """
        # 方法1：暴力法 O(n*m)
        print("方法1：暴力法")
        common1 = []
        for x in arr1:
            if x in arr2 and x not in common1:
                common1.append(x)
        print(f"公共元素: {common1}")
        
        # 方法2：集合法 O(n+m)
        print("方法2：集合法（优化）")
        set1 = set(arr1)
        set2 = set(arr2)
        common2 = list(set1 & set2)
        print(f"公共元素: {common2}")
        
        return common1, common2
    
    def find_duplicates(arr):
        """
        找数组中的重复元素（优化版本）
        """
        # 方法1：暴力法 O(n²)
        print("方法1：暴力法")
        duplicates1 = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j] and arr[i] not in duplicates1:
                    duplicates1.append(arr[i])
        print(f"重复元素: {duplicates1}")
        
        # 方法2：计数法 O(n)
        print("方法2：计数法（优化）")
        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1
        
        duplicates2 = [x for x, c in count.items() if c > 1]
        print(f"重复元素: {duplicates2}")
        
        return duplicates1, duplicates2
    
    def fibonacci_optimized(n):
        """
        斐波那契数列（优化版本）
        """
        # 方法1：递归法 O(2^n)
        def fib_recursive(n):
            if n <= 1:
                return n
            return fib_recursive(n - 1) + fib_recursive(n - 2)
        
        # 方法2：动态规划 O(n)
        def fib_dp(n):
            if n <= 1:
                return n
            dp = [0] * (n + 1)
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]
        
        # 方法3：空间优化 O(n)时间，O(1)空间
        def fib_optimized(n):
            if n <= 1:
                return n
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
        print(f"斐波那契数列第{n}项:")
        print(f"递归法: {fib_recursive(n)}")
        print(f"动态规划: {fib_dp(n)}")
        print(f"空间优化: {fib_optimized(n)}")
        
        return fib_recursive(n), fib_dp(n), fib_optimized(n)
    
    # 测试优化算法
    print("1. 找公共元素:")
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [4, 5, 6, 7, 8, 9]
    find_common_elements(arr1, arr2)
    
    print("\n2. 找重复元素:")
    arr3 = [1, 2, 3, 2, 4, 5, 3, 6, 7, 2]
    find_duplicates(arr3)
    
    print("\n3. 斐波那契数列优化:")
    fibonacci_optimized(10)

def main():
    """
    主函数，演示综合应用
    """
    print("=== 综合应用算法题演示 ===")
    
    # 综合数字处理
    number_results = comprehensive_number_processing()
    
    # 综合字符串处理
    string_results = comprehensive_string_processing()
    
    # 综合排序应用
    comprehensive_sorting_application()
    
    # 综合数学计算
    math_results = comprehensive_math_calculation()
    
    # 综合算法优化
    comprehensive_algorithm_optimization()
    
    print("\n=== 综合应用总结 ===")
    print("本程序综合应用了以下编程基本方法：")
    print("1. 累加、累乘 - 数字处理和数学计算")
    print("2. 求最值 - 数字处理和统计计算")
    print("3. 穷举 - 素数判断和重复元素查找")
    print("4. 求素数 - 数学计算中的素数统计")
    print("5. 数字分离 - 数字处理中的各位数字提取")
    print("6. 字符处理 - 字符串处理中的各种操作")
    print("7. 冒泡排序 - 学生成绩排序")
    print("8. 选择排序 - 学生成绩排序")
    print("9. 算法优化 - 时间复杂度和空间复杂度优化")

if __name__ == "__main__":
    main()

