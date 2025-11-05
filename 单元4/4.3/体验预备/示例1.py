touristHeights = [1.8, 1.15, 1.62, 1.3, 1.65, 1.78, 1.1]  	  # 第1行
n = 0  							# 第2行
for tourist in touristHeights:  				  # 第3行
    if tourist <= 1.2:  					# 第4行
        n += 1  						# 第5行
print(f"共有{n}位游客获得了小红旗")  			  # 第6行
