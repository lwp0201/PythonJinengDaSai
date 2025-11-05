# 排序算法-冒泡排序
'''
题目: 冒泡排序算法及其优化
要求掌握冒泡排序的基本编程方法

例如：
1. 基本冒泡排序
2. 优化冒泡排序
3. 双向冒泡排序
4. 冒泡排序性能分析
5. 冒泡排序应用
'''

def bubble_sort_basic(arr):
    """
    基本冒泡排序
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()  # 不修改原数组
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n - 1):
        # 内层循环进行相邻元素比较和交换
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def bubble_sort_optimized(arr):
    """
    优化的冒泡排序（提前终止）
    :param arr: list，待排序的数组
    :return: tuple，(排序后的数组, 比较次数, 交换次数)
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n - 1):
        swapped = False  # 标记本轮是否发生交换
        
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr, comparisons, swaps

def bubble_sort_with_details(arr):
    """
    带详细过程的冒泡排序
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"初始数组: {arr}")
    
    for i in range(n - 1):
        print(f"\n第 {i + 1} 轮排序:")
        swapped = False
        
        for j in range(n - 1 - i):
            print(f"  比较 {arr[j]} 和 {arr[j + 1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f" -> 交换 -> {arr}")
                swapped = True
            else:
                print(f" -> 不交换")
        
        if not swapped:
            print("  数组已有序，提前结束")
            break
    
    return arr

def cocktail_sort(arr):
    """
    双向冒泡排序（鸡尾酒排序）
    :param arr: list，待排序的数组
    :return: list，排序后的数组
    """
    arr = arr.copy()
    n = len(arr)
    start = 0
    end = n - 1
    
    while start < end:
        # 从左到右冒泡
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end -= 1
        
        # 从右到左冒泡
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        start += 1
    
    return arr

def bubble_sort_recursive(arr, n=None):
    """
    递归冒泡排序
    :param arr: list，待排序的数组
    :param n: int，数组长度
    :return: list，排序后的数组
    """
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    # 一轮冒泡排序
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # 递归处理剩余部分
    return bubble_sort_recursive(arr, n - 1)

def bubble_sort_stable_demo():
    """
    演示冒泡排序的稳定性
    """
    print("\n=== 冒泡排序稳定性演示 ===")
    
    # 创建包含重复元素的数组
    arr = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]
    print(f"原始数组: {arr}")
    
    # 按第一个元素排序
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(f"排序后: {arr}")
    print("相同元素的相对位置保持不变，说明冒泡排序是稳定的")

def performance_comparison():
    """
    性能比较
    """
    import time
    import random
    
    print("\n=== 冒泡排序性能比较 ===")
    
    # 生成测试数据
    sizes = [100, 500, 1000]
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\n数组大小: {size}")
        
        # 基本冒泡排序
        start_time = time.time()
        bubble_sort_basic(arr)
        basic_time = time.time() - start_time
        
        # 优化冒泡排序
        start_time = time.time()
        bubble_sort_optimized(arr)
        optimized_time = time.time() - start_time
        
        # 双向冒泡排序
        start_time = time.time()
        cocktail_sort(arr)
        cocktail_time = time.time() - start_time
        
        print(f"基本冒泡排序: {basic_time:.6f}秒")
        print(f"优化冒泡排序: {optimized_time:.6f}秒")
        print(f"双向冒泡排序: {cocktail_time:.6f}秒")

def bubble_sort_applications():
    """
    冒泡排序的应用
    """
    print("\n=== 冒泡排序应用 ===")
    
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
        for j in range(n - 1 - i):
            if students[j]["score"] < students[j + 1]["score"]:
                students[j], students[j + 1] = students[j + 1], students[j]
    
    print("按成绩降序排列:", students)
    
    # 2. 字符串排序
    words = ["banana", "apple", "cherry", "date"]
    print(f"\n2. 字符串排序:")
    print("原始数据:", words)
    
    words_sorted = bubble_sort_basic(words)
    print("排序后:", words_sorted)
    
    # 3. 自定义比较函数
    def custom_bubble_sort(arr, compare_func):
        arr = arr.copy()
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if compare_func(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n3. 自定义比较函数排序:")
    print("原始数据:", numbers)
    
    # 按绝对值排序
    abs_sorted = custom_bubble_sort(numbers, lambda x, y: abs(x) > abs(y))
    print("按绝对值排序:", abs_sorted)

def bubble_sort_analysis():
    """
    冒泡排序算法分析
    """
    print("\n=== 冒泡排序算法分析 ===")
    
    print("时间复杂度:")
    print("  最好情况: O(n) - 数组已经有序")
    print("  平均情况: O(n²)")
    print("  最坏情况: O(n²) - 数组逆序")
    
    print("\n空间复杂度: O(1) - 原地排序")
    
    print("\n稳定性: 稳定 - 相等元素的相对位置不变")
    
    print("\n特点:")
    print("  1. 简单易懂，容易实现")
    print("  2. 原地排序，空间复杂度低")
    print("  3. 稳定排序")
    print("  4. 时间复杂度较高，不适合大数据量")
    print("  5. 可以通过优化减少不必要的比较")

def main():
    """
    主函数，演示冒泡排序的各种实现和应用
    """
    print("=== 冒泡排序算法综合演示 ===")
    
    # 测试数据
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"测试数组: {test_arr}")
    
    # 基本冒泡排序
    print("\n1. 基本冒泡排序:")
    result1 = bubble_sort_basic(test_arr)
    print(f"排序结果: {result1}")
    
    # 优化冒泡排序
    print("\n2. 优化冒泡排序:")
    result2, comparisons, swaps = bubble_sort_optimized(test_arr)
    print(f"排序结果: {result2}")
    print(f"比较次数: {comparisons}, 交换次数: {swaps}")
    
    # 详细过程演示
    print("\n3. 详细过程演示:")
    bubble_sort_with_details([5, 2, 8, 1, 9])
    
    # 双向冒泡排序
    print("\n4. 双向冒泡排序:")
    result3 = cocktail_sort(test_arr)
    print(f"排序结果: {result3}")
    
    # 递归冒泡排序
    print("\n5. 递归冒泡排序:")
    result4 = bubble_sort_recursive(test_arr.copy())
    print(f"排序结果: {result4}")
    
    # 稳定性演示
    bubble_sort_stable_demo()
    
    # 性能比较
    performance_comparison()
    
    # 应用示例
    bubble_sort_applications()
    
    # 算法分析
    bubble_sort_analysis()

if __name__ == "__main__":
    main()

