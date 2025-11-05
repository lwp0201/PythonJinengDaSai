'''
年龄验证

'''
while True:
    try:
        age = int(input("请输入您的年龄："))
        if age < 0:
            print("年龄不能为负数")
        elif age < 18:
            print("您还未成年。")
        else:
            print("您已经成年。")
        continue
    except ValueError:
        print("输入错误：年龄必须是一个整数。")
    except Exception as err:
        print("代码运行出现其他错误，错误原因：{}".format(err))
