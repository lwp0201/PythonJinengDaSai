'''
你有一个包含字符串的列表lst，以及一个整数index。
请编写一个函数get_word_at_index，
该函数尝试获取lst列表中指定索引index的句子中的第一个单词，并返回该单词。
如果index超出列表的范围，或者指定句子为空或没有单词
则捕获IndexError和其他异常，并返回None。

'''
def get_word_at_index(lst, index):
    try:
        word = lst[index]
        if not word:
            return None
        return word.split()[0]
    except IndexError:
        return None
    except Exception as err:
        print("代码运行出现其他错误，错误原因：{}".format(err))

lst = ["Hello world", "This is a test", "Python is fun"]
index = 1
print(get_word_at_index(lst, index))  # 输出："This"

index = 10
print(get_word_at_index(lst, index))  # 输出：None