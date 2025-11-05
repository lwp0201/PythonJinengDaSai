'''
题目描述
某国为了防御敌国的导弹袭击，发展出一种导弹拦截系统。但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于前一发的高度。某天，雷达捕捉到敌国的导弹来袭。由于该系统还在试用阶段，所以只有一套系统，因此有可能不能拦截所有的导弹。

输入导弹依次飞来的高度，计算这套系统最多能拦截多少导弹，如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。

输入格式
一行，若干个整数，中间由空格隔开。

输出格式
两行，每行一个整数，第一个数字表示这套系统最多能拦截多少导弹，第二个数字表示如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。
'''

import bisect

def lds_length(heights):
    # 最长不升子序列 O(nlogn)
    piles = []
    for h in heights:
        # 找到第一个 <= h 的位置（反向思考，维护递减序列）
        idx = bisect.bisect_right([-x for x in piles], -h)
        if idx == len(piles):
            piles.append(h)
        else:
            piles[idx] = h
    return len(piles)

def min_systems(heights):
    # 最少拦截系统数 O(nlogn)
    # 维护每个系统最后拦截的导弹高度的递增序列
    piles = []
    for h in heights:
        idx = bisect.bisect_left(piles, h)
        if idx == len(piles):
            piles.append(h)
        else:
            piles[idx] = h
    return len(piles)

# 重新实现 main，自动选择算法
def main_optimized():
    try:
        heights = list(map(int, input().strip().split()))
    except Exception:
        heights = []

    if not heights:
        print(0)
        print(0)
        return

    n = len(heights)
    if n <= 1000:
        # 小数据量，直接用O(n^2)算法
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if heights[i] <= heights[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))

        piles = []
        for h in heights:
            placed = False
            for i in range(len(piles)):
                if piles[i] >= h:
                    piles[i] = h
                    placed = True
                    break
            if not placed:
                piles.append(h)
        print(len(piles))
    else:
        # 大数据量，使用O(nlogn)算法
        print(lds_length(heights))
        print(min_systems(heights))

# 若需要用优化版，取消下行注释
main_optimized()
