#快速排序
def quick_sort(arr):
    """
    快速排序算法，对传入的列表进行排序（从小到大）。
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# 测试代码
if __name__ == "__main__":
    nums = [50, 23, 9, 18, 61, 32]
    print("原始列表：", nums)
    sorted_nums = quick_sort(nums)
    print("排序后列表：", sorted_nums)
