# 求最值
nums = [12, 5, 23, 8, 19, 2, 45]
# 不使用内置方法求最大值和最小值
max_num = nums[0]
min_num = nums[0]
for num in nums[1:]:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("最大值为:", max_num)
print("最小值为:", min_num)
