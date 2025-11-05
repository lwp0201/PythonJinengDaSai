'''
列表读取错误
假设你正在编写一个管理班级学生名单的程序。这个程序允许你通过索引来访问、修改或删除学生的信息。
每个学生都有一个唯一的学号，这个学号被用作列表中的索引。
'''



def getInfoById(id,students):
    try:
        id = int(id)
        stuinfo=students[id - 1]
    except ValueError:
        return "学号要求是整数，请检查输入"
    except IndexError:
        return "学号不存在，请检查输入"
    except Exception as err:
        return "代码运行出现其他错误，错误原因：{}".format(err)
    else:
        return stuinfo

students=[
    [1,"张三","男","住宿","非团员","唱歌，看书"],
    [2, "李四", "女", "走读", "团员", "游泳，画画"],
    [3, "王五", "男", "住宿", "非团员", "打篮球，编程"],
    [4, "赵六", "女", "走读", "团员", "跳舞，写作"],
    [5, "陈七", "男", "住宿", "非团员", "摄影，旅行"],
    [6, "刘八", "女", "走读", "团员", "做饭，看电影"]
]
while True:
    id=input("请输入学号：")
    info = getInfoById(id, students)
    print(info)