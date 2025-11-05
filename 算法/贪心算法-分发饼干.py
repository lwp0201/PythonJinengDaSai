# 贪心算法-分发饼干
'''
题目: 假设你是一位很棒的家长，想要给你的孩子们一些饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让该孩子满足胃口的饼干的最小尺寸；
并且每块饼干 j，都有一个尺寸 s[j]。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

例如：
输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1, 2, 3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块饼干，2个孩子的胃口值分别是1, 2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2。
'''

def findContentChildren(g, s):
    """
    分发饼干，尽可能满足更多孩子
    :param g: list，孩子的胃口值列表
    :param s: list，饼干的尺寸列表
    :return: int，能够满足的孩子数量
    """
    # 贪心算法思想：为了满足尽可能多的孩子，我们应该：
    # 1. 优先满足胃口小的孩子（用小饼干满足小胃口）
    # 2. 优先使用小饼干（避免浪费大饼干）
    # 因此，我们将两个数组都排序，然后用双指针匹配
    
    g.sort()  # 将孩子的胃口值从小到大排序
    s.sort()  # 将饼干的尺寸从小到大排序
    
    child_index = 0  # 孩子指针
    cookie_index = 0  # 饼干指针
    satisfied_count = 0  # 满足的孩子数量
    
    # 双指针遍历
    while child_index < len(g) and cookie_index < len(s):
        # 如果当前饼干能满足当前孩子的胃口
        if s[cookie_index] >= g[child_index]:
            satisfied_count += 1
            child_index += 1  # 孩子得到满足，移动到下一个孩子
        cookie_index += 1  # 无论是否满足，饼干都被使用，移动到下一块饼干
    
    return satisfied_count

def findContentChildrenDetailed(g, s):
    """
    分发饼干（详细版本），返回分配方案
    :param g: list，孩子的胃口值列表
    :param s: list，饼干的尺寸列表
    :return: tuple，(满足的孩子数量, 分配方案)
    """
    # 创建带索引的列表，方便追踪原始位置
    children = [(g[i], i) for i in range(len(g))]
    cookies = [(s[i], i) for i in range(len(s))]
    
    # 按胃口值和尺寸排序
    children.sort()
    cookies.sort()
    
    child_index = 0
    cookie_index = 0
    satisfied_count = 0
    assignment = []  # 分配方案
    
    while child_index < len(children) and cookie_index < len(cookies):
        child_greed, child_original_index = children[child_index]
        cookie_size, cookie_original_index = cookies[cookie_index]
        
        if cookie_size >= child_greed:
            satisfied_count += 1
            assignment.append((child_original_index, cookie_original_index, child_greed, cookie_size))
            child_index += 1
        cookie_index += 1
    
    return satisfied_count, assignment

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    g1 = [1, 2, 3]
    s1 = [1, 1]
    result1 = findContentChildren(g1, s1)
    print(f"孩子胃口值: {g1}")
    print(f"饼干尺寸: {s1}")
    print(f"最多能满足 {result1} 个孩子")
    
    # 测试用例2
    g2 = [1, 2]
    s2 = [1, 2, 3]
    result2 = findContentChildren(g2, s2)
    print(f"\n孩子胃口值: {g2}")
    print(f"饼干尺寸: {s2}")
    print(f"最多能满足 {result2} 个孩子")
    
    # 测试用例3：详细版本
    g3 = [3, 1, 2]
    s3 = [2, 1, 3]
    result3, assignment3 = findContentChildrenDetailed(g3, s3)
    print(f"\n孩子胃口值: {g3}")
    print(f"饼干尺寸: {s3}")
    print(f"最多能满足 {result3} 个孩子")
    print("分配方案:")
    for child_idx, cookie_idx, greed, size in assignment3:
        print(f"  孩子{child_idx}(胃口{greed}) <- 饼干{cookie_idx}(尺寸{size})")
    
    # 测试用例4：边界情况
    g4 = [1, 1, 1]
    s4 = [1, 1, 1]
    result4 = findContentChildren(g4, s4)
    print(f"\n孩子胃口值: {g4}")
    print(f"饼干尺寸: {s4}")
    print(f"最多能满足 {result4} 个孩子")

