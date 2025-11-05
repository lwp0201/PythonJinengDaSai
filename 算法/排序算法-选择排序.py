# 排序算法-选择排序
'''
题目: 选择排序算法及其优化
要求掌握选择排序的基本编程方法

例如：
1. 基本选择排序
2. 优化选择排序
3. 双向选择排序
4. 选择排序性能分析
5. 选择排序应用
'''

def selection_sort_basic(arr):
    """
    基本选择排序
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()  # 不修改原数组
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n - 1):
        # 假设当前位置是最小值的位置
        min_index = i
        
        # 内层循环找到最小值的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # 交换元素
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def selection_sort_optimized(arr):
    """
    优化的选择排序（记录比较和交换次数）
    :param arr: list，待排序的数组
    :return: tuple，(排序后的数组, 比较次数, 交换次数)
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps

def selection_sort_with_details(arr):
    """
    带详细过程的选择排序
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"初始数组: {arr}")
    
    for i in range(n - 1):
        print(f"\n第 {i + 1} 轮排序:")
        min_index = i
        
        print(f"  从位置 {i} 开始寻找最小值")
        
        for j in range(i + 1, n):
            print(f"    比较 {arr[j]} 和 {arr[min_index]}", end="")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f" -> 更新最小值位置为 {j}")
            else:
                print(f" -> 最小值位置不变")
        
        if min_index != i:
            print(f"  交换 {arr[i]} 和 {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(f"  交换后: {arr}")
        else:
            print(f"  位置 {i} 已经是最小值，无需交换")
    
    return arr

def double_selection_sort(arr):
    """
    双向选择排序（同时找最大值和最小值）
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n // 2):
        min_index = i
        max_index = n - 1 - i
        
        # 找到最小值和最大值的索引
        for j in range(i, n - i):
            if arr[j] < arr[min_index]:
                min_index = j
            if arr[j] > arr[max_index]:
                max_index = j
        
        # 交换最小值到前面
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # 如果最大值在i位置，需要调整
        if max_index == i:
            max_index = min_index
        
        # 交换最大值到后面
        if max_index != n - 1 - i:
            arr[n - 1 - i], arr[max_index] = arr[max_index], arr[n - 1 - i]
    
    return arr

def selection_sort_recursive(arr, start=0):
    """
    递归选择排序
    :param arr: list，待排序的数组
    :param start: int，开始位置
    :return: list，排序后的数组
    """
    if start >= len(arr) - 1:
        return arr
    
    # 找到最小值的索引
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    
    # 交换元素
    if min_index != start:
        arr[start], arr[min_index] = arr[min_index], arr[start]
    
    # 递归处理剩余部分
    return selection_sort_recursive(arr, start + 1)

def selection_sort_stable_demo():
    """
    演示选择排序的不稳定性
    """
    print("\n=== 选择排序稳定性演示 ===")
    
    # 创建包含重复元素的数组
    arr = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]
    print(f"原始数组: {arr}")
    
    # 按第一个元素排序
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print(f"排序后: {arr}")
    print("相同元素的相对位置可能改变，说明选择排序是不稳定的")

def performance_comparison():
    """
    性能比较
    """
    import time
    import random
    
    print("\n=== 选择排序性能比较 ===")
    
    # 生成测试数据
    sizes = [100, 500, 1000]
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\n数组大小: {size}")
        
        # 基本选择排序
        start_time = time.time()
        selection_sort_basic(arr)
        basic_time = time.time() - start_time
        
        # 优化选择排序
        start_time = time.time()
        selection_sort_optimized(arr)
        optimized_time = time.time() - start_time
        
        # 双向选择排序
        start_time = time.time()
        double_selection_sort(arr)
        double_time = time.time() - start_time
        
        print(f"基本选择排序: {basic_time:.6f}秒")
        print(f"优化选择排序: {optimized_time:.6f}秒")
        print(f"双向选择排序: {double_time:.6f}秒")

def selection_sort_applications():
    """
    选择排序的应用
    """
    print("\n=== 选择排序应用 ===")
    
    # 1. 学生成绩排序
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 78},
        {"name": "赵六", "score": 88}
    ]
    
    print("1. 学生成绩排序:")
    print("原始数据:", students)
    
    # 按成绩排序
    n = len(students)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if students[j]["score"] > students[max_index]["score"]:
                max_index = j
        
        if max_index != i:
            students[i], students[max_index] = students[max_index], students[i]
    
    print("按成绩降序排列:", students)
    
    # 2. 字符串排序
    words = ["banana", "apple", "cherry", "date"]
    print(f"\n2. 字符串排序:")
    print("原始数据:", words)
    
    words_sorted = selection_sort_basic(words)
    print("排序后:", words_sorted)
    
    # 3. 自定义比较函数
    def custom_selection_sort(arr, compare_func):
        arr = arr.copy()
        n = len(arr)
        for i in range(n - 1):
            target_index = i
            for j in range(i + 1, n):
                if compare_func(arr[j], arr[target_index]):
                    target_index = j
            
            if target_index != i:
                arr[i], arr[target_index] = arr[target_index], arr[i]
        return arr
    
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n3. 自定义比较函数排序:")
    print("原始数据:", numbers)
    
    # 按绝对值排序
    abs_sorted = custom_selection_sort(numbers, lambda x, y: abs(x) < abs(y))
    print("按绝对值排序:", abs_sorted)

def selection_sort_analysis():
    """
    选择排序算法分析
    """
    print("\n=== 选择排序算法分析 ===")
    
    print("时间复杂度:")
    print("  最好情况: O(n²) - 仍需比较所有元素")
    print("  平均情况: O(n²)")
    print("  最坏情况: O(n²) - 数组逆序")
    
    print("\n空间复杂度: O(1) - 原地排序")
    
    print("\n稳定性: 不稳定 - 相等元素的相对位置可能改变")
    
    print("\n特点:")
    print("  1. 简单易懂，容易实现")
    print("  2. 原地排序，空间复杂度低")
    print("  3. 交换次数少，最多n-1次交换")
    print("  4. 时间复杂度固定为O(n²)")
    print("  5. 不适合大数据量排序")

def selection_vs_bubble():
    """
    选择排序与冒泡排序的比较
    """
    print("\n=== 选择排序 vs 冒泡排序 ===")
    
    print("相同点:")
    print("  1. 都是简单的排序算法")
    print("  2. 时间复杂度都是O(n²)")
    print("  3. 空间复杂度都是O(1)")
    print("  4. 都适合小数据量排序")
    
    print("\n不同点:")
    print("  选择排序:")
    print("    - 交换次数少，最多n-1次")
    print("    - 比较次数固定为n(n-1)/2")
    print("    - 不稳定排序")
    print("    - 时间复杂度固定")
    
    print("  冒泡排序:")
    print("    - 交换次数多，最多n(n-1)/2次")
    print("    - 比较次数可变，可优化")
    print("    - 稳定排序")
    print("    - 最好情况时间复杂度O(n)")

def main():
    """
    主函数，演示选择排序的各种实现和应用
    """
    print("=== 选择排序算法综合演示 ===")
    
    # 测试数据
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"测试数组: {test_arr}")
    
    # 基本选择排序
    print("\n1. 基本选择排序:")
    result1 = selection_sort_basic(test_arr)
    print(f"排序结果: {result1}")
    
    # 优化选择排序
    print("\n2. 优化选择排序:")
    result2, comparisons, swaps = selection_sort_optimized(test_arr)
    print(f"排序结果: {result2}")
    print(f"比较次数: {comparisons}, 交换次数: {swaps}")
    
    # 详细过程演示
    print("\n3. 详细过程演示:")
    selection_sort_with_details([5, 2, 8, 1, 9])
    
    # 双向选择排序
    print("\n4. 双向选择排序:")
    result3 = double_selection_sort(test_arr)
    print(f"排序结果: {result3}")
    
    # 递归选择排序
    print("\n5. 递归选择排序:")
    result4 = selection_sort_recursive(test_arr.copy())
    print(f"排序结果: {result4}")
    
    # 稳定性演示
    selection_sort_stable_demo()
    
    # 性能比较
    performance_comparison()
    
    # 应用示例
    selection_sort_applications()
    
    # 算法分析
    selection_sort_analysis()
    
    # 与冒泡排序比较
    selection_vs_bubble()

if __name__ == "__main__":
    main()

