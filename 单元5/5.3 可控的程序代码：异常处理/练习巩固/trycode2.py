lst1=["apple","orange","banana"]
while True:
    try:
        i = int(input("请输入整数i："))
        s=lst1[i]
    except ValueError:
        print("i要求是整数，请检查输入")
    except IndexError:
        print("i超出了lst1列表的下标，请检查输入")
    except Exception as err:
        print("代码运行出现其他错误，错误原因：{}".format(err))
    else:
        print(s)
    finally:
        print("程序运行完毕")

