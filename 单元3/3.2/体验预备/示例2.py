# 2021年和2023年的销量
sales2021 = 5000
sales2023 = 7500
# 使用公式计算增长率
# 增长率 = ((后一年的销量 / 前一年的销量) ** (1 / 年数) - 1
growthRate = ((sales2023 / sales2021) ** (1 / 2)) - 1
print(growthRate)