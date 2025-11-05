# 求最值-最值算法
'''
题目: 求最值相关的算法
要求掌握求最值的基本编程方法

例如：
1. 求数组中的最大值和最小值
2. 求第二大的数
3. 求数组中的最大值和最小值的位置
4. 求数组中的前k个最大值
5. 求数组中的中位数
'''

def find_max_min(arr):
    """
    求数组中的最大值和最小值
    :param arr: list，数组
    :return: tuple，(最大值, 最小值)
    """
    if not arr:
        return None, None
    
    max_val = min_val = arr[0]
    
    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return max_val, min_val

def find_max_min_builtin(arr):
    """
    使用内置函数求最大值和最小值
    :param arr: list，数组
    :return: tuple，(最大值, 最小值)
    """
    if not arr:
        return None, None
    
    return max(arr), min(arr)

def find_second_largest(arr):
    """
    求数组中的第二大的数
    :param arr: list，数组
    :return: int，第二大的数，如果不存在返回None
    """
    if len(arr) < 2:
        return None
    
    # 去重并排序
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None
    
    unique_arr.sort(reverse=True)
    return unique_arr[1]

def find_second_largest_optimized(arr):
    """
    优化的方法求第二大的数
    :param arr: list，数组
    :return: int，第二大的数，如果不存在返回None
    """
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

def find_max_min_positions(arr):
    """
    求数组中的最大值和最小值的位置
    :param arr: list，数组
    :return: tuple，(最大值位置列表, 最小值位置列表)
    """
    if not arr:
        return [], []
    
    max_val = max(arr)
    min_val = min(arr)
    
    max_positions = [i for i, x in enumerate(arr) if x == max_val]
    min_positions = [i for i, x in enumerate(arr) if x == min_val]
    
    return max_positions, min_positions

def find_top_k_largest(arr, k):
    """
    求数组中的前k个最大值
    :param arr: list，数组
    :param k: int，前k个
    :return: list，前k个最大值
    """
    if k <= 0 or k > len(arr):
        return []
    
    # 方法一：排序
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:k]

def find_top_k_largest_heap(arr, k):
    """
    使用堆求前k个最大值
    :param arr: list，数组
    :param k: int，前k个
    :return: list，前k个最大值
    """
    import heapq
    
    if k <= 0 or k > len(arr):
        return []
    
    # 使用最小堆
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return sorted(heap, reverse=True)

def find_median(arr):
    """
    求数组中的中位数
    :param arr: list，数组
    :return: float，中位数
    """
    if not arr:
        return None
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

def find_median_quickselect(arr):
    """
    使用快速选择算法求中位数
    :param arr: list，数组
    :return: float，中位数
    """
    if not arr:
        return None
    
    def quickselect(nums, k):
        if len(nums) == 1:
            return nums[0]
        
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        if k < len(left):
            return quickselect(left, k)
        elif k < len(left) + len(middle):
            return pivot
        else:
            return quickselect(right, k - len(left) - len(middle))
    
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr, n // 2)
    else:
        return (quickselect(arr, n // 2 - 1) + quickselect(arr, n // 2)) / 2

def find_kth_largest(arr, k):
    """
    求数组中的第k大的数
    :param arr: list，数组
    :param k: int，第k大
    :return: int，第k大的数
    """
    if k <= 0 or k > len(arr):
        return None
    
    # 去重
    unique_arr = list(set(arr))
    if k > len(unique_arr):
        return None
    
    unique_arr.sort(reverse=True)
    return unique_arr[k - 1]

def find_kth_largest_heap(arr, k):
    """
    使用堆求第k大的数
    :param arr: list，数组
    :param k: int，第k大
    :return: int，第k大的数
    """
    import heapq
    
    if k <= 0 or k > len(arr):
        return None
    
    # 使用最小堆
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

def find_local_maxima(arr):
    """
    找到数组中的所有局部最大值
    局部最大值：比相邻元素都大的元素
    :param arr: list，数组
    :return: list，局部最大值及其位置
    """
    if len(arr) < 3:
        return []
    
    local_maxima = []
    
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            local_maxima.append((arr[i], i))
    
    return local_maxima

def find_local_minima(arr):
    """
    找到数组中的所有局部最小值
    局部最小值：比相邻元素都小的元素
    :param arr: list，数组
    :return: list，局部最小值及其位置
    """
    if len(arr) < 3:
        return []
    
    local_minima = []
    
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            local_minima.append((arr[i], i))
    
    return local_minima

def find_peak_element(arr):
    """
    找到数组中的一个峰值元素
    峰值元素：大于或等于相邻元素的元素
    :param arr: list，数组
    :return: int，峰值元素的索引
    """
    if not arr:
        return -1
    
    if len(arr) == 1:
        return 0
    
    # 检查边界
    if arr[0] >= arr[1]:
        return 0
    if arr[-1] >= arr[-2]:
        return len(arr) - 1
    
    # 二分查找
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# 测试代码
if __name__ == "__main__":
    # 测试数据
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"测试数组: {test_arr}")
    
    # 测试最大值和最小值
    max_val, min_val = find_max_min(test_arr)
    max_val_builtin, min_val_builtin = find_max_min_builtin(test_arr)
    print(f"\n最大值和最小值:")
    print(f"自定义方法: 最大值={max_val}, 最小值={min_val}")
    print(f"内置函数: 最大值={max_val_builtin}, 最小值={min_val_builtin}")
    
    # 测试第二大的数
    second_largest = find_second_largest(test_arr)
    second_largest_opt = find_second_largest_optimized(test_arr)
    print(f"\n第二大的数:")
    print(f"排序方法: {second_largest}")
    print(f"优化方法: {second_largest_opt}")
    
    # 测试最大值和最小值的位置
    max_positions, min_positions = find_max_min_positions(test_arr)
    print(f"\n最大值和最小值的位置:")
    print(f"最大值{max_val}的位置: {max_positions}")
    print(f"最小值{min_val}的位置: {min_positions}")
    
    # 测试前k个最大值
    k = 3
    top_k = find_top_k_largest(test_arr, k)
    top_k_heap = find_top_k_largest_heap(test_arr, k)
    print(f"\n前{k}个最大值:")
    print(f"排序方法: {top_k}")
    print(f"堆方法: {top_k_heap}")
    
    # 测试中位数
    median = find_median(test_arr)
    median_quick = find_median_quickselect(test_arr)
    print(f"\n中位数:")
    print(f"排序方法: {median}")
    print(f"快速选择: {median_quick}")
    
    # 测试第k大的数
    k = 3
    kth_largest = find_kth_largest(test_arr, k)
    kth_largest_heap = find_kth_largest_heap(test_arr, k)
    print(f"\n第{k}大的数:")
    print(f"排序方法: {kth_largest}")
    print(f"堆方法: {kth_largest_heap}")
    
    # 测试局部最大值和最小值
    local_maxima = find_local_maxima(test_arr)
    local_minima = find_local_minima(test_arr)
    print(f"\n局部最大值: {local_maxima}")
    print(f"局部最小值: {local_minima}")
    
    # 测试峰值元素
    peak_index = find_peak_element(test_arr)
    print(f"\n峰值元素索引: {peak_index}, 值: {test_arr[peak_index]}")
    
    # 边界情况测试
    print(f"\n边界情况测试:")
    empty_arr = []
    single_arr = [5]
    two_arr = [3, 7]
    
    print(f"空数组: 最大值={find_max_min(empty_arr)[0]}, 最小值={find_max_min(empty_arr)[1]}")
    print(f"单元素数组: 最大值={find_max_min(single_arr)[0]}, 最小值={find_max_min(single_arr)[1]}")
    print(f"两元素数组: 最大值={find_max_min(two_arr)[0]}, 最小值={find_max_min(two_arr)[1]}")
    
    # 性能测试
    import time
    import random
    
    large_arr = [random.randint(1, 1000) for _ in range(10000)]
    k = 100
    
    print(f"\n性能测试 (数组长度: {len(large_arr)}):")
    
    start_time = time.time()
    top_k_sort = find_top_k_largest(large_arr, k)
    time_sort = time.time() - start_time
    
    start_time = time.time()
    top_k_heap = find_top_k_largest_heap(large_arr, k)
    time_heap = time.time() - start_time
    
    print(f"排序方法耗时: {time_sort:.6f}秒")
    print(f"堆方法耗时: {time_heap:.6f}秒")
    print(f"堆方法比排序方法快 {time_sort/time_heap:.2f} 倍")

