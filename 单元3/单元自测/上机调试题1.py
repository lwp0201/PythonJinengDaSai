aStr = input("请输入第一个数a: ")
bStr = input("请输入第二个数b: ")

a = float(aStr)
b = float(bStr)

sumAB = a + b                      # 计算两数之和
diffAB = a - b                     # 计算两数之差
productAB = a * b                  # 计算两数之积
squareDiff = a ** 2 - b ** 2       # 计算两数的平方差

# 打印结果
print("两数之和为:", sumAB)
print("两数之差为:", diffAB)
print("两数之积为:", productAB)
print("两数的平方差为:", squareDiff)