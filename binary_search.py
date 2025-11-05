def binary_search(nums, target):
    """
    二分法查找函数
    
    参数:
        nums (list): 有序列表
        target: 要查找的目标元素
    
    返回:
        int: 找到目标元素返回其索引，未找到返回-1
    """
    if not nums:  # 空列表
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # 计算中间位置
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def main():
    """主函数测试用例"""
    print("=== 二分法查找测试 ===")
    
    # 基本测试
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    targets = [5, 9, 2, 20]
    
    print(f"有序列表: {nums}")
    for target in targets:
        result = binary_search(nums, target)
        print(f"查找 {target}: 索引 {result}")


if __name__ == "__main__":
    main()
