import random


def process_students_list(students):
    """
    处理学生字典列表
    
    参数:
        students (list): 学生字典列表，直接修改原列表
    
    操作:
        1. 为每个学生添加random字段（0-100随机整数）
        2. 按random值从大到小排序
        3. 删除age小于20的学生
        4. 在每个学生的courses列表末尾添加"Pyic"
    """
    # 1. 为每个学生添加random字段
    for student in students:
        student['random'] = random.randint(0, 100)
    
    # 2. 按random值从大到小排序
    # 方法1：使用自定义函数（更易懂）
    def get_random_value(student):
        return student['random']
    
    students.sort(key=get_random_value, reverse=True)
    
    # 方法2：使用冒泡排序（完全手动实现）
    # n = len(students)
    # for i in range(n):
    #     for j in range(0, n - i - 1):
    #         if students[j]['random'] < students[j + 1]['random']:
    #             students[j], students[j + 1] = students[j + 1], students[j]
    
    # 3. 删除age小于20的学生
    # 方法1：分步骤删除
    i = 0
    while i < len(students):
        if students[i]['age'] < 20:
            students.pop(i)  # 删除当前学生
        else:
            i += 1  # 移动到下一个学生
    
    # 4. 在每个学生的courses列表末尾添加"Pyic"
    for student in students:
        student['courses'].append("Pyic")


def main():
    """主函数测试用例"""
    print("=== 字典列表处理测试 ===")
    
    # 基本测试
    students = [
        {"name": "李四", "age": 20, "courses": ["Python", "Math"]},
        {"name": "张三", "age": 19, "courses": ["Java"]},
        {"name": "王五", "age": 22, "courses": ["C++"]}
    ]
    
    print("处理前:", students)
    process_students_list(students)
    print("处理后:", students)


if __name__ == "__main__":
    main()
