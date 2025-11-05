#对各个数字的出现次数分别赋值
num1 = 367
num2 = 57
num3 = 147
num4 = 55
num5 = 65
num6 = 42
num7 = 41
num8 = 54
num9 = 46
num10 = 64
num100 = 90
num1000 = 124
num10000 = 117

print("“三”出现的次数比“二”出现的次数多--->", num3 > num2)
print("“四”出现的次数比“七”出现的次数的两倍还多--->", num4 > num7 * 2)
print("奇数的次数和比偶数的次数和大，并且比“百”、“千”、“万”的和更大--->",
      num1 + num3 + num5 + num7 + num9 > num2 + num4 + num6 + num8 + num10 and num1 + num3 + num5 + num7 + num9 > num100 + num1000 + num10000)