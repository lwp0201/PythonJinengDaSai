age = int(input("旅客年龄:"))   # 第1行
if age <= 12:                   # 第2行
    print("免票")               # 第3行
elif 12 < age < 60:             # 第4行
    print("全价票")            # 第5行
elif 60 <= age < 70:           # 第6行
    print("半价票")            # 第7行
else:                          # 第8行
    print("免票")             # 第9行
