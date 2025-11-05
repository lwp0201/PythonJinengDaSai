'''
标题： 标识符命名格式的自我练习

思政元素
坚持不懈的练习才是通往成功的道路

背诵英文单词
如何记忆 标识符的命名规则

'''

import random
import string
import keyword

'''
随机产生标识符（长度在3-8之间）

'''
def createid():
    n=random.randint(3,8)
    str1 = string.ascii_letters + string.digits + "_-!@#$%"
    lst=random.sample(str1, n)
    id = ''.join(lst)
    return id

'''
首字母只能是英文字符或下划线
内容只能是英文字符，下划线和数字组成
不能是关键字
'''
def checkid(idx):
    keywords = keyword.kwlist  # 获取所有的关键字列表
    ret = [1, "标识符正确无误"]
    # 判断标识符首字母是否是英文字母或下划线
    s = idx[0]
    if not ("a" <= s <= "z" or "A" <= s <= "Z" or s == "_"):
        ret[0] = 0
        ret[1] = "首字母不是英文字母或下划线"

    # 判断标识符中包含有非字母，数字，或下划线的字符
    for i in idx:
        if not ("a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9" or i == "_"):
            ret[0] = 0
            ret[1] = "标识符中包含有非字母，数字，或下划线的字符"
            break

    # 判断标识符是否是关键字
    if idx in keywords:
        ret[0] = 0
        ret[1] = "标识符是关键字"

    # 返回判断结果
    return ret

score=0
while True:
    id = createid()
    ret = checkid(id)
    try:
        print("标识符：【{}】".format(id))
        n=int(input("请指出以上标识符是否正确（正确：1，错误：0）："))
    except:
        print("输入错误")
    else:
        if n==ret[0]:
            score+=1
            print("答对了！")
        else:
            print("答错了")
            print("提示:{}".format(ret[1]))
    finally:
        print("当前得分：{}".format(score))
        print("="*20)


