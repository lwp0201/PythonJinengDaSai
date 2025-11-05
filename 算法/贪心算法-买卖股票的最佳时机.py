# 贪心算法-买卖股票的最佳时机
'''
题目: 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），
设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

例如：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，
最大利润 = 6-1 = 5。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

def maxProfit(prices):
    """
    计算买卖股票的最大利润（只能交易一次）
    :param prices: list，股票每天的价格
    :return: int，最大利润
    """
    # 贪心算法思想：为了获得最大利润，我们应该在最低点买入，在最高点卖出。
    # 遍历价格数组，维护一个变量记录到目前为止的最低价格，
    # 同时计算如果今天卖出能获得的最大利润。
    
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]  # 到目前为止的最低价格
    max_profit = 0  # 最大利润
    
    for price in prices[1:]:
        # 更新最低价格
        min_price = min(min_price, price)
        
        # 计算如果今天卖出的利润，并更新最大利润
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
    
    return max_profit

def maxProfitWithDetails(prices):
    """
    计算买卖股票的最大利润，并返回买卖时机
    :param prices: list，股票每天的价格
    :return: tuple，(最大利润, 买入日期, 卖出日期)
    """
    if not prices or len(prices) < 2:
        return 0, -1, -1
    
    min_price = prices[0]
    min_price_day = 0
    max_profit = 0
    buy_day = -1
    sell_day = -1
    
    for i in range(1, len(prices)):
        price = prices[i]
        
        # 更新最低价格和买入日期
        if price < min_price:
            min_price = price
            min_price_day = i
        
        # 计算当前利润并更新最大利润
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = min_price_day
            sell_day = i
    
    return max_profit, buy_day, sell_day

def maxProfitMultipleTransactions(prices):
    """
    计算买卖股票的最大利润（可以多次交易）
    :param prices: list，股票每天的价格
    :return: int，最大利润
    """
    # 贪心算法思想：只要明天的价格比今天高，就在今天买入明天卖出
    # 这样可以获得所有上涨的收益
    
    if not prices or len(prices) < 2:
        return 0
    
    max_profit = 0
    
    for i in range(1, len(prices)):
        # 如果今天价格比昨天高，就进行交易
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    
    return max_profit

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = maxProfit(prices1)
    profit1, buy1, sell1 = maxProfitWithDetails(prices1)
    print(f"股票价格: {prices1}")
    print(f"最大利润: {result1}")
    if buy1 != -1 and sell1 != -1:
        print(f"买入日期: 第{buy1+1}天 (价格{prices1[buy1]})")
        print(f"卖出日期: 第{sell1+1}天 (价格{prices1[sell1]})")
    
    # 测试用例2
    prices2 = [7, 6, 4, 3, 1]
    result2 = maxProfit(prices2)
    print(f"\n股票价格: {prices2}")
    print(f"最大利润: {result2}")
    
    # 测试用例3：多次交易
    prices3 = [1, 2, 3, 4, 5]
    result3_single = maxProfit(prices3)
    result3_multiple = maxProfitMultipleTransactions(prices3)
    print(f"\n股票价格: {prices3}")
    print(f"单次交易最大利润: {result3_single}")
    print(f"多次交易最大利润: {result3_multiple}")
    
    # 测试用例4：边界情况
    prices4 = [5, 4, 3, 2, 1]
    result4 = maxProfit(prices4)
    print(f"\n股票价格: {prices4}")
    print(f"最大利润: {result4}")
    
    # 测试用例5：空数组
    prices5 = []
    result5 = maxProfit(prices5)
    print(f"\n股票价格: {prices5}")
    print(f"最大利润: {result5}")

