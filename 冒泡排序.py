# 冒泡排序
def bubble_sort(arr):
    """
    冒泡排序算法，对传入的列表进行排序（从小到大）。
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False # 提前退出标志位
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 测试代码
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表：", nums)
    sorted_nums = bubble_sort(nums)
    print("排序后列表：", sorted_nums)
