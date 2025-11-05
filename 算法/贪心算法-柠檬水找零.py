# 贪心算法-柠檬水找零
'''
题目: 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，按账单 bills 支付的顺序，一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

例如：
输入: [5,5,5,10,20]
输出: true
解释:
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找零一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

输入: [5,5,10]
输出: true

输入: [10,10]
输出: false

输入: [5,5,10,10,20]
输出: false
解释:
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
'''

def lemonadeChange(bills):
    """
    判断是否能给所有顾客正确找零
    :param bills: list，顾客支付的钞票面额列表
    :return: bool，是否能正确找零
    """
    # 贪心算法思想：对于找零，我们应该优先使用大面额的钞票。
    # 因为大面额的钞票更"珍贵"，应该尽量保留用于找零大面额的支付。
    # 具体策略：
    # - 收到5美元：直接收下，不需要找零
    # - 收到10美元：找零1张5美元
    # - 收到20美元：优先找零1张10美元+1张5美元，如果没有10美元则找零3张5美元
    
    five_count = 0  # 5美元钞票数量
    ten_count = 0   # 10美元钞票数量
    
    for bill in bills:
        if bill == 5:
            # 收到5美元，直接收下
            five_count += 1
        elif bill == 10:
            # 收到10美元，需要找零1张5美元
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False  # 没有5美元可以找零
        elif bill == 20:
            # 收到20美元，优先找零1张10美元+1张5美元
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                # 如果没有10美元，找零3张5美元
                five_count -= 3
            else:
                return False  # 无法找零
    
    return True

def lemonadeChangeDetailed(bills):
    """
    详细版本：显示找零过程
    :param bills: list，顾客支付的钞票面额列表
    :return: tuple，(是否能找零, 找零过程)
    """
    five_count = 0
    ten_count = 0
    process = []  # 找零过程记录
    
    for i, bill in enumerate(bills):
        if bill == 5:
            five_count += 1
            process.append(f"顾客{i+1}: 支付5美元，无需找零，剩余5美元×{five_count}，10美元×{ten_count}")
        elif bill == 10:
            if five_count > 0:
                five_count -= 1
                ten_count += 1
                process.append(f"顾客{i+1}: 支付10美元，找零5美元×1，剩余5美元×{five_count}，10美元×{ten_count}")
            else:
                process.append(f"顾客{i+1}: 支付10美元，无法找零，失败！")
                return False, process
        elif bill == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
                process.append(f"顾客{i+1}: 支付20美元，找零10美元×1+5美元×1，剩余5美元×{five_count}，10美元×{ten_count}")
            elif five_count >= 3:
                five_count -= 3
                process.append(f"顾客{i+1}: 支付20美元，找零5美元×3，剩余5美元×{five_count}，10美元×{ten_count}")
            else:
                process.append(f"顾客{i+1}: 支付20美元，无法找零，失败！")
                return False, process
    
    return True, process

def lemonadeChangeWithStats(bills):
    """
    带统计信息的版本
    :param bills: list，顾客支付的钞票面额列表
    :return: tuple，(是否能找零, 统计信息)
    """
    five_count = 0
    ten_count = 0
    total_revenue = 0
    total_change_given = 0
    
    for bill in bills:
        total_revenue += bill
        
        if bill == 5:
            five_count += 1
        elif bill == 10:
            if five_count > 0:
                five_count -= 1
                ten_count += 1
                total_change_given += 5
            else:
                return False, {
                    'total_revenue': total_revenue,
                    'total_change_given': total_change_given,
                    'remaining_fives': five_count,
                    'remaining_tens': ten_count,
                    'failed_at': bill
                }
        elif bill == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
                total_change_given += 15
            elif five_count >= 3:
                five_count -= 3
                total_change_given += 15
            else:
                return False, {
                    'total_revenue': total_revenue,
                    'total_change_given': total_change_given,
                    'remaining_fives': five_count,
                    'remaining_tens': ten_count,
                    'failed_at': bill
                }
    
    return True, {
        'total_revenue': total_revenue,
        'total_change_given': total_change_given,
        'remaining_fives': five_count,
        'remaining_tens': ten_count,
        'net_profit': total_revenue - total_change_given
    }

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    bills1 = [5, 5, 5, 10, 20]
    result1 = lemonadeChange(bills1)
    result1_detailed, process1 = lemonadeChangeDetailed(bills1)
    result1_stats, stats1 = lemonadeChangeWithStats(bills1)
    
    print(f"账单: {bills1}")
    print(f"能否找零: {result1}")
    print("详细过程:")
    for step in process1:
        print(f"  {step}")
    print(f"统计信息: {stats1}")
    
    # 测试用例2
    bills2 = [5, 5, 10]
    result2 = lemonadeChange(bills2)
    result2_detailed, process2 = lemonadeChangeDetailed(bills2)
    
    print(f"\n账单: {bills2}")
    print(f"能否找零: {result2}")
    print("详细过程:")
    for step in process2:
        print(f"  {step}")
    
    # 测试用例3
    bills3 = [10, 10]
    result3 = lemonadeChange(bills3)
    result3_detailed, process3 = lemonadeChangeDetailed(bills3)
    
    print(f"\n账单: {bills3}")
    print(f"能否找零: {result3}")
    print("详细过程:")
    for step in process3:
        print(f"  {step}")
    
    # 测试用例4
    bills4 = [5, 5, 10, 10, 20]
    result4 = lemonadeChange(bills4)
    result4_detailed, process4 = lemonadeChangeDetailed(bills4)
    
    print(f"\n账单: {bills4}")
    print(f"能否找零: {result4}")
    print("详细过程:")
    for step in process4:
        print(f"  {step}")
    
    # 测试用例5：边界情况
    bills5 = [5]
    result5 = lemonadeChange(bills5)
    print(f"\n账单: {bills5}")
    print(f"能否找零: {result5}")

