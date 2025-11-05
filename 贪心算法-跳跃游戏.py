# 贪心算法-跳跃游戏
'''
题目: 给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

例如：
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0，
所以你永远不可能到达最后一个位置。
'''

def canJump(nums):
    """
    判断是否能够到达最后一个位置
    :param nums: 非负整数数组，每个元素代表在该位置可以跳跃的最大长度
    :return: bool，是否能够到达最后一个位置
    """
    # 贪心算法思想：维护一个变量记录当前能够到达的最远位置。
    # 遍历数组，对于每个位置，如果当前位置在可达范围内，
    # 就更新最远可达位置。如果最远可达位置大于等于最后一个位置，则返回True。
    
    max_reach = 0  # 当前能够到达的最远位置
    
    for i in range(len(nums)):
        # 如果当前位置超出了最远可达位置，说明无法到达
        if i > max_reach:
            return False
        
        # 更新最远可达位置
        max_reach = max(max_reach, i + nums[i])
        
        # 如果已经能够到达最后一个位置，直接返回True
        if max_reach >= len(nums) - 1:
            return True
    
    return True

def canJumpWithSteps(nums):
    """
    判断是否能够到达最后一个位置，并返回最少跳跃步数
    :param nums: 非负整数数组
    :return: int，最少跳跃步数，如果无法到达返回-1
    """
    if len(nums) <= 1:
        return 0
    
    steps = 0  # 跳跃步数
    max_reach = 0  # 当前步数下能到达的最远位置
    end = 0  # 当前步数下能到达的边界
    
    for i in range(len(nums) - 1):
        # 更新当前步数下能到达的最远位置
        max_reach = max(max_reach, i + nums[i])
        
        # 如果到达了当前步数的边界，需要再跳一步
        if i == end:
            steps += 1
            end = max_reach
            
            # 如果边界已经覆盖了最后一个位置，返回步数
            if end >= len(nums) - 1:
                return steps
    
    return -1  # 无法到达

# 测试代码
if __name__ == "__main__":
    # 测试用例1：能够到达
    nums1 = [2, 3, 1, 1, 4]
    print(f"数组 {nums1} 能否到达最后位置: {canJump(nums1)}")
    print(f"最少跳跃步数: {canJumpWithSteps(nums1)}")
    
    # 测试用例2：无法到达
    nums2 = [3, 2, 1, 0, 4]
    print(f"\n数组 {nums2} 能否到达最后位置: {canJump(nums2)}")
    print(f"最少跳跃步数: {canJumpWithSteps(nums2)}")
    
    # 测试用例3：单个元素
    nums3 = [0]
    print(f"\n数组 {nums3} 能否到达最后位置: {canJump(nums3)}")
    print(f"最少跳跃步数: {canJumpWithSteps(nums3)}")
    
    # 测试用例4：简单情况
    nums4 = [1, 2, 3]
    print(f"\n数组 {nums4} 能否到达最后位置: {canJump(nums4)}")
    print(f"最少跳跃步数: {canJumpWithSteps(nums4)}")

