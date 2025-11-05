# Python 异常处理学习指南

## 目录
1. [异常处理基础](#1-异常处理基础)
2. [常见异常类型](#2-常见异常类型)
3. [try-except语句](#3-try-except语句)
4. [finally和else子句](#4-finally和else子句)
5. [自定义异常](#5-自定义异常)
6. [异常链和上下文管理](#6-异常链和上下文管理)
7. [日志记录](#7-日志记录)
8. [最佳实践](#8-最佳实践)
9. [实际应用](#9-实际应用)
10. [高级技巧](#10-高级技巧)

---

## 1. 异常处理基础

### 1.1 什么是异常？
异常是程序运行时发生的错误，它会中断正常的程序执行流程。

### 1.2 异常处理的重要性
```python
# 没有异常处理的代码
def divide_numbers(a, b):
    return a / b

# 如果b为0，程序会崩溃
result = divide_numbers(10, 0)  # ZeroDivisionError: division by zero
print("这行代码不会执行")
```

### 1.3 基本异常处理
```python
# 使用try-except处理异常
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None

result = safe_divide(10, 0)
print(f"结果: {result}")  # 输出: 错误：除数不能为零, 结果: None
print("程序继续执行")
```

---

## 2. 常见异常类型

### 2.1 内置异常类型
```python
# 1. 语法错误 (SyntaxError)
# 这些错误在程序运行前就会被发现
# print("Hello World"  # 缺少右括号

# 2. 运行时错误
try:
    # NameError - 名称错误
    print(undefined_variable)
except NameError as e:
    print(f"名称错误: {e}")

try:
    # TypeError - 类型错误
    result = "hello" + 5
except TypeError as e:
    print(f"类型错误: {e}")

try:
    # ValueError - 值错误
    number = int("abc")
except ValueError as e:
    print(f"值错误: {e}")

try:
    # IndexError - 索引错误
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"索引错误: {e}")

try:
    # KeyError - 键错误
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"键错误: {e}")

try:
    # AttributeError - 属性错误
    my_string = "hello"
    my_string.append("world")
except AttributeError as e:
    print(f"属性错误: {e}")

try:
    # FileNotFoundError - 文件未找到
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"文件未找到: {e}")

try:
    # ZeroDivisionError - 除零错误
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
```

### 2.2 异常层次结构
```python
# 查看异常层次结构
import builtins

def print_exception_hierarchy(exception_class, indent=0):
    """打印异常层次结构"""
    print("  " * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 1)

# 打印部分异常层次结构
print("异常层次结构:")
print_exception_hierarchy(Exception)
```

### 2.3 异常信息获取
```python
def analyze_exception():
    """分析异常信息"""
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"异常类型: {type(e).__name__}")
        print(f"异常信息: {e}")
        print(f"异常参数: {e.args}")
        
        # 获取异常详细信息
        import traceback
        print("详细错误信息:")
        traceback.print_exc()

analyze_exception()
```

---

## 3. try-except语句

### 3.1 基本语法
```python
# 基本try-except结构
try:
    # 可能出错的代码
    risky_code()
except ExceptionType:
    # 处理特定异常
    handle_exception()
```

### 3.2 捕获多个异常
```python
def process_data(data):
    """处理数据，捕获多种异常"""
    try:
        # 尝试转换为整数
        number = int(data)
        # 尝试除法运算
        result = 100 / number
        return result
    except ValueError:
        print("错误：无法转换为整数")
        return None
    except ZeroDivisionError:
        print("错误：除数为零")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 测试不同情况
print(process_data("10"))    # 正常情况
print(process_data("abc"))   # ValueError
print(process_data("0"))     # ZeroDivisionError
```

### 3.3 捕获多个异常类型
```python
def safe_operation(x, y):
    """安全操作，捕获多种异常"""
    try:
        result = x / y
        return result
    except (ZeroDivisionError, TypeError) as e:
        print(f"操作错误: {e}")
        return None
    except Exception as e:
        print(f"其他错误: {e}")
        return None

# 测试
print(safe_operation(10, 2))    # 正常
print(safe_operation(10, 0))    # ZeroDivisionError
print(safe_operation("10", 2))  # TypeError
```

### 3.4 捕获所有异常
```python
def risky_function():
    """可能出错的函数"""
    try:
        # 可能出错的代码
        data = {"key": "value"}
        result = data["nonexistent_key"]
        return result
    except Exception as e:
        print(f"捕获到异常: {type(e).__name__}: {e}")
        return None

risky_function()
```

---

## 4. finally和else子句

### 4.1 finally子句
```python
def file_operation(filename):
    """文件操作示例"""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"文件内容: {content}")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except PermissionError:
        print(f"没有权限访问文件 {filename}")
    finally:
        # 无论是否发生异常，都会执行
        if file:
            file.close()
            print("文件已关闭")

# 测试
file_operation("test.txt")
```

### 4.2 else子句
```python
def divide_with_else(a, b):
    """使用else子句的除法"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数为零，无法计算")
        return None
    else:
        # 只有在没有异常时才执行
        print("计算成功")
        return result
    finally:
        # 无论是否发生异常都执行
        print("计算完成")

print(divide_with_else(10, 2))  # 正常情况
print(divide_with_else(10, 0))  # 异常情况
```

### 4.3 完整示例
```python
def process_user_input():
    """处理用户输入"""
    while True:
        try:
            user_input = input("请输入一个数字 (输入'quit'退出): ")
            if user_input.lower() == 'quit':
                break
            
            number = float(user_input)
            
        except ValueError:
            print("错误：请输入有效的数字")
            continue
        except KeyboardInterrupt:
            print("\n程序被用户中断")
            break
        else:
            # 只有在没有异常时才执行
            print(f"您输入的数字是: {number}")
            print(f"数字的平方是: {number ** 2}")
        finally:
            # 每次循环都执行
            print("-" * 30)

# process_user_input()  # 取消注释以运行
```

---

## 5. 自定义异常

### 5.1 创建自定义异常
```python
# 自定义异常类
class CustomError(Exception):
    """自定义异常基类"""
    pass

class ValidationError(CustomError):
    """验证错误"""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

class BusinessLogicError(CustomError):
    """业务逻辑错误"""
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

# 使用自定义异常
def validate_age(age):
    """验证年龄"""
    if not isinstance(age, int):
        raise ValidationError("年龄必须是整数", "age")
    if age < 0:
        raise ValidationError("年龄不能为负数", "age")
    if age > 150:
        raise ValidationError("年龄不能超过150岁", "age")
    return True

def process_user(user_data):
    """处理用户数据"""
    try:
        validate_age(user_data.get("age"))
        print("用户数据验证通过")
    except ValidationError as e:
        print(f"验证失败: {e.message} (字段: {e.field})")
    except Exception as e:
        print(f"其他错误: {e}")

# 测试
process_user({"age": 25})      # 正常
process_user({"age": -5})      # 负数
process_user({"age": "abc"})   # 非整数
```

### 5.2 异常链
```python
class DatabaseError(Exception):
    """数据库错误"""
    pass

class ConnectionError(DatabaseError):
    """连接错误"""
    pass

def connect_to_database():
    """连接数据库"""
    try:
        # 模拟连接失败
        raise ConnectionError("无法连接到数据库服务器")
    except ConnectionError as e:
        # 重新抛出异常，保留原始异常信息
        raise DatabaseError("数据库操作失败") from e

def handle_database_operation():
    """处理数据库操作"""
    try:
        connect_to_database()
    except DatabaseError as e:
        print(f"数据库错误: {e}")
        print(f"原始错误: {e.__cause__}")

handle_database_operation()
```

### 5.3 异常装饰器
```python
def handle_exceptions(exceptions=(Exception,)):
    """异常处理装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f"函数 {func.__name__} 发生异常: {e}")
                return None
        return wrapper
    return decorator

@handle_exceptions((ValueError, TypeError))
def risky_function(x, y):
    """可能出错的函数"""
    return x / y

# 测试装饰器
print(risky_function(10, 2))    # 正常
print(risky_function(10, 0))    # 被装饰器捕获
print(risky_function("10", 2)) # 被装饰器捕获
```

---

## 6. 异常链和上下文管理

### 6.1 异常链
```python
def read_config_file(filename):
    """读取配置文件"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"配置文件 {filename} 不存在") from e

class ConfigurationError(Exception):
    """配置错误"""
    pass

def load_application():
    """加载应用程序"""
    try:
        config = read_config_file("config.txt")
        print("应用程序加载成功")
    except ConfigurationError as e:
        print(f"配置错误: {e}")
        print(f"原始错误: {e.__cause__}")

# load_application()
```

### 6.2 上下文管理器
```python
class DatabaseConnection:
    """数据库连接上下文管理器"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        """进入上下文"""
        try:
            print(f"连接到数据库 {self.host}:{self.port}")
            self.connection = f"连接对象-{self.host}:{self.port}"
            return self.connection
        except Exception as e:
            print(f"连接失败: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.connection:
            print("关闭数据库连接")
            self.connection = None
        
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")
            # 返回False表示不抑制异常
            return False

# 使用上下文管理器
try:
    with DatabaseConnection("localhost", 5432) as conn:
        print(f"使用连接: {conn}")
        # 模拟数据库操作
        print("执行数据库查询")
except Exception as e:
    print(f"数据库操作失败: {e}")
```

### 6.3 异常上下文
```python
import contextlib

@contextlib.contextmanager
def safe_file_operation(filename, mode='r'):
    """安全的文件操作上下文管理器"""
    file = None
    try:
        print(f"打开文件: {filename}")
        file = open(filename, mode)
        yield file
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        yield None
    except PermissionError:
        print(f"没有权限访问文件 {filename}")
        yield None
    finally:
        if file:
            print("关闭文件")
            file.close()

# 使用上下文管理器
with safe_file_operation("test.txt") as f:
    if f:
        content = f.read()
        print(f"文件内容: {content}")
```

---

## 7. 日志记录

### 7.1 基本日志记录
```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_data(data):
    """处理数据并记录日志"""
    try:
        logger.info(f"开始处理数据: {data}")
        result = int(data) * 2
        logger.info(f"数据处理成功，结果: {result}")
        return result
    except ValueError as e:
        logger.error(f"数据格式错误: {e}")
        return None
    except Exception as e:
        logger.exception(f"处理数据时发生未知错误: {e}")
        return None

# 测试日志记录
process_data("10")
process_data("abc")
```

### 7.2 高级日志配置
```python
import logging
import logging.handlers
import os

def setup_logging():
    """设置高级日志配置"""
    # 创建日志目录
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # 创建logger
    logger = logging.getLogger("application")
    logger.setLevel(logging.DEBUG)
    
    # 创建文件处理器
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, "app.log"),
        maxBytes=1024*1024,  # 1MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    
    # 创建格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 使用高级日志
logger = setup_logging()

def risky_operation():
    """有风险的操作"""
    try:
        logger.info("开始执行有风险的操作")
        # 模拟可能出错的操作
        result = 10 / 0
        logger.info("操作成功完成")
        return result
    except ZeroDivisionError as e:
        logger.error(f"除零错误: {e}")
        return None
    except Exception as e:
        logger.exception(f"未知错误: {e}")
        return None

risky_operation()
```

---

## 8. 最佳实践

### 8.1 异常处理原则
```python
# 1. 具体异常优于通用异常
def good_exception_handling():
    """好的异常处理示例"""
    try:
        data = {"key": "value"}
        value = data["nonexistent_key"]
    except KeyError as e:
        print(f"键不存在: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

# 2. 不要忽略异常
def bad_exception_handling():
    """不好的异常处理示例"""
    try:
        risky_operation()
    except:
        pass  # 不要这样做！

# 3. 提供有意义的错误信息
def meaningful_error_handling():
    """提供有意义的错误信息"""
    try:
        age = int(input("请输入年龄: "))
        if age < 0:
            raise ValueError("年龄不能为负数")
        return age
    except ValueError as e:
        print(f"输入错误: {e}")
        return None
```

### 8.2 异常处理模式
```python
# 1. 重试模式
import time
import random

def retry_operation(max_attempts=3, delay=1):
    """重试操作装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        print(f"操作失败，已重试 {max_attempts} 次: {e}")
                        raise
                    print(f"第 {attempt + 1} 次尝试失败: {e}，{delay}秒后重试")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=1)
def unreliable_operation():
    """不可靠的操作"""
    if random.random() < 0.7:  # 70%的概率失败
        raise Exception("随机失败")
    return "操作成功"

# 测试重试机制
try:
    result = unreliable_operation()
    print(result)
except Exception as e:
    print(f"最终失败: {e}")
```

### 8.3 资源管理
```python
class ResourceManager:
    """资源管理器"""
    
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.resource = None
    
    def __enter__(self):
        try:
            print(f"获取资源: {self.resource_name}")
            self.resource = f"资源-{self.resource_name}"
            return self.resource
        except Exception as e:
            print(f"获取资源失败: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            print(f"释放资源: {self.resource_name}")
            self.resource = None
        
        if exc_type:
            print(f"资源使用过程中发生异常: {exc_type.__name__}: {exc_val}")
        
        # 返回False表示不抑制异常
        return False

# 使用资源管理器
try:
    with ResourceManager("数据库连接") as resource:
        print(f"使用资源: {resource}")
        # 模拟可能出错的操作
        if random.random() < 0.3:
            raise Exception("随机错误")
        print("操作成功")
except Exception as e:
    print(f"操作失败: {e}")
```

---

## 9. 实际应用

### 9.1 文件处理应用
```python
import os
import shutil

class FileProcessor:
    """文件处理器"""
    
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.processed_files = []
        self.failed_files = []
    
    def process_file(self, filename):
        """处理单个文件"""
        file_path = os.path.join(self.base_dir, filename)
        
        try:
            # 检查文件是否存在
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"文件不存在: {filename}")
            
            # 检查文件权限
            if not os.access(file_path, os.R_OK):
                raise PermissionError(f"没有读取权限: {filename}")
            
            # 处理文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 模拟处理
            processed_content = content.upper()
            
            # 保存处理后的文件
            output_path = os.path.join(self.base_dir, f"processed_{filename}")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            self.processed_files.append(filename)
            print(f"成功处理文件: {filename}")
            
        except FileNotFoundError as e:
            print(f"文件错误: {e}")
            self.failed_files.append((filename, str(e)))
        except PermissionError as e:
            print(f"权限错误: {e}")
            self.failed_files.append((filename, str(e)))
        except UnicodeDecodeError as e:
            print(f"编码错误: {e}")
            self.failed_files.append((filename, str(e)))
        except Exception as e:
            print(f"处理文件 {filename} 时发生未知错误: {e}")
            self.failed_files.append((filename, str(e)))
    
    def process_directory(self):
        """处理目录中的所有文件"""
        try:
            files = os.listdir(self.base_dir)
            txt_files = [f for f in files if f.endswith('.txt')]
            
            print(f"找到 {len(txt_files)} 个文本文件")
            
            for filename in txt_files:
                self.process_file(filename)
            
            # 输出处理结果
            print(f"\n处理完成:")
            print(f"成功处理: {len(self.processed_files)} 个文件")
            print(f"处理失败: {len(self.failed_files)} 个文件")
            
            if self.failed_files:
                print("\n失败的文件:")
                for filename, error in self.failed_files:
                    print(f"  {filename}: {error}")
                    
        except Exception as e:
            print(f"处理目录时发生错误: {e}")

# 使用文件处理器
# processor = FileProcessor("test_files")
# processor.process_directory()
```

### 9.2 网络请求应用
```python
import requests
import time
from typing import Optional, Dict, Any

class APIClient:
    """API客户端"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def make_request(self, endpoint: str, method: str = "GET", 
                    data: Optional[Dict[str, Any]] = None,
                    max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """发送API请求"""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(max_retries):
            try:
                print(f"发送请求到 {url} (尝试 {attempt + 1}/{max_retries})")
                
                if method.upper() == "GET":
                    response = self.session.get(url, timeout=self.timeout)
                elif method.upper() == "POST":
                    response = self.session.post(url, json=data, timeout=self.timeout)
                else:
                    raise ValueError(f"不支持的HTTP方法: {method}")
                
                # 检查响应状态
                response.raise_for_status()
                
                # 解析JSON响应
                result = response.json()
                print(f"请求成功: {result}")
                return result
                
            except requests.exceptions.Timeout:
                print(f"请求超时 (尝试 {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # 指数退避
                else:
                    print("所有重试都失败了")
                    
            except requests.excepti