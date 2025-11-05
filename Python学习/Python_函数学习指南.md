# Python 函数学习指南

## 目录
1. [函数基础](#1-函数基础)
2. [函数参数](#2-函数参数)
3. [返回值](#3-返回值)
4. [作用域](#4-作用域)
5. [高级特性](#5-高级特性)
6. [装饰器](#6-装饰器)
7. [生成器](#7-生成器)
8. [递归](#8-递归)
9. [内置函数](#9-内置函数)
10. [最佳实践](#10-最佳实践)

---

## 1. 函数基础

### 1.1 什么是函数？
函数是一段可重复使用的代码块，用于执行特定的任务。

### 1.2 定义函数
```python
def function_name(parameters):
    """函数文档字符串"""
    # 函数体
    return result
```

### 1.3 基本示例
```python
# 简单函数
def greet():
    print("Hello, World!")

# 带参数的函数
def greet_person(name):
    print(f"Hello, {name}!")

# 带返回值的函数
def add(a, b):
    return a + b

# 调用函数
greet()                    # 输出: Hello, World!
greet_person("Alice")      # 输出: Hello, Alice!
result = add(3, 5)         # result = 8
print(result)
```

### 1.4 函数文档字符串
```python
def calculate_area(length, width):
    """
    计算矩形面积
    
    参数:
        length (float): 长度
        width (float): 宽度
    
    返回:
        float: 面积
    """
    return length * width

# 查看函数文档
print(calculate_area.__doc__)
help(calculate_area)
```

---

## 2. 函数参数

### 2.1 位置参数
```python
def power(base, exponent):
    return base ** exponent

result = power(2, 3)  # 2^3 = 8
print(result)
```

### 2.2 关键字参数
```python
def power(base, exponent):
    return base ** exponent

# 使用关键字参数
result = power(exponent=3, base=2)  # 顺序可以改变
print(result)
```

### 2.3 默认参数
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # 输出: Hello, Alice!
greet("Bob", "Hi")       # 输出: Hi, Bob!
greet("Charlie", greeting="Good morning")  # 输出: Good morning, Charlie!
```

### 2.4 可变参数 *args
```python
def sum_all(*args):
    """计算所有参数的和"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))           # 输出: 6
print(sum_all(1, 2, 3, 4, 5))     # 输出: 15
print(sum_all())                  # 输出: 0
```

### 2.5 关键字参数 **kwargs
```python
def print_info(**kwargs):
    """打印所有关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")
# 输出:
# name: Alice
# age: 25
# city: Beijing
```

### 2.6 参数组合
```python
def complex_function(a, b, c=10, *args, **kwargs):
    """
    参数组合示例
    a, b: 必需的位置参数
    c: 默认参数
    *args: 可变位置参数
    **kwargs: 可变关键字参数
    """
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

complex_function(1, 2, 3, 4, 5, name="Alice", age=25)
# 输出:
# a=1, b=2, c=3
# args=(4, 5)
# kwargs={'name': 'Alice', 'age': 25}
```

### 2.7 参数解包
```python
def multiply(x, y, z):
    return x * y * z

# 使用列表解包
numbers = [2, 3, 4]
result = multiply(*numbers)  # 等同于 multiply(2, 3, 4)
print(result)  # 输出: 24

# 使用字典解包
params = {'x': 2, 'y': 3, 'z': 4}
result = multiply(**params)  # 等同于 multiply(x=2, y=3, z=4)
print(result)  # 输出: 24
```

---

## 3. 返回值

### 3.1 单个返回值
```python
def square(x):
    return x * x

result = square(5)
print(result)  # 输出: 25
```

### 3.2 多个返回值
```python
def divide_and_remainder(a, b):
    """返回商和余数"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(17, 5)
print(f"商: {q}, 余数: {r}")  # 输出: 商: 3, 余数: 2

# 也可以作为一个元组接收
result = divide_and_remainder(17, 5)
print(result)  # 输出: (3, 2)
```

### 3.3 返回None
```python
def print_message(msg):
    print(msg)
    # 没有return语句，默认返回None

result = print_message("Hello")
print(result)  # 输出: None
```

### 3.4 条件返回
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(85))  # 输出: B
```

---

## 4. 作用域

### 4.1 局部作用域
```python
def my_function():
    local_var = "我是局部变量"
    print(local_var)

my_function()
# print(local_var)  # 错误！局部变量在函数外不可访问
```

### 4.2 全局作用域
```python
global_var = "我是全局变量"

def my_function():
    print(global_var)  # 可以访问全局变量

my_function()
print(global_var)  # 也可以访问
```

### 4.3 修改全局变量
```python
counter = 0

def increment():
    global counter  # 声明使用全局变量
    counter += 1

increment()
print(counter)  # 输出: 1
```

### 4.4 嵌套作用域
```python
def outer_function():
    outer_var = "外部变量"
    
    def inner_function():
        nonlocal outer_var  # 声明使用外部函数的变量
        outer_var = "修改后的外部变量"
        print(f"内部函数: {outer_var}")
    
    inner_function()
    print(f"外部函数: {outer_var}")

outer_function()
# 输出:
# 内部函数: 修改后的外部变量
# 外部函数: 修改后的外部变量
```

---

## 5. 高级特性

### 5.1 函数作为参数
```python
def apply_operation(x, y, operation):
    """将操作函数应用到两个数上"""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)
print(result1)  # 输出: 8
print(result2)  # 输出: 15
```

### 5.2 函数作为返回值
```python
def create_multiplier(n):
    """创建一个乘法器函数"""
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15
```

### 5.3 闭包
```python
def outer_function(x):
    def inner_function(y):
        return x + y  # 内部函数可以访问外部函数的变量
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # 输出: 15
```

### 5.4 高阶函数
```python
# map函数
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)  # 输出: [1, 4, 9, 16, 25]

# filter函数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4]

# reduce函数
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 输出: 15
```

---

## 6. 装饰器

### 6.1 简单装饰器
```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 函数执行前
# Hello!
# 函数执行后
```

### 6.2 带参数的装饰器
```python
def decorator_with_args(*args, **kwargs):
    def decorator(func):
        def wrapper(*func_args, **func_kwargs):
            print(f"装饰器参数: {args}, {kwargs}")
            return func(*func_args, **func_kwargs)
        return wrapper
    return decorator

@decorator_with_args("test", debug=True)
def my_function(x, y):
    return x + y

result = my_function(3, 5)
print(result)
```

### 6.3 类装饰器
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

### 6.4 内置装饰器
```python
class MyClass:
    def __init__(self):
        self._value = 0
    
    @property
    def value(self):
        """获取值"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """设置值"""
        if new_value < 0:
            raise ValueError("值不能为负数")
        self._value = new_value
    
    @staticmethod
    def static_method():
        """静态方法"""
        return "这是静态方法"
    
    @classmethod
    def class_method(cls):
        """类方法"""
        return f"这是 {cls.__name__} 的类方法"

obj = MyClass()
obj.value = 10
print(obj.value)  # 输出: 10
print(MyClass.static_method())  # 输出: 这是静态方法
print(MyClass.class_method())   # 输出: 这是 MyClass 的类方法
```

---

## 7. 生成器

### 7.1 生成器函数
```python
def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

# 使用生成器
counter = count_up_to(5)
for num in counter:
    print(num)  # 输出: 1, 2, 3, 4, 5
```

### 7.2 生成器表达式
```python
# 生成器表达式
squares = (x * x for x in range(5))
print(list(squares))  # 输出: [0, 1, 4, 9, 16]

# 等价于生成器函数
def squares_func():
    for x in range(5):
        yield x * x

squares2 = squares_func()
print(list(squares2))  # 输出: [0, 1, 4, 9, 16]
```

### 7.3 生成器的优势
```python
def fibonacci(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 内存效率高，只在需要时计算
fib = fibonacci(10)
for num in fib:
    print(num, end=" ")  # 输出: 0 1 1 2 3 5 8 13 21 34
```

---

## 8. 递归

### 8.1 基本递归
```python
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 输出: 120
```

### 8.2 尾递归优化
```python
def factorial_tail(n, accumulator=1):
    """尾递归版本的阶乘"""
    if n <= 1:
        return accumulator
    else:
        return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(5))  # 输出: 120
```

### 8.3 递归深度限制
```python
import sys

def deep_recursion(n):
    if n <= 0:
        return 0
    return 1 + deep_recursion(n - 1)

# 查看递归深度限制
print(f"递归深度限制: {sys.getrecursionlimit()}")

# 修改递归深度限制
sys.setrecursionlimit(2000)
print(f"新的递归深度限制: {sys.getrecursionlimit()}")
```

### 8.4 递归应用示例
```python
def binary_search(arr, target, left=0, right=None):
    """二分查找的递归实现"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(numbers, 7)
print(f"找到目标在索引: {result}")  # 输出: 找到目标在索引: 3
```

---

## 9. 内置函数

### 9.1 数学函数
```python
# abs() - 绝对值
print(abs(-5))  # 输出: 5

# max() - 最大值
print(max(1, 5, 3, 9, 2))  # 输出: 9

# min() - 最小值
print(min(1, 5, 3, 9, 2))  # 输出: 1

# sum() - 求和
print(sum([1, 2, 3, 4, 5]))  # 输出: 15

# pow() - 幂运算
print(pow(2, 3))  # 输出: 8

# round() - 四舍五入
print(round(3.14159, 2))  # 输出: 3.14
```

### 9.2 类型转换函数
```python
# int() - 转换为整数
print(int("123"))  # 输出: 123
print(int(3.14))   # 输出: 3

# float() - 转换为浮点数
print(float("3.14"))  # 输出: 3.14
print(float(123))     # 输出: 123.0

# str() - 转换为字符串
print(str(123))    # 输出: "123"
print(str(3.14))   # 输出: "3.14"

# bool() - 转换为布尔值
print(bool(1))     # 输出: True
print(bool(0))     # 输出: False
print(bool(""))    # 输出: False
print(bool("abc")) # 输出: True
```

### 9.3 序列函数
```python
# len() - 获取长度
print(len("Hello"))     # 输出: 5
print(len([1, 2, 3]))   # 输出: 3

# sorted() - 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))  # 输出: [1, 1, 2, 3, 4, 5, 6, 9]

# reversed() - 反转
print(list(reversed([1, 2, 3, 4])))  # 输出: [4, 3, 2, 1]

# enumerate() - 枚举
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
# 输出:
# 0: a
# 1: b
# 2: c

# zip() - 打包
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
# 输出:
# Alice: 25
# Bob: 30
# Charlie: 35
```

### 9.4 其他有用函数
```python
# all() - 所有元素为真
print(all([True, True, True]))   # 输出: True
print(all([True, False, True]))  # 输出: False

# any() - 任一元素为真
print(any([False, False, True]))  # 输出: True
print(any([False, False, False])) # 输出: False

# isinstance() - 类型检查
print(isinstance(123, int))      # 输出: True
print(isinstance("hello", str))  # 输出: True

# hasattr() - 检查属性
class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(hasattr(obj, 'value'))  # 输出: True
print(hasattr(obj, 'name'))   # 输出: False
```

---

## 10. 最佳实践

### 10.1 函数命名规范
```python
# 使用小写字母和下划线
def calculate_total_price():
    pass

def get_user_info():
    pass

def is_valid_email():
    pass
```

### 10.2 函数长度
```python
# 好的做法：函数简短，职责单一
def validate_email(email):
    """验证邮箱格式"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_email(to, subject, body):
    """发送邮件"""
    # 发送邮件的逻辑
    pass

# 不好的做法：函数过长，职责过多
def process_user_registration(user_data):
    # 验证数据
    # 检查邮箱
    # 发送邮件
    # 保存到数据库
    # 记录日志
    # ... 太多职责
    pass
```

### 10.3 错误处理
```python
def safe_divide(a, b):
    """安全除法"""
    try:
        return a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：参数类型不正确")
        return None

result = safe_divide(10, 0)  # 输出: 错误：除数不能为零
```

### 10.4 文档字符串
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=12):
    """
    计算复利
    
    参数:
        principal (float): 本金
        rate (float): 年利率（小数形式，如0.05表示5%）
        time (float): 时间（年）
        compound_frequency (int): 复利频率（每年复利次数，默认12次）
    
    返回:
        float: 最终金额
    
    示例:
        >>> calculate_compound_interest(1000, 0.05, 2)
        1104.7130674412967
    """
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return amount
```

### 10.5 类型提示
```python
from typing import List, Dict, Optional

def process_students(students: List[Dict[str, any]]) -> Dict[str, int]:
    """
    处理学生数据
    
    参数:
        students: 学生列表，每个学生是包含姓名和分数的字典
    
    返回:
        包含统计信息的字典
    """
    total_students = len(students)
    total_score = sum(student.get('score', 0) for student in students)
    average_score = total_score / total_students if total_students > 0 else 0
    
    return {
        'total_students': total_students,
        'total_score': total_score,
        'average_score': average_score
    }
```

### 10.6 函数式编程风格
```python
# 使用函数式编程风格
def is_even(x):
    return x % 2 == 0

def square(x):
    return x * x

# 链式操作
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(map(square, filter(is_even, numbers)))
print(result)  # 输出: 220 (2^2 + 4^2 + 6^2 + 8^2 + 10^2)
```

---

## 总结

Python函数是编程的核心概念，掌握好函数的使用对于编写高质量代码至关重要。记住以下要点：

1. **函数应该职责单一**：一个函数只做一件事
2. **使用有意义的名称**：函数名应该清楚表达其功能
3. **编写文档字符串**：帮助他人理解函数的作用
4. **合理使用参数**：根据需要使用不同类型的参数
5. **处理异常**：确保函数的健壮性
6. **避免过深的递归**：注意递归深度限制
7. **使用类型提示**：提高代码可读性和维护性

通过不断练习和实践，您将能够熟练运用Python函数，编写出更加优雅和高效的代码！
