# 贪心算法-最大子数组和
'''
题目: 给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

例如：
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

输入: [1]
输出: 1

输入: [5,4,-1,7,8]
输出: 23

输入: [-1]
输出: -1
'''

def maxSubArray(nums):
    """
    找到最大子数组和（贪心算法）
    :param nums: list，整数数组
    :return: int，最大子数组和
    """
    # 贪心算法思想：如果当前子数组的和为负数，那么继续累加只会让结果更小。
    # 因此，当子数组和为负数时，我们应该重新开始计算子数组和。
    # 这样可以保证我们总是在寻找"有希望"的子数组。
    
    if not nums:
        return 0
    
    max_sum = nums[0]  # 全局最大和
    current_sum = nums[0]  # 当前子数组和
    
    for i in range(1, len(nums)):
        # 如果当前子数组和为负数，重新开始
        if current_sum < 0:
            current_sum = nums[i]
        else:
            # 否则继续累加
            current_sum += nums[i]
        
        # 更新全局最大和
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def maxSubArrayWithIndices(nums):
    """
    找到最大子数组和，并返回子数组的起始和结束索引
    :param nums: list，整数数组
    :return: tuple，(最大和, 起始索引, 结束索引)
    """
    if not nums:
        return 0, -1, -1
    
    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

def maxSubArrayDetailed(nums):
    """
    详细版本：显示计算过程
    :param nums: list，整数数组
    :return: tuple，(最大和, 计算过程)
    """
    if not nums:
        return 0, []
    
    max_sum = nums[0]
    current_sum = nums[0]
    process = [f"初始: current_sum={current_sum}, max_sum={max_sum}"]
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            process.append(f"位置{i}: 重新开始，current_sum={current_sum}")
        else:
            current_sum += nums[i]
            process.append(f"位置{i}: 累加{nums[i]}，current_sum={current_sum}")
        
        if current_sum > max_sum:
            max_sum = current_sum
            process.append(f"位置{i}: 更新max_sum={max_sum}")
    
    return max_sum, process

def maxSubArrayBruteForce(nums):
    """
    暴力解法：尝试所有可能的子数组
    :param nums: list，整数数组
    :return: int，最大子数组和
    """
    if not nums:
        return 0
    
    max_sum = nums[0]
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def maxSubArrayDivideConquer(nums):
    """
    分治法：将问题分解为子问题
    :param nums: list，整数数组
    :return: int，最大子数组和
    """
    def divideConquer(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # 递归求解左右两部分的最大子数组和
        left_max = divideConquer(left, mid)
        right_max = divideConquer(mid + 1, right)
        
        # 计算跨越中点的最大子数组和
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
        
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
        
        cross_sum = left_sum + right_sum
        
        return max(left_max, right_max, cross_sum)
    
    if not nums:
        return 0
    
    return divideConquer(0, len(nums) - 1)

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = maxSubArray(nums1)
    result1_indices = maxSubArrayWithIndices(nums1)
    result1_detailed, process1 = maxSubArrayDetailed(nums1)
    result1_brute = maxSubArrayBruteForce(nums1)
    result1_divide = maxSubArrayDivideConquer(nums1)
    
    print(f"数组: {nums1}")
    print(f"贪心算法结果: {result1}")
    print(f"暴力算法结果: {result1_brute}")
    print(f"分治算法结果: {result1_divide}")
    print(f"最大子数组和: {result1_indices[0]}, 起始索引: {result1_indices[1]}, 结束索引: {result1_indices[2]}")
    print("计算过程:")
    for step in process1:
        print(f"  {step}")
    
    # 测试用例2
    nums2 = [1]
    result2 = maxSubArray(nums2)
    print(f"\n数组: {nums2}")
    print(f"最大子数组和: {result2}")
    
    # 测试用例3
    nums3 = [5, 4, -1, 7, 8]
    result3 = maxSubArray(nums3)
    result3_indices = maxSubArrayWithIndices(nums3)
    print(f"\n数组: {nums3}")
    print(f"最大子数组和: {result3}")
    print(f"子数组: {nums3[result3_indices[1]:result3_indices[2]+1]}")
    
    # 测试用例4
    nums4 = [-1]
    result4 = maxSubArray(nums4)
    print(f"\n数组: {nums4}")
    print(f"最大子数组和: {result4}")
    
    # 测试用例5：全负数
    nums5 = [-5, -2, -8, -1]
    result5 = maxSubArray(nums5)
    result5_indices = maxSubArrayWithIndices(nums5)
    print(f"\n数组: {nums5}")
    print(f"最大子数组和: {result5}")
    print(f"子数组: {nums5[result5_indices[1]:result5_indices[2]+1]}")

