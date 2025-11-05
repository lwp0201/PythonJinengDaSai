try:
    # 尝试打开一个不存在的文件
    with open('123.txt', 'r') as file:
        # 如果文件存在，这里会执行文件读取操作
        content = file.read()
        print(content)
except FileNotFoundError as e:
    # 如果文件不存在，会捕获到FileNotFoundError异常
    print(f"文件未找到: {e}")

    # 程序继续执行其他操作（如果有的话）