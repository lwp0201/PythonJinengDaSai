'''
write_to_file函数尝试打开（或创建）一个文件，并以写入模式（'w'）打开它。
如果文件所在的目录不存在或者程序没有足够的权限来创建文件，
将会触发FileNotFoundError异常。
此外，我们也捕获了其他类型的异常，
以便在写入过程中发生其他问题时能够提供一些错误信息。
'''
def write_to_file(filename, content):
    try:
        with open(filename, 'w',encoding='utf8') as file:
            file.write(content)
        print("成功将内容写入文件：{}".format(filename))
    except FileNotFoundError:
        print("无法创建或写入文件：{}".format(filename))
    except Exception as err:
        print("代码运行出现其他错误，错误原因：{}".format(err))

    # 使用示例
write_to_file("output.txt", "Hello, World!")