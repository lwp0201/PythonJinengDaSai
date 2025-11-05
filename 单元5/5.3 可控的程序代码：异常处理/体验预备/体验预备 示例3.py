'''
可以提示错误点

'''
while True:
    try:
        a=int(input("请输入被除数a："))
        b=int(input("请输入除数b："))
        c=a/b
    except ValueError:
        print("输入错误: 输入的不是数值类型，请重新输入。")
    except ZeroDivisionError:
        print("除数不能为零，请重新输入。")
    except Exception as err:
        print("代码运行出现其他错误，错误原因：{}".format(err))
    else:
        print("{}除以{}的商是:{}".format(a,b,c))
