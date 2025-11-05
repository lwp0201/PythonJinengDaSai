"""
🔐 ================================================
    自定义函数应用 - 安全密码生成器
================================================

📝 功能说明：
    使用自定义函数生成高安全性密码
    确保密码中每个字符都不重复，提高密码强度
    展示了函数封装、模块组合和算法设计

🔧 主要知识点：
    • 自定义函数定义和调用 (def, return)
    • string模块的使用 (ascii_letters, digits)
    • random模块的choice函数
    • 列表操作 (append, len, join)
    • 条件判断和循环控制 (while, if)
    • 字符去重算法设计
    • 用户输入处理 (input, int)

🎯 学习目标：
    掌握自定义函数的编写和调用
    理解模块化编程的思想
    学会设计高效的算法
    掌握字符串和列表的高级操作
    理解密码安全的基本原理

💡 扩展思考：
    可以添加特殊字符支持
    可以设置密码复杂度要求
    可以添加密码强度评估
    可以保存密码到文件
    可以添加密码历史记录

🛡️ 安全提示：
    生成的密码具有高随机性和唯一性
    每个字符都不重复，增加破解难度
    建议定期更换密码以保障账户安全
"""
import string
import random
def create_pwd(n):
    # 返回大小写字母和数字的组合
    chars = string.ascii_letters + string.digits
    lst = []
    while len(lst) < n:
        c = random.choice(chars)
        if c not in lst:
            lst.append(c)
    return "".join(lst)
while True:
    n=int(input("请输入n值："))
    print("长度为{}的随机密码为：{}".format(n,create_pwd(n)))

