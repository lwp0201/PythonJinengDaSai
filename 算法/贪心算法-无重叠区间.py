# 贪心算法-无重叠区间
'''
题目: 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意：
1. 可以认为区间的终点总是大于它的起点。
2. 区间 [1,2] 和 [2,3] 的边界相互"接触"，但没有相互重叠。

例如：
输入: [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

输入: [[1,2],[1,2],[1,2]]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

输入: [[1,2],[2,3]]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''

def eraseOverlapIntervals(intervals):
    """
    计算需要移除区间的最小数量，使剩余区间互不重叠
    :param intervals: list，区间列表，每个区间是[start, end]格式
    :return: int，需要移除的区间数量
    """
    # 贪心算法思想：为了移除最少的区间，我们应该保留最多的不重叠区间。
    # 策略：按结束时间排序，优先选择结束时间早的区间。
    # 这样可以为后续区间留出更多空间。
    
    if not intervals or len(intervals) <= 1:
        return 0
    
    # 按结束时间排序
    intervals.sort(key=lambda x: x[1])
    
    count = 0  # 需要移除的区间数量
    end = intervals[0][1]  # 当前保留区间的结束时间
    
    for i in range(1, len(intervals)):
        # 如果当前区间与已保留的区间重叠，需要移除
        if intervals[i][0] < end:
            count += 1
        else:
            # 不重叠，保留当前区间，更新结束时间
            end = intervals[i][1]
    
    return count

def eraseOverlapIntervalsByStart(intervals):
    """
    按开始时间排序的贪心算法
    :param intervals: list，区间列表
    :return: int，需要移除的区间数量
    """
    if not intervals or len(intervals) <= 1:
        return 0
    
    # 按开始时间排序
    intervals.sort(key=lambda x: x[0])
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # 重叠，移除结束时间较晚的区间
            count += 1
            end = min(end, intervals[i][1])  # 保留结束时间早的
        else:
            end = intervals[i][1]
    
    return count

def findNonOverlappingIntervals(intervals):
    """
    找到最大数量的不重叠区间
    :param intervals: list，区间列表
    :return: list，最大数量的不重叠区间
    """
    if not intervals:
        return []
    
    # 按结束时间排序
    intervals.sort(key=lambda x: x[1])
    
    result = [intervals[0]]
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        # 如果当前区间不重叠，加入结果
        if intervals[i][0] >= end:
            result.append(intervals[i])
            end = intervals[i][1]
    
    return result

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    result1 = eraseOverlapIntervals(intervals1)
    result1_start = eraseOverlapIntervalsByStart(intervals1)
    non_overlapping1 = findNonOverlappingIntervals(intervals1)
    print(f"区间: {intervals1}")
    print(f"按结束时间排序 - 需要移除 {result1} 个区间")
    print(f"按开始时间排序 - 需要移除 {result1_start} 个区间")
    print(f"最大不重叠区间: {non_overlapping1}")
    
    # 测试用例2
    intervals2 = [[1,2],[1,2],[1,2]]
    result2 = eraseOverlapIntervals(intervals2)
    non_overlapping2 = findNonOverlappingIntervals(intervals2)
    print(f"\n区间: {intervals2}")
    print(f"需要移除 {result2} 个区间")
    print(f"最大不重叠区间: {non_overlapping2}")
    
    # 测试用例3
    intervals3 = [[1,2],[2,3]]
    result3 = eraseOverlapIntervals(intervals3)
    non_overlapping3 = findNonOverlappingIntervals(intervals3)
    print(f"\n区间: {intervals3}")
    print(f"需要移除 {result3} 个区间")
    print(f"最大不重叠区间: {non_overlapping3}")
    
    # 测试用例4：复杂情况
    intervals4 = [[1,4],[2,3],[3,5],[4,6]]
    result4 = eraseOverlapIntervals(intervals4)
    non_overlapping4 = findNonOverlappingIntervals(intervals4)
    print(f"\n区间: {intervals4}")
    print(f"需要移除 {result4} 个区间")
    print(f"最大不重叠区间: {non_overlapping4}")
    
    # 测试用例5：边界情况
    intervals5 = []
    result5 = eraseOverlapIntervals(intervals5)
    print(f"\n区间: {intervals5}")
    print(f"需要移除 {result5} 个区间")
