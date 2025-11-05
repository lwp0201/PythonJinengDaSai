# Python 面向对象学习指南

## 目录
1. [面向对象基础](#1-面向对象基础)
2. [Python中的"一切皆对象"](#2-python中的一切皆对象)
3. [类和对象](#3-类和对象)
4. [属性和方法](#4-属性和方法)
5. [继承](#5-继承)
6. [多态](#6-多态)
7. [封装](#7-封装)
8. [特殊方法](#8-特殊方法)
9. [装饰器在类中的应用](#9-装饰器在类中的应用)
10. [高级特性](#10-高级特性)
11. [设计模式](#11-设计模式)
12. [最佳实践](#12-最佳实践)

---

## 1. 面向对象基础

### 1.1 什么是面向对象编程？
面向对象编程（OOP）是一种编程范式，它将数据和操作数据的方法组织在一起，形成"对象"。

### 1.2 面向对象的三大特性
- **封装（Encapsulation）**：隐藏内部实现细节
- **继承（Inheritance）**：子类继承父类的特性
- **多态（Polymorphism）**：同一接口，不同实现

### 1.3 基本概念
```python
# 类（Class）：对象的模板
class Person:
    pass

# 对象（Object）：类的实例
person = Person()
```

---

## 2. Python中的"一切皆对象"

### 2.1 什么是"一切皆对象"？
在Python中，**一切皆对象**意味着所有的数据都是对象，包括：
- 数字、字符串、列表、字典等基本数据类型
- 函数、类、模块
- 甚至类型本身也是对象

### 2.2 基本数据类型也是对象
```python
# 数字是对象
num = 42
print(type(num))           # <class 'int'>
print(num.__class__)       # <class 'int'>
print(hasattr(num, '__add__'))  # True - 有加法方法

# 字符串是对象
text = "Hello"
print(type(text))          # <class 'str'>
print(text.upper())        # 调用字符串的方法
print(hasattr(text, 'upper'))  # True

# 列表是对象
my_list = [1, 2, 3]
print(type(my_list))       # <class 'list'>
print(my_list.append)      # <built-in method list.append>
```

### 2.3 函数也是对象
```python
def greet(name):
    return f"Hello, {name}!"

# 函数是对象，可以赋值给变量
my_function = greet
print(my_function("Alice"))  # 输出: Hello, Alice!

# 函数有属性
print(greet.__name__)       # 输出: greet
print(greet.__doc__)        # 输出: None
print(type(greet))          # <class 'function'>

# 函数可以作为参数传递
def apply_function(func, value):
    return func(value)

result = apply_function(greet, "Bob")
print(result)  # 输出: Hello, Bob!
```

### 2.4 类也是对象
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"Hello, I'm {self.name}"

# 类本身也是对象
print(type(Person))        # <class 'type'>
print(Person.__name__)     # 输出: Person
print(hasattr(Person, '__init__'))  # True

# 类可以动态创建
def create_person_class():
    class DynamicPerson:
        def __init__(self, name):
            self.name = name
    return DynamicPerson

DynamicPerson = create_person_class()
person = DynamicPerson("Charlie")
print(person.name)  # 输出: Charlie
```

### 2.5 类型也是对象
```python
# 类型本身也是对象
print(type(int))           # <class 'type'>
print(type(str))           # <class 'type'>
print(type(list))          # <class 'type'>

# 可以检查类型的类型
print(type(type))          # <class 'type'>
print(type(object))        # <class 'type'>

# 所有类型都继承自object
print(int.__bases__)       # (<class 'object'>,)
print(str.__bases__)       # (<class 'object'>,)
print(list.__bases__)      # (<class 'object'>,)
```

### 2.6 对象的方法和属性
```python
# 每个对象都有__class__属性
num = 42
print(num.__class__)       # <class 'int'>

# 每个对象都有__dict__属性（如果有的话）
class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(obj.__dict__)        # {'value': 10}

# 每个对象都有__str__和__repr__方法
print(str(42))             # 42
print(repr(42))            # 42
print(42.__str__())        # 42
print(42.__repr__())       # 42
```

### 2.7 动态属性访问
```python
class DynamicObject:
    def __init__(self):
        self.attributes = {}
    
    def __getattr__(self, name):
        """当属性不存在时调用"""
        if name in self.attributes:
            return self.attributes[name]
        return f"属性 {name} 不存在"
    
    def __setattr__(self, name, value):
        """设置属性时调用"""
        if name == 'attributes':
            super().__setattr__(name, value)
        else:
            self.attributes[name] = value

# 使用动态对象
obj = DynamicObject()
obj.name = "Alice"
obj.age = 25

print(obj.name)            # 输出: Alice
print(obj.age)             # 输出: 25
print(obj.nonexistent)     # 输出: 属性 nonexistent 不存在
```

### 2.8 对象身份和相等性
```python
# 对象身份（is操作符）
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)              # False - 不同的对象
print(a is c)              # True - 同一个对象
print(id(a) == id(c))      # True - 相同的ID

# 对象相等性（==操作符）
print(a == b)              # True - 内容相同
print(a == c)              # True - 内容相同

# 自定义相等性
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """自定义相等性比较"""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    
    def __hash__(self):
        """自定义哈希值"""
        return hash((self.name, self.age))

person1 = Person("Alice", 25)
person2 = Person("Alice", 25)
person3 = Person("Bob", 25)

print(person1 == person2)  # True - 内容相同
print(person1 == person3)  # False - 内容不同
print(person1 is person2)  # False - 不同对象
```

### 2.9 对象的生命周期
```python
class LifecycleDemo:
    def __new__(cls, *args, **kwargs):
        """对象创建时调用"""
        print("__new__ 被调用")
        return super().__new__(cls)
    
    def __init__(self, name):
        """对象初始化时调用"""
        print("__init__ 被调用")
        self.name = name
    
    def __del__(self):
        """对象销毁时调用"""
        print(f"__del__ 被调用，对象 {self.name} 被销毁")

# 创建对象
print("创建对象:")
obj = LifecycleDemo("测试对象")

# 删除对象
print("删除对象:")
del obj

# 强制垃圾回收
import gc
gc.collect()
```

### 2.10 元类（Metaclass）
```python
# 元类是创建类的类
class MyMeta(type):
    """自定义元类"""
    def __new__(cls, name, bases, attrs):
        print(f"创建类: {name}")
        # 为所有方法添加装饰
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                attrs[attr_name] = cls.add_logging(attr_value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def add_logging(func):
        """为方法添加日志"""
        def wrapper(*args, **kwargs):
            print(f"调用方法: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

# 使用元类创建类
class MyClass(metaclass=MyMeta):
    def method1(self):
        return "方法1"
    
    def method2(self):
        return "方法2"

# 使用类
obj = MyClass()
print(obj.method1())  # 输出: 调用方法: method1, 方法1
print(obj.method2())  # 输出: 调用方法: method2, 方法2
```

### 2.11 实际应用示例
```python
# 1. 函数式编程中的对象
def create_multiplier(factor):
    """创建乘法器函数"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15

# 2. 装饰器作为对象
class CountCalls:
    """计数装饰器类"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # 输出: 函数 greet 被调用了 1 次, Hello, Alice!
print(greet("Bob"))    # 输出: 函数 greet 被调用了 2 次, Hello, Bob!

# 3. 动态类创建
def create_class(class_name, methods):
    """动态创建类"""
    class_dict = {}
    for method_name, method_func in methods.items():
        class_dict[method_name] = method_func
    
    return type(class_name, (), class_dict)

# 动态创建类
methods = {
    'say_hello': lambda self: "Hello!",
    'say_goodbye': lambda self: "Goodbye!"
}

DynamicClass = create_class('DynamicClass', methods)
obj = DynamicClass()
print(obj.say_hello())    # 输出: Hello!
print(obj.say_goodbye())  # 输出: Goodbye!
```

### 2.12 "一切皆对象"的意义
```python
# 1. 统一性：所有数据都有相同的基本操作
def show_object_info(obj):
    """显示对象信息"""
    print(f"对象类型: {type(obj)}")
    print(f"对象ID: {id(obj)}")
    print(f"对象字符串表示: {str(obj)}")
    print(f"对象repr表示: {repr(obj)}")
    print(f"是否有__class__属性: {hasattr(obj, '__class__')}")
    print("---")

# 测试不同类型的对象
show_object_info(42)           # 整数
show_object_info("hello")      # 字符串
show_object_info([1, 2, 3])    # 列表
show_object_info({"a": 1})     # 字典
show_object_info(lambda x: x)  # 函数

# 2. 灵活性：可以像操作对象一样操作所有数据
def add_metadata(obj, key, value):
    """为对象添加元数据"""
    if not hasattr(obj, '_metadata'):
        obj._metadata = {}
    obj._metadata[key] = value

# 为任何对象添加元数据
num = 42
add_metadata(num, 'source', 'user_input')
add_metadata(num, 'timestamp', '2023-12-25')

print(num._metadata)  # 输出: {'source': 'user_input', 'timestamp': '2023-12-25'}
```

---

## 3. 类和对象

### 3.1 定义类
```python
class Person:
    """人类"""
    
    # 类属性
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """构造函数"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"

# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(person1.introduce())  # 输出: 我是张三，今年25岁
print(person2.introduce())  # 输出: 我是李四，今年30岁
```

### 3.2 构造函数和析构函数
```python
class Person:
    def __init__(self, name, age):
        """构造函数"""
        print(f"创建Person对象: {name}")
        self.name = name
        self.age = age
    
    def __del__(self):
        """析构函数"""
        print(f"销毁Person对象: {self.name}")

# 创建对象
person = Person("张三", 25)
del person  # 手动删除对象
```

### 3.3 类属性和实例属性
```python
class Person:
    # 类属性
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        Person.population += 1  # 增加人口计数
    
    @classmethod
    def get_population(cls):
        """获取人口总数"""
        return cls.population

# 访问类属性
print(f"物种: {Person.species}")
print(f"人口: {Person.get_population()}")

# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"人口: {Person.get_population()}")  # 输出: 2
```

---

## 4. 属性和方法

### 4.1 实例方法
```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x):
        """加法"""
        self.result += x
        return self
    
    def subtract(self, x):
        """减法"""
        self.result -= x
        return self
    
    def multiply(self, x):
        """乘法"""
        self.result *= x
        return self
    
    def get_result(self):
        """获取结果"""
        return self.result

# 链式调用
calc = Calculator()
result = calc.add(5).multiply(3).subtract(2).get_result()
print(result)  # 输出: 13
```

### 4.2 类方法
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """从字符串创建日期对象"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """获取今天的日期"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# 使用类方法
date1 = Date.from_string("2023-12-25")
date2 = Date.today()
print(date1)  # 输出: 2023-12-25
print(date2)  # 输出: 今天的日期
```

### 4.3 静态方法
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        """加法"""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """乘法"""
        return x * y
    
    @staticmethod
    def is_even(number):
        """判断是否为偶数"""
        return number % 2 == 0

# 使用静态方法
result = MathUtils.add(5, 3)
print(result)  # 输出: 8

is_even = MathUtils.is_even(4)
print(is_even)  # 输出: True
```

### 4.4 属性装饰器
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """获取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value
    
    @property
    def area(self):
        """计算面积"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """计算周长"""
        import math
        return 2 * math.pi * self._radius

# 使用属性
circle = Circle(5)
print(f"半径: {circle.radius}")
print(f"面积: {circle.area:.2f}")
print(f"周长: {circle.circumference:.2f}")

# 设置半径
circle.radius = 10
print(f"新半径: {circle.radius}")
```

---

## 5. 继承

### 5.1 基本继承
```python
class Animal:
    """动物基类"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "动物发出声音"
    
    def move(self):
        return f"{self.name}在移动"

class Dog(Animal):
    """狗类"""
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        return "汪汪汪"
    
    def fetch(self):
        return f"{self.name}在捡球"

class Cat(Animal):
    """猫类"""
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        return "喵喵喵"
    
    def climb(self):
        return f"{self.name}在爬树"

# 使用继承
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "橘色")

print(dog.make_sound())  # 输出: 汪汪汪
print(cat.make_sound())  # 输出: 喵喵喵
print(dog.fetch())       # 输出: 旺财在捡球
print(cat.climb())       # 输出: 咪咪在爬树
```

### 5.2 多重继承
```python
class Flyable:
    """可飞行接口"""
    def fly(self):
        return "飞行中"

class Swimmable:
    """可游泳接口"""
    def swim(self):
        return "游泳中"

class Duck(Animal, Flyable, Swimmable):
    """鸭子类"""
    def __init__(self, name):
        super().__init__(name, "鸭子")
    
    def make_sound(self):
        return "嘎嘎嘎"

# 使用多重继承
duck = Duck("唐老鸭")
print(duck.make_sound())  # 输出: 嘎嘎嘎
print(duck.fly())         # 输出: 飞行中
print(duck.swim())        # 输出: 游泳中
```

### 5.3 方法解析顺序（MRO）
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# 查看方法解析顺序
print(D.__mro__)  # 输出: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
print(d.method())  # 输出: B (按照MRO顺序)
```

---

## 6. 多态

### 6.1 基本多态
```python
class Shape:
    """形状基类"""
    def area(self):
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        raise NotImplementedError("子类必须实现perimeter方法")

class Rectangle(Shape):
    """矩形"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圆形"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 多态使用
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

for shape in shapes:
    print(f"面积: {shape.area():.2f}, 周长: {shape.perimeter():.2f}")
```

### 6.2 鸭子类型
```python
class Duck:
    def quack(self):
        return "嘎嘎嘎"
    
    def fly(self):
        return "飞行中"

class Person:
    def quack(self):
        return "模仿鸭子叫"
    
    def fly(self):
        return "坐飞机"

def make_sound_and_fly(animal):
    """鸭子类型：只要会quack和fly就行"""
    print(animal.quack())
    print(animal.fly())

# 使用鸭子类型
duck = Duck()
person = Person()

make_sound_and_fly(duck)    # 输出: 嘎嘎嘎, 飞行中
make_sound_and_fly(person)  # 输出: 模仿鸭子叫, 坐飞机
```

---

## 7. 封装

### 7.1 私有属性和方法
```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # 私有属性
        self.__transaction_history = []   # 私有属性
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +{amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"取款: -{amount}")
            return True
        return False
    
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    def get_transaction_history(self):
        """获取交易历史"""
        return self.__transaction_history.copy()  # 返回副本

# 使用封装
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)

print(f"余额: {account.get_balance()}")  # 输出: 余额: 1300
print(f"交易历史: {account.get_transaction_history()}")
```

### 6.2 属性访问控制
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# 使用属性控制
temp = Temperature(25)
print(f"摄氏度: {temp.celsius}")      # 输出: 摄氏度: 25
print(f"华氏度: {temp.fahrenheit}")    # 输出: 华氏度: 77.0

temp.fahrenheit = 86
print(f"摄氏度: {temp.celsius}")      # 输出: 摄氏度: 30.0
```

---

## 7. 特殊方法

### 7.1 字符串表示
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """用户友好的字符串表示"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """开发者友好的字符串表示"""
        return f"Person('{self.name}', {self.age})"

person = Person("张三", 25)
print(str(person))   # 输出: Person(name='张三', age=25)
print(repr(person))  # 输出: Person('张三', 25)
```

### 7.2 比较操作
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, other):
        """等于"""
        return self.score == other.score
    
    def __lt__(self, other):
        """小于"""
        return self.score < other.score
    
    def __le__(self, other):
        """小于等于"""
        return self.score <= other.score
    
    def __gt__(self, other):
        """大于"""
        return self.score > other.score
    
    def __ge__(self, other):
        """大于等于"""
        return self.score >= other.score
    
    def __ne__(self, other):
        """不等于"""
        return self.score != other.score

# 使用比较操作
student1 = Student("张三", 85)
student2 = Student("李四", 90)

print(student1 < student2)   # 输出: True
print(student1 == student2)  # 输出: False
print(student1 >= student2)  # 输出: False
```

### 7.3 算术操作
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """加法"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """减法"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """标量乘法"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# 使用算术操作
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)  # 输出: Vector(4, 6)
print(v1 - v2)  # 输出: Vector(2, 2)
print(v1 * 2)   # 输出: Vector(6, 8)
```

### 7.4 容器操作
```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __len__(self):
        """长度"""
        return len(self.items)
    
    def __getitem__(self, index):
        """索引访问"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """索引赋值"""
        self.items[index] = value
    
    def __contains__(self, item):
        """包含检查"""
        return item in self.items
    
    def __iter__(self):
        """迭代"""
        return iter(self.items)

# 使用容器操作
cart = ShoppingCart()
cart.add_item("苹果")
cart.add_item("香蕉")
cart.add_item("橙子")

print(len(cart))           # 输出: 3
print(cart[0])             # 输出: 苹果
print("苹果" in cart)      # 输出: True

for item in cart:
    print(item)            # 输出: 苹果, 香蕉, 橙子
```

---

## 8. 装饰器在类中的应用

### 8.1 类装饰器
```python
def singleton(cls):
    """单例装饰器"""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "数据库连接"
        print("创建数据库连接")

# 测试单例
db1 = Database()
db2 = Database()
print(db1 is db2)  # 输出: True
```

### 8.2 方法装饰器
```python
def log_method(func):
    """方法日志装饰器"""
    def wrapper(self, *args, **kwargs):
        print(f"调用方法: {func.__name__}")
        result = func(self, *args, **kwargs)
        print(f"方法 {func.__name__} 执行完成")
        return result
    return wrapper

class Calculator:
    @log_method
    def add(self, x, y):
        return x + y
    
    @log_method
    def multiply(self, x, y):
        return x * y

calc = Calculator()
result = calc.add(5, 3)  # 输出: 调用方法: add, 方法 add 执行完成
print(result)            # 输出: 8
```

### 8.3 属性装饰器
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("年龄必须是非负整数")
        self._age = value

person = Person("张三", 25)
person.age = 30
print(f"姓名: {person.name}, 年龄: {person.age}")
```

---

## 9. 高级特性

### 9.1 抽象基类
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """抽象形状类"""
    
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass
    
    def description(self):
        """描述形状"""
        return f"这是一个{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# 使用抽象基类
rect = Rectangle(5, 3)
print(rect.area())        # 输出: 15
print(rect.perimeter())   # 输出: 16
print(rect.description()) # 输出: 这是一个Rectangle
```

### 9.2 元类
```python
class SingletonMeta(type):
    """单例元类"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "数据库连接"

# 测试单例元类
db1 = Database()
db2 = Database()
print(db1 is db2)  # 输出: True
```

### 9.3 描述符
```python
class PositiveNumber:
    """正数描述符"""
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name}必须是正数")
        instance.__dict__[self.name] = value

class Rectangle:
    width = PositiveNumber('width')
    height = PositiveNumber('height')
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 使用描述符
rect = Rectangle(5, 3)
print(rect.area())  # 输出: 15

try:
    rect.width = -1  # 会抛出异常
except ValueError as e:
    print(e)  # 输出: width必须是正数
```

### 9.4 上下文管理器
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        print(f"连接到数据库 {self.host}:{self.port}")
        self.connection = f"连接对象-{self.host}:{self.port}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        self.connection = None
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")

# 使用上下文管理器
with DatabaseConnection("localhost", 5432) as conn:
    print(f"使用连接: {conn}")
    # 数据库操作
```

---

## 10. 设计模式

### 10.1 工厂模式
```python
class AnimalFactory:
    """动物工厂"""
    
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        elif animal_type == "duck":
            return Duck(name)
        else:
            raise ValueError(f"未知的动物类型: {animal_type}")

class Dog:
    def __init__(self, name):
        self.name = name
        self.sound = "汪汪汪"

class Cat:
    def __init__(self, name):
        self.name = name
        self.sound = "喵喵喵"

class Duck:
    def __init__(self, name):
        self.name = name
        self.sound = "嘎嘎嘎"

# 使用工厂模式
dog = AnimalFactory.create_animal("dog", "旺财")
cat = AnimalFactory.create_animal("cat", "咪咪")
print(f"{dog.name}: {dog.sound}")
print(f"{cat.name}: {cat.sound}")
```

### 10.2 观察者模式
```python
class Subject:
    """主题类"""
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    """观察者基类"""
    def update(self, message):
        raise NotImplementedError

class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email
    
    def update(self, message):
        print(f"发送邮件到 {self.email}: {message}")

class SMSObserver(Observer):
    def __init__(self, phone):
        self.phone = phone
    
    def update(self, message):
        print(f"发送短信到 {self.phone}: {message}")

# 使用观察者模式
subject = Subject()
email_observer = EmailObserver("user@example.com")
sms_observer = SMSObserver("1234567890")

subject.attach(email_observer)
subject.attach(sms_observer)

subject.notify("系统维护通知")
```

### 10.3 策略模式
```python
class PaymentStrategy:
    """支付策略基类"""
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"使用信用卡 {self.card_number} 支付 {amount} 元"

class AlipayPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account
    
    def pay(self, amount):
        return f"使用支付宝 {self.account} 支付 {amount} 元"

class WeChatPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account
    
    def pay(self, amount):
        return f"使用微信 {self.account} 支付 {amount} 元"

class PaymentProcessor:
    """支付处理器"""
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        return self.strategy.pay(amount)

# 使用策略模式
credit_card = CreditCardPayment("1234-5678-9012-3456")
processor = PaymentProcessor(credit_card)
result = processor.process_payment(100)
print(result)
```

---

## 11. 最佳实践

### 11.1 类设计原则
```python
# 1. 单一职责原则
class User:
    """用户类 - 只负责用户信息"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    """用户仓库类 - 只负责用户数据操作"""
    def save(self, user):
        # 保存用户到数据库
        pass
    
    def find_by_email(self, email):
        # 根据邮箱查找用户
        pass

# 2. 开闭原则
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 3. 里氏替换原则
class Bird:
    def fly(self):
        return "飞行中"

class Eagle(Bird):
    def fly(self):
        return "老鹰在飞行"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("企鹅不会飞")
```

### 11.2 命名规范
```python
class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number, initial_balance=0):
        # 私有属性使用下划线前缀
        self._account_number = account_number
        self._balance = initial_balance
        self._transaction_history = []
    
    def deposit(self, amount):
        """存款方法"""
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"存款: +{amount}")
            return True
        return False
    
    def get_balance(self):
        """获取余额"""
        return self._balance
    
    def get_transaction_history(self):
        """获取交易历史"""
        return self._transaction_history.copy()
```

### 11.3 文档字符串
```python
class Calculator:
    """计算器类
    
    提供基本的数学运算功能，包括加法、减法、乘法和除法。
    
    属性:
        result (float): 当前计算结果
    
    示例:
        >>> calc = Calculator()
        >>> calc.add(5).multiply(3).get_result()
        15.0
    """
    
    def __init__(self):
        """初始化计算器"""
        self.result = 0
    
    def add(self, value):
        """加法运算
        
        参数:
            value (float): 要加的数
        
        返回:
            Calculator: 返回自身以支持链式调用
        """
        self.result += value
        return self
    
    def multiply(self, value):
        """乘法运算
        
        参数:
            value (float): 要乘的数
        
        返回:
            Calculator: 返回自身以支持链式调用
        """
        self.result *= value
        return self
```

### 11.4 类型提示
```python
from typing import List, Dict, Optional, Union

class Student:
    """学生类"""
    
    def __init__(self, name: str, age: int, grades: Optional[List[float]] = None):
        self.name: str = name
        self.age: int = age
        self.grades: List[float] = grades or []
    
    def add_grade(self, grade: float) -> None:
        """添加成绩"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
    
    def get_average_grade(self) -> float:
        """获取平均成绩"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_grade_report(self) -> Dict[str, Union[str, float]]:
        """获取成绩报告"""
        return {
            'name': self.name,
            'average': self.get_average_grade(),
            'total_grades': len(self.grades)
        }
```

### 11.5 测试友好设计
```python
class EmailService:
    """邮件服务类"""
    
    def __init__(self, smtp_server: str, port: int):
        self.smtp_server = smtp_server
        self.port = port
        self._connection = None
    
    def connect(self) -> bool:
        """连接SMTP服务器"""
        try:
            # 模拟连接
            self._connection = f"连接到 {self.smtp_server}:{self.port}"
            return True
        except Exception:
            return False
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """发送邮件"""
        if not self._connection:
            return False
        
        # 模拟发送邮件
        print(f"发送邮件到 {to}: {subject}")
        return True

# 测试友好的设计
def test_email_service():
    """测试邮件服务"""
    service = EmailService("smtp.example.com", 587)
    
    # 测试连接
    assert service.connect() == True
    
    # 测试发送邮件
    assert service.send_email("test@example.com", "测试", "测试内容") == True

# 运行测试
test_email_service()
print("所有测试通过！")
```

---

## 总结

Python面向对象编程是构建复杂应用程序的重要技能。掌握好面向对象编程需要理解以下要点：

1. **理解三大特性**：封装、继承、多态
2. **合理使用继承**：避免过深的继承层次
3. **重视封装**：保护内部实现
4. **善用特殊方法**：让类更易用
5. **遵循设计原则**：编写可维护的代码
6. **使用类型提示**：提高代码可读性
7. **编写测试**：确保代码质量

通过不断练习和实践，您将能够熟练运用Python面向对象编程，构建出优雅、可维护的应用程序！
