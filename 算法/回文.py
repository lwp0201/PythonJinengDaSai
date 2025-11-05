#回文数
num = input("请输入一个数字:")
if num == num[::-1]:
    print("是回文数")
else:
    print("不是回文数")