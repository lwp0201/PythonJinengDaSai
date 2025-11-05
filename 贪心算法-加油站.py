# 贪心算法-加油站
'''
题目: 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

注意：如果题目有解，该答案即为唯一答案。

例如：
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可以作为起始索引。

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
开往 2 号加油站，你需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
'''

def canCompleteCircuit(gas, cost):
    """
    找到能够绕环路行驶一周的起始加油站
    :param gas: list，每个加油站的汽油量
    :param cost: list，从每个加油站到下一个加油站的消耗
    :return: int，起始加油站索引，如果无解返回-1
    """
    # 贪心算法思想：
    # 1. 如果总汽油量小于总消耗量，肯定无解
    # 2. 如果从某个加油站出发无法到达下一个加油站，那么从这个加油站之前的任何加油站出发都无法到达
    # 3. 因此，我们可以从无法到达的位置的下一个位置开始尝试
    
    total_gas = 0  # 总汽油量
    total_cost = 0  # 总消耗量
    current_gas = 0  # 当前油箱中的汽油量
    start_station = 0  # 起始加油站
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]
        
        # 如果当前油箱汽油不足，说明从start_station到i都无法作为起始点
        if current_gas < 0:
            start_station = i + 1  # 从下一个加油站开始尝试
            current_gas = 0  # 重置当前汽油量
    
    # 如果总汽油量小于总消耗量，无解
    if total_gas < total_cost:
        return -1
    
    return start_station

def canCompleteCircuitDetailed(gas, cost):
    """
    详细版本：找到起始加油站并显示行驶过程
    :param gas: list，每个加油站的汽油量
    :param cost: list，从每个加油站到下一个加油站的消耗
    :return: tuple，(起始加油站索引, 行驶过程)
    """
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    if total_gas < total_cost:
        return -1, []
    
    current_gas = 0
    start_station = 0
    journey = []  # 行驶过程记录
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        journey.append({
            'station': i,
            'gas_available': gas[i],
            'cost': cost[i],
            'gas_after': current_gas
        })
        
        if current_gas < 0:
            start_station = i + 1
            current_gas = 0
    
    return start_station, journey

def canCompleteCircuitBruteForce(gas, cost):
    """
    暴力解法：尝试从每个加油站出发
    :param gas: list，每个加油站的汽油量
    :param cost: list，从每个加油站到下一个加油站的消耗
    :return: int，起始加油站索引，如果无解返回-1
    """
    n = len(gas)
    
    for start in range(n):
        current_gas = 0
        can_complete = True
        
        for i in range(n):
            station = (start + i) % n
            current_gas += gas[station] - cost[station]
            
            if current_gas < 0:
                can_complete = False
                break
        
        if can_complete:
            return start
    
    return -1

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    result1 = canCompleteCircuit(gas1, cost1)
    start1, journey1 = canCompleteCircuitDetailed(gas1, cost1)
    result1_brute = canCompleteCircuitBruteForce(gas1, cost1)
    
    print(f"汽油量: {gas1}")
    print(f"消耗量: {cost1}")
    print(f"贪心算法结果: 从第{result1}个加油站出发")
    print(f"暴力算法结果: 从第{result1_brute}个加油站出发")
    
    if start1 != -1:
        print(f"\n从第{start1}个加油站出发的行驶过程:")
        for step in journey1:
            print(f"  加油站{step['station']}: 获得{step['gas_available']}升, "
                  f"消耗{step['cost']}升, 剩余{step['gas_after']}升")
    
    # 测试用例2
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    result2 = canCompleteCircuit(gas2, cost2)
    result2_brute = canCompleteCircuitBruteForce(gas2, cost2)
    
    print(f"\n汽油量: {gas2}")
    print(f"消耗量: {cost2}")
    print(f"贪心算法结果: {result2}")
    print(f"暴力算法结果: {result2_brute}")
    
    # 测试用例3：边界情况
    gas3 = [5, 1, 2, 3, 4]
    cost3 = [4, 4, 1, 5, 1]
    result3 = canCompleteCircuit(gas3, cost3)
    
    print(f"\n汽油量: {gas3}")
    print(f"消耗量: {cost3}")
    print(f"结果: 从第{result3}个加油站出发")
    
    # 测试用例4：单个加油站
    gas4 = [2]
    cost4 = [2]
    result4 = canCompleteCircuit(gas4, cost4)
    
    print(f"\n汽油量: {gas4}")
    print(f"消耗量: {cost4}")
    print(f"结果: 从第{result4}个加油站出发")
