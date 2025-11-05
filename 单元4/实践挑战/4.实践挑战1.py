weight = eval(input("请输入体重(kg)："))
height = eval(input("身高(cm)："))
height = height / 100
bmi = weight / height ** 2
if bmi < 18.5:
    print("体重过低")
elif 18.5 <= bmi < 24:
    print("正常范围")
elif 24 <= bmi < 27:
    print("超重")
elif 27 <= bmi < 29.9:
    print("I度肥胖")
elif 30 <= bmi < 34.9:
    print("II度肥胖")
elif 35 <= bmi < 39.9:
    print("III度肥胖")
else:
    print("IV度肥胖")

lowWeight = int(18.5 * height * height)
upperWeight = int(24 * height * height)
print(f"您的理想体重范围：{lowWeight}kg-{upperWeight}kg")
