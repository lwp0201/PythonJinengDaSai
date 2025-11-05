poet = ["李白", "杜甫", "白居易", "王维", "孟浩然", "李商隐"]  # 诗人列表
poemCounts = [29, 39, 6, 29, 15, 24]  # 入选次数列表
poet.append("杜牧")  # 添加“杜牧”
poemCounts.append(9)  # 添加次数
print("诗人：", poet)
print("入选次数：", poemCounts)
m = min(poemCounts)  # 获取最小入选次数
i = poemCounts.index(m)  # 找到最小次数的索引
print("剔除诗人：{}，该诗人作品数为：{}".format(poet[i], poemCounts[i]))  # 输出剔除的相关信息
poet.pop(i)  # 剔除数据
poemCounts.pop(i)
poemCounts.sort(reverse=True)  # 从大到小排序
print("入选次数从大到小为：", poemCounts)