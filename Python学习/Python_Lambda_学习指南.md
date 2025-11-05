# Python Lambda 函数学习指南

## 什么是 Lambda 函数？

Lambda 函数是 Python 中的**匿名函数**（没有名字的函数），它是一种创建简单函数的快捷方式。

## 基本语法

```python
lambda 参数: 表达式
```

## 1. 基础示例

### 普通函数 vs Lambda 函数

```python
# 普通函数
def add(x, y):
    return x + y

# Lambda 函数
add_lambda = lambda x, y: x + y

# 使用效果相同
print(add(3, 5))        # 输出: 8
print(add_lambda(3, 5)) # 输出: 8
```

### 简单示例

```python
# 计算平方
square = lambda x: x * x
print(square(5))  # 输出: 25

# 判断奇偶
is_even = lambda x: x % 2 == 0
print(is_even(4))  # 输出: True
print(is_even(3))  # 输出: False

# 获取字符串长度
get_length = lambda s: len(s)
print(get_length("Hello"))  # 输出: 5
```

## 2. 在列表操作中使用 Lambda

### map() 函数
```python
numbers = [1, 2, 3, 4, 5]

# 使用 lambda 计算平方
squares = list(map(lambda x: x * x, numbers))
print(squares)  # 输出: [1, 4, 9, 16, 25]

# 转换为字符串
strings = list(map(lambda x: str(x), numbers))
print(strings)  # 输出: ['1', '2', '3', '4', '5']
```

### filter() 函数
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6, 8, 10]

# 筛选大于5的数
big_numbers = list(filter(lambda x: x > 5, numbers))
print(big_numbers)  # 输出: [6, 7, 8, 9, 10]
```

## 3. 在排序中使用 Lambda

### 列表排序
```python
# 数字列表排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(key=lambda x: x)
print(numbers)  # 输出: [1, 1, 2, 3, 4, 5, 6, 9]

# 按绝对值排序
numbers = [-3, 1, -4, 1, 5, -9, 2, 6]
numbers.sort(key=lambda x: abs(x))
print(numbers)  # 输出: [1, 1, 2, -3, -4, 5, 6, -9]
```

### 字典列表排序
```python
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 19, "score": 92},
    {"name": "王五", "age": 21, "score": 78}
]

# 按年龄排序
students.sort(key=lambda student: student['age'])
print("按年龄排序:", students)

# 按分数排序（从高到低）
students.sort(key=lambda student: student['score'], reverse=True)
print("按分数排序:", students)

# 按姓名排序
students.sort(key=lambda student: student['name'])
print("按姓名排序:", students)
```

## 4. 多参数 Lambda

```python
# 两个参数
add = lambda x, y: x + y
print(add(3, 5))  # 输出: 8

# 三个参数
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 输出: 24

# 默认参数
power = lambda x, n=2: x ** n
print(power(5))    # 输出: 25 (默认平方)
print(power(5, 3)) # 输出: 125 (立方)
```

## 5. 条件表达式

```python
# 简单的条件判断
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # 输出: 20

# 判断正负数
sign = lambda x: "正数" if x > 0 else "负数" if x < 0 else "零"
print(sign(5))   # 输出: 正数
print(sign(-3))  # 输出: 负数
print(sign(0))   # 输出: 零
```

## 6. 实际应用场景

### 数据处理
```python
# 处理学生数据
students = [
    {"name": "张三", "age": 20, "courses": ["Python", "Math"]},
    {"name": "李四", "age": 19, "courses": ["Java", "Physics"]},
    {"name": "王五", "age": 22, "courses": ["C++", "Chemistry"]}
]

# 获取所有学生姓名
names = list(map(lambda s: s['name'], students))
print(names)  # 输出: ['张三', '李四', '王五']

# 获取年龄大于20的学生
adults = list(filter(lambda s: s['age'] > 20, students))
print(adults)  # 输出: [{'name': '王五', 'age': 22, 'courses': ['C++', 'Chemistry']}]

# 按年龄排序
students.sort(key=lambda s: s['age'])
print("按年龄排序:", students)
```

### 文件处理
```python
# 按文件大小排序
files = [
    {"name": "file1.txt", "size": 1024},
    {"name": "file2.txt", "size": 512},
    {"name": "file3.txt", "size": 2048}
]

files.sort(key=lambda f: f['size'])
print("按大小排序:", files)
```

## 7. Lambda 的优缺点

### 优点
- **简洁**: 一行代码完成简单功能
- **方便**: 不需要定义函数名
- **灵活**: 可以作为参数传递

### 缺点
- **可读性**: 复杂逻辑时不如普通函数清晰
- **调试困难**: 没有函数名，调试时不易定位
- **功能限制**: 只能包含表达式，不能包含语句

## 8. 什么时候使用 Lambda？

### 适合使用 Lambda 的场景：
```python
# 1. 简单的数学运算
square = lambda x: x * x

# 2. 简单的条件判断
is_positive = lambda x: x > 0

# 3. 作为其他函数的参数
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))

# 4. 简单的排序键
students.sort(key=lambda s: s['age'])
```

### 不适合使用 Lambda 的场景：
```python
# 复杂逻辑应该用普通函数
def complex_calculation(x, y, z):
    if x > 0:
        result = x * y + z
        if result > 100:
            return result * 0.9
        else:
            return result * 1.1
    else:
        return 0

# 不要写成复杂的 lambda
# complex_lambda = lambda x, y, z: x * y + z * 0.9 if x > 0 and x * y + z > 100 else x * y + z * 1.1 if x > 0 else 0
```

## 9. 练习题目

### 练习1：基础操作
```python
# 创建一个 lambda 函数，计算两个数的平均值
average = lambda x, y: (x + y) / 2
print(average(10, 20))  # 应该输出: 15.0
```

### 练习2：列表处理
```python
# 使用 lambda 和 map 将字符串列表转换为大写
words = ["hello", "world", "python"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)  # 应该输出: ['HELLO', 'WORLD', 'PYTHON']
```

### 练习3：排序
```python
# 按字符串长度排序
words = ["python", "java", "c", "javascript", "go"]
words.sort(key=lambda w: len(w))
print(words)  # 应该输出: ['c', 'go', 'java', 'python', 'javascript']
```

## 10. 总结

Lambda 函数是 Python 中一个强大的工具，特别适合：
- 简单的数学运算
- 作为其他函数的参数
- 数据处理和排序
- 函数式编程

记住：**如果逻辑复杂，还是用普通函数更好！**

---

**学习建议：**
1. 从简单的数学运算开始练习
2. 尝试在 `map()`, `filter()`, `sort()` 中使用 lambda
3. 逐步理解 lambda 在数据处理中的应用
4. 不要过度使用，保持代码可读性
