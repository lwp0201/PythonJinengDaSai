#选择排序
def selection_sort(arr):
    """
    选择排序算法，对传入的列表进行排序（从小到大）。
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 测试代码
if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    print("原始列表：", nums)
    sorted_nums = selection_sort(nums)
    print("排序后列表：", sorted_nums)
