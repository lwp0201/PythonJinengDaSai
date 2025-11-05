'''
查看学生作业
输入学生姓名，显示学生作业内容

编写一个函数read_file_content，该函数接受一个文件名作为参数，
并尝试读取该文件的内容。如果文件不存在，
则捕获FileNotFoundError异常，并打印一条错误消息。
如果文件存在并成功读取，则返回文件内容。

'''
import os
path=os.getcwd()
while True:
    filename = input("请输入学生姓名：")
    filepath = path + "/学生作业/" + filename + ".txt"
    try:
        with open(filepath,"r",encoding='utf8') as f:
            s=f.read()
    except FileNotFoundError:
        print("文件未找到，请重新输入学生姓名")
    except Exception as err:
        print("代码运行出现其他错误，请重新输入学生姓名")
        print("错误原因：{}".format(err))
    else:
        print("学生【{}】的作业如下：{}".format(filename,s))
