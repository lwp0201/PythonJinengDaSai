# 基本结构-控制结构应用
'''
题目: 综合应用顺序、选择、循环三种基本结构
要求掌握基本结构的应用方法

包括：
1. 顺序结构：赋值语句、注释语句、暂停语句和结束语句
2. 选择结构：单次、多次、嵌套选择结构
3. 循环结构：单重、双重循环结构
'''

import time
import random

def demonstrate_sequential_structure():
    """
    演示顺序结构
    """
    print("=== 顺序结构演示 ===")
    
    # 赋值语句
    a = 10
    b = 20
    c = a + b
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = a + b = {c}")
    
    # 注释语句（这里就是注释）
    # 这是单行注释
    """
    这是多行注释
    可以写多行内容
    """
    
    # 暂停语句
    print("程序暂停3秒...")
    time.sleep(3)  # 暂停3秒
    
    print("程序继续执行")
    
    # 结束语句（在函数中）
    print("顺序结构演示结束")
    return c

def demonstrate_single_selection():
    """
    演示单次选择结构
    """
    print("\n=== 单次选择结构演示 ===")
    
    # 基本if语句
    age = int(input("请输入年龄: "))
    
    if age >= 18:
        print("您已成年")
    
    # if-else语句
    score = int(input("请输入成绩: "))
    
    if score >= 60:
        print("及格")
    else:
        print("不及格")
    
    # 三元运算符
    result = "优秀" if score >= 90 else "良好" if score >= 80 else "一般"
    print(f"成绩等级: {result}")

def demonstrate_multiple_selection():
    """
    演示多次选择结构
    """
    print("\n=== 多次选择结构演示 ===")
    
    # if-elif-else语句
    score = int(input("请输入成绩: "))
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"成绩等级: {grade}")
    
    # 使用字典实现多分支选择
    grade_dict = {
        (90, 100): "优秀",
        (80, 89): "良好",
        (70, 79): "中等",
        (60, 69): "及格",
        (0, 59): "不及格"
    }
    
    for (min_score, max_score), description in grade_dict.items():
        if min_score <= score <= max_score:
            print(f"成绩描述: {description}")
            break

def demonstrate_nested_selection():
    """
    演示嵌套选择结构
    """
    print("\n=== 嵌套选择结构演示 ===")
    
    # 嵌套if语句
    age = int(input("请输入年龄: "))
    has_license = input("是否有驾照? (y/n): ").lower() == 'y'
    
    if age >= 18:
        if has_license:
            print("可以开车")
        else:
            print("需要先考驾照")
    else:
        print("年龄不够，不能开车")
    
    # 多层嵌套
    weather = input("请输入天气 (sunny/rainy/cloudy): ").lower()
    temperature = int(input("请输入温度: "))
    
    if weather == "sunny":
        if temperature > 30:
            print("天气很热，建议穿短袖")
        elif temperature > 20:
            print("天气温暖，可以穿长袖")
        else:
            print("天气凉爽，建议穿外套")
    elif weather == "rainy":
        if temperature > 15:
            print("下雨但不太冷，带雨伞")
        else:
            print("下雨且较冷，带雨伞和外套")
    else:
        print("多云天气，根据温度选择衣服")

def demonstrate_single_loop():
    """
    演示单重循环结构
    """
    print("\n=== 单重循环结构演示 ===")
    
    # for循环 - 遍历序列
    print("1. for循环遍历列表:")
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    for fruit in fruits:
        print(f"  {fruit}")
    
    # for循环 - 使用range
    print("\n2. for循环使用range:")
    for i in range(1, 6):
        print(f"  数字: {i}")
    
    # for循环 - 带步长
    print("\n3. for循环带步长:")
    for i in range(0, 10, 2):
        print(f"  偶数: {i}")
    
    # while循环
    print("\n4. while循环:")
    count = 0
    while count < 5:
        print(f"  计数: {count}")
        count += 1
    
    # while循环 - 条件控制
    print("\n5. while循环条件控制:")
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    
    print(f"猜一个1-100之间的数字")
    while guess != number and attempts < 10:
        guess = int(input("请输入你的猜测: "))
        attempts += 1
        
        if guess < number:
            print("太小了")
        elif guess > number:
            print("太大了")
        else:
            print(f"恭喜！你猜对了，用了{attempts}次")
    
    if guess != number:
        print(f"游戏结束，正确答案是{number}")

def demonstrate_double_loop():
    """
    演示双重循环结构
    """
    print("\n=== 双重循环结构演示 ===")
    
    # 双重for循环 - 打印乘法表
    print("1. 九九乘法表:")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j}", end="\t")
        print()  # 换行
    
    # 双重for循环 - 打印图案
    print("\n2. 打印三角形:")
    n = 5
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
    
    # 双重for循环 - 打印空心矩形
    print("\n3. 打印空心矩形:")
    width = 8
    height = 5
    
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
    # 双重while循环
    print("\n4. 双重while循环:")
    i = 1
    while i <= 3:
        j = 1
        while j <= 3:
            print(f"({i},{j})", end=" ")
            j += 1
        print()
        i += 1
    
    # 混合循环
    print("\n5. 混合循环:")
    for i in range(1, 4):
        j = 1
        while j <= i:
            print(f"{j}", end=" ")
            j += 1
        print()

def demonstrate_loop_control():
    """
    演示循环控制语句
    """
    print("\n=== 循环控制语句演示 ===")
    
    # break语句
    print("1. break语句 - 找到第一个偶数:")
    numbers = [1, 3, 5, 8, 9, 12, 15]
    for num in numbers:
        if num % 2 == 0:
            print(f"找到第一个偶数: {num}")
            break
        print(f"检查数字: {num}")
    
    # continue语句
    print("\n2. continue语句 - 跳过奇数:")
    for i in range(1, 11):
        if i % 2 == 1:
            continue
        print(f"偶数: {i}")
    
    # else子句
    print("\n3. else子句 - 循环正常结束:")
    for i in range(3):
        print(f"循环: {i}")
    else:
        print("循环正常结束")
    
    # 带break的else
    print("\n4. 带break的else:")
    for i in range(5):
        if i == 3:
            print(f"遇到{i}，提前退出")
            break
        print(f"循环: {i}")
    else:
        print("循环正常结束")

def demonstrate_comprehensive_example():
    """
    综合示例：学生成绩管理系统
    """
    print("\n=== 综合示例：学生成绩管理系统 ===")
    
    students = []
    
    while True:
        print("\n请选择操作:")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 计算平均分")
        print("4. 查找学生")
        print("5. 退出")
        
        choice = input("请输入选择 (1-5): ")
        
        if choice == "1":
            # 添加学生
            name = input("请输入学生姓名: ")
            scores = []
            
            # 输入多门成绩
            while True:
                score_input = input("请输入成绩 (输入'done'结束): ")
                if score_input.lower() == 'done':
                    break
                try:
                    score = float(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("成绩必须在0-100之间")
                except ValueError:
                    print("请输入有效的数字")
            
            if scores:
                student = {
                    'name': name,
                    'scores': scores,
                    'average': sum(scores) / len(scores)
                }
                students.append(student)
                print(f"学生 {name} 添加成功")
            else:
                print("没有输入有效成绩")
        
        elif choice == "2":
            # 查看所有学生
            if not students:
                print("没有学生信息")
            else:
                print(f"\n{'姓名':<10} {'成绩':<20} {'平均分':<8}")
                print("-" * 40)
                for student in students:
                    scores_str = ", ".join([f"{s:.1f}" for s in student['scores']])
                    print(f"{student['name']:<10} {scores_str:<20} {student['average']:<8.2f}")
        
        elif choice == "3":
            # 计算平均分
            if not students:
                print("没有学生信息")
            else:
                total_average = sum(student['average'] for student in students) / len(students)
                print(f"所有学生的平均分: {total_average:.2f}")
        
        elif choice == "4":
            # 查找学生
            search_name = input("请输入要查找的学生姓名: ")
            found = False
            
            for student in students:
                if search_name.lower() in student['name'].lower():
                    print(f"找到学生: {student['name']}")
                    print(f"成绩: {student['scores']}")
                    print(f"平均分: {student['average']:.2f}")
                    found = True
            
            if not found:
                print("未找到该学生")
        
        elif choice == "5":
            print("退出程序")
            break
        
        else:
            print("无效选择，请重新输入")

def main():
    """
    主函数
    """
    print("=== 基本结构控制结构应用演示 ===")
    
    # 演示各种结构
    demonstrate_sequential_structure()
    demonstrate_single_selection()
    demonstrate_multiple_selection()
    demonstrate_nested_selection()
    demonstrate_single_loop()
    demonstrate_double_loop()
    demonstrate_loop_control()
    
    # 综合示例
    demonstrate_comprehensive_example()

if __name__ == "__main__":
    main()

