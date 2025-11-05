tourists = ['张三', '李四', '王五', '赵六', '孙七']  # 全体旅客名单
arrived = ['李四', '赵六', '张三']  # 已到旅客名单
for people in tourists:  # 循环读取己到旅客名单
    tourists.remove(people)  # 从全体旅客名单中删除已到旅客
print("未到人数:", len(tourists))  # 打印输出
print("他们是:", tourists)  # 打印输出
