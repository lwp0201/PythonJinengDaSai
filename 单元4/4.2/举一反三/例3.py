tourists = ['张三', '李四', '王五', '赵六', '孙七']  # 全体旅客名单
while True:  # 循环点名
   people = input("已到旅客:")  # 输入已到旅客名单
   tourists.remove(people)  # 从全体旅客名单中删除已到旅客
   if tourists==[]:  # 如果旅客名单列表为空，即全部旅客到齐
       print("所有旅客都已到")  # 输出信息
       break  # 中断循环
