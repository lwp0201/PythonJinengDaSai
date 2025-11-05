ages = [34, 25, 67, 65, 55, 43, 44, 51]  		# 第1行
for j in range(0, 7):  			# 第2行
    if ages[j] > ages[j + 1]:  			# 第3行
        ages[j], ages[j + 1] = ages[j + 1], ages[j]  	# 第4行
print(ages[7])  				# 第5行
