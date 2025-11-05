flag = True  # 初始化接龙游戏状态
idiomList = ["八仙过海"]  # 初始化成语
print("开始的成语是：", idiomList[0])
# 持续接龙
while flag == True:
    idiom = input("请接下一个成语：")  # 输入新的成语
    if idiom not in idiomList:  # 判断是否为新的成语
        lastIdiom = idiomList[-1]  # 获取上一个成语
        if lastIdiom[-1] == idiom[0]:  # 判断上一个成语的最后一个字与新成语的第一个字一致
            idiomList.append(idiom)  # 加入到成语列表
        else:
            print("上一个成语是：{}，你接的是{}，接龙失败!".format(lastIdiom, idiom))  # 输出错误信息
            flag = False  # 设置游戏状态为结束
    else:
        print("你接的成语已经存在！接龙失败")  # 输出错误信息
        flag = False  # 设置游戏状态为结束
print("接的成语有：", idiomList)  # 输出接龙成功的成语列表