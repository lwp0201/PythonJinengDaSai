# 定义列表保存成语
wordList = ['一帆风顺','三心二意','八仙过海','五湖四海','千锤百炼','七上八下']
wordList.append("一举两得")                  #把"一举两得"添加到列表中
wordList.remove('千锤百炼')                  #把"千锤百炼"移除列表
wordCount = len(wordList)                    #统计输入的成语个数
print("成语列表为：", wordList)              # 输出成语列表
print("总共有", wordCount , "个成语")        # 统计输入的成语个数
wordList.sort()                              # 对输入的成语进行排序
print("排序后：", wordList)                  # 输出排序后的结果