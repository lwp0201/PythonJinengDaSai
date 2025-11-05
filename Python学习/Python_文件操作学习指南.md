# Python 文件操作学习指南

## 目录
1. [文件操作基础](#1-文件操作基础)
2. [文件读写模式](#2-文件读写模式)
3. [文本文件操作](#3-文本文件操作)
4. [二进制文件操作](#4-二进制文件操作)
5. [文件路径操作](#5-文件路径操作)
6. [目录操作](#6-目录操作)
7. [文件信息获取](#7-文件信息获取)
8. [异常处理](#8-异常处理)
9. [高级文件操作](#9-高级文件操作)
10. [最佳实践](#10-最佳实践)

---

## 1. 文件操作基础

### 1.1 什么是文件操作？
文件操作是指程序与文件系统进行交互，包括读取、写入、创建、删除文件等操作。

### 1.2 基本文件操作流程
```python
# 1. 打开文件
file = open('example.txt', 'r')

# 2. 操作文件
content = file.read()

# 3. 关闭文件
file.close()
```

### 1.3 使用with语句（推荐）
```python
# 使用with语句自动管理文件
with open('example.txt', 'r') as file:
    content = file.read()
    # 文件会自动关闭
```

---

## 2. 文件读写模式

### 2.1 文本模式详解

#### 2.1.1 只读模式 ('r')
```python
# 'r' - 只读模式（默认）
# 特点：文件必须存在，只能读取，不能写入
# 文件指针：从文件开头开始

# 基本用法
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# 逐行读取
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip()去除换行符

# 读取所有行
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(f"总行数: {len(lines)}")

# 读取指定字符数
with open('file.txt', 'r') as f:
    first_100_chars = f.read(100)
    print(f"前100个字符: {first_100_chars}")

# 错误处理
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在！")
```

#### 2.1.2 写入模式 ('w')
```python
# 'w' - 写入模式（覆盖）
# 特点：如果文件存在则清空内容，如果不存在则创建
# 文件指针：从文件开头开始
# 注意：使用此模式会完全覆盖原文件内容！

# 基本写入
with open('file.txt', 'w') as f:
    f.write('Hello World')
    f.write('\nThis is a new line')

# 写入多行
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)

# 使用print函数写入
with open('file.txt', 'w') as f:
    print('使用print写入', file=f)
    print('可以自动添加换行符', file=f)

# 格式化写入
data = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
with open('data.txt', 'w') as f:
    for key, value in data.items():
        f.write(f"{key}: {value}\n")

# 批量写入（性能更好）
large_data = [f"Line {i}\n" for i in range(1000)]
with open('large_file.txt', 'w') as f:
    f.writelines(large_data)
```

#### 2.1.3 追加模式 ('a')
```python
# 'a' - 追加模式
# 特点：如果文件存在则在末尾追加，如果不存在则创建
# 文件指针：从文件末尾开始
# 注意：无法读取文件内容，只能写入

# 基本追加
with open('log.txt', 'a') as f:
    f.write('2023-12-25 10:00:00 - 系统启动\n')
    f.write('2023-12-25 10:01:00 - 用户登录\n')

# 追加结构化数据
import datetime

def log_message(message):
    """记录日志消息"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('app.log', 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

# 使用日志函数
log_message("应用程序启动")
log_message("数据库连接成功")
log_message("用户操作完成")

# 追加CSV数据
def append_csv_data(filename, data):
    """追加CSV数据"""
    with open(filename, 'a') as f:
        f.write(','.join(map(str, data)) + '\n')

# 使用示例
append_csv_data('sales.csv', ['2023-12-25', '产品A', 100, 29.99])
append_csv_data('sales.csv', ['2023-12-25', '产品B', 50, 19.99])
```

#### 2.1.4 创建模式 ('x')
```python
# 'x' - 创建模式（独占创建）
# 特点：如果文件已存在则报错，如果不存在则创建
# 文件指针：从文件开头开始
# 用途：防止意外覆盖重要文件

# 基本用法
try:
    with open('new_file.txt', 'x') as f:
        f.write('这是新创建的文件')
    print("文件创建成功")
except FileExistsError:
    print("文件已存在，无法创建")

# 创建配置文件
config_data = {
    'database_host': 'localhost',
    'database_port': 5432,
    'debug_mode': True,
    'max_connections': 100
}

try:
    with open('config.txt', 'x') as f:
        for key, value in config_data.items():
            f.write(f"{key} = {value}\n")
    print("配置文件创建成功")
except FileExistsError:
    print("配置文件已存在")

# 创建带时间戳的文件
import datetime

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'backup_{timestamp}.txt'

try:
    with open(filename, 'x') as f:
        f.write(f'备份文件创建时间: {datetime.datetime.now()}\n')
        f.write('备份内容...\n')
    print(f"备份文件 {filename} 创建成功")
except FileExistsError:
    print("备份文件已存在")
```

#### 2.1.5 文本模式最佳实践
```python
# 1. 总是指定编码
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. 处理不同编码的文件
def read_file_with_encoding(filename):
    """尝试不同编码读取文件"""
    encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                content = f.read()
            print(f"成功使用 {encoding} 编码读取文件")
            return content
        except UnicodeDecodeError:
            continue
    
    raise ValueError("无法使用任何编码读取文件")

# 3. 安全写入（先写入临时文件）
import tempfile
import os

def safe_write(filename, content):
    """安全写入文件"""
    # 创建临时文件
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.tmp') as temp_file:
        temp_file.write(content)
        temp_filename = temp_file.name
    
    try:
        # 原子性操作：重命名临时文件
        os.replace(temp_filename, filename)
        print(f"文件 {filename} 写入成功")
    except Exception as e:
        # 清理临时文件
        os.unlink(temp_filename)
        raise e

# 使用安全写入
safe_write('important.txt', '重要数据')

# 4. 文件操作上下文管理器
class FileManager:
    """文件管理器"""
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"文件操作出错: {exc_type.__name__}: {exc_val}")

# 使用自定义文件管理器
with FileManager('test.txt', 'w') as f:
    f.write('使用自定义文件管理器')
```

#### 2.1.6 文本模式常见问题
```python
# 问题1：文件路径问题
import os

# 检查文件是否存在
filename = 'data.txt'
if os.path.exists(filename):
    print(f"文件 {filename} 存在")
else:
    print(f"文件 {filename} 不存在")

# 问题2：权限问题
try:
    with open('/root/protected.txt', 'r') as f:
        content = f.read()
except PermissionError:
    print("没有权限访问文件")

# 问题3：文件被占用
try:
    with open('locked_file.txt', 'w') as f:
        f.write('test')
except IOError as e:
    print(f"文件被占用: {e}")

# 问题4：磁盘空间不足
try:
    with open('large_file.txt', 'w') as f:
        for i in range(1000000):
            f.write(f"Line {i}\n")
except OSError as e:
    print(f"磁盘空间不足: {e}")

# 问题5：文件名包含特殊字符
import re

def sanitize_filename(filename):
    """清理文件名"""
    # 移除或替换非法字符
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename

safe_filename = sanitize_filename('file<name>.txt')
print(f"安全文件名: {safe_filename}")
```

### 2.2 读写模式
```python
# 'r+' - 读写模式
with open('file.txt', 'r+') as f:
    content = f.read()
    f.write('Additional content')

# 'w+' - 写读模式
with open('file.txt', 'w+') as f:
    f.write('New content')
    f.seek(0)  # 回到文件开头
    content = f.read()

# 'a+' - 追加读模式
with open('file.txt', 'a+') as f:
    f.write('Appended content')
    f.seek(0)
    content = f.read()
```

### 2.3 二进制模式
```python
# 'rb' - 二进制只读
with open('image.jpg', 'rb') as f:
    data = f.read()

# 'wb' - 二进制写入
with open('copy.jpg', 'wb') as f:
    f.write(data)

# 'ab' - 二进制追加
with open('log.bin', 'ab') as f:
    f.write(b'\x00\x01\x02')
```

---

## 3. 文本文件操作

### 3.1 读取文件
```python
# 读取整个文件
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 逐行读取
with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # strip()去除换行符

# 读取所有行到列表
with open('example.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# 读取指定字节数
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read(100)  # 读取前100个字符
    print(content)
```

### 3.2 写入文件
```python
# 写入字符串
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World\n')
    f.write('Python is awesome!')

# 写入多行
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 使用print函数写入
with open('output.txt', 'w', encoding='utf-8') as f:
    print('Hello World', file=f)
    print('Python is awesome!', file=f)
```

### 3.3 文件定位
```python
with open('example.txt', 'r+', encoding='utf-8') as f:
    # 获取当前位置
    position = f.tell()
    print(f"当前位置: {position}")
    
    # 移动到文件开头
    f.seek(0)
    
    # 移动到文件末尾
    f.seek(0, 2)  # 2表示从文件末尾开始
    
    # 移动到指定位置
    f.seek(10)  # 移动到第10个字符
    
    # 相对移动
    f.seek(5, 1)  # 从当前位置向后移动5个字符
    f.seek(-3, 1)  # 从当前位置向前移动3个字符
```

### 3.4 编码处理
```python
# 指定编码
with open('chinese.txt', 'w', encoding='utf-8') as f:
    f.write('你好，世界！')

# 读取不同编码的文件
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    # 如果UTF-8失败，尝试其他编码
    with open('file.txt', 'r', encoding='gbk') as f:
        content = f.read()

# 自动检测编码
import chardet

with open('unknown.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    
    with open('unknown.txt', 'r', encoding=encoding) as f:
        content = f.read()
```

---

## 4. 二进制文件操作

### 4.1 读取二进制文件
```python
# 读取图片文件
with open('image.jpg', 'rb') as f:
    image_data = f.read()
    print(f"图片大小: {len(image_data)} 字节")

# 读取二进制文件的前几个字节
with open('binary_file.bin', 'rb') as f:
    header = f.read(4)  # 读取前4个字节
    print(f"文件头: {header}")
```

### 4.2 写入二进制文件
```python
# 创建二进制文件
data = b'\x48\x65\x6c\x6c\x6f'  # "Hello"的ASCII码
with open('binary_output.bin', 'wb') as f:
    f.write(data)

# 复制二进制文件
with open('source.jpg', 'rb') as source:
    with open('copy.jpg', 'wb') as target:
        while True:
            chunk = source.read(1024)  # 每次读取1KB
            if not chunk:
                break
            target.write(chunk)
```

### 4.3 结构化二进制数据
```python
import struct

# 写入结构化数据
with open('data.bin', 'wb') as f:
    # 写入整数
    f.write(struct.pack('i', 12345))  # 4字节整数
    # 写入浮点数
    f.write(struct.pack('f', 3.14159))  # 4字节浮点数
    # 写入字符串
    f.write(b'Hello World')

# 读取结构化数据
with open('data.bin', 'rb') as f:
    # 读取整数
    integer = struct.unpack('i', f.read(4))[0]
    print(f"整数: {integer}")
    
    # 读取浮点数
    float_num = struct.unpack('f', f.read(4))[0]
    print(f"浮点数: {float_num}")
    
    # 读取字符串
    string = f.read(11).decode('utf-8')
    print(f"字符串: {string}")
```

---

## 5. 文件路径操作

### 5.1 os.path模块
```python
import os

# 路径拼接
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)  # 输出: folder/subfolder/file.txt (Windows: folder\subfolder\file.txt)

# 获取文件名
filename = os.path.basename('/path/to/file.txt')
print(filename)  # 输出: file.txt

# 获取目录名
dirname = os.path.dirname('/path/to/file.txt')
print(dirname)  # 输出: /path/to

# 分割路径
dir_name, file_name = os.path.split('/path/to/file.txt')
print(f"目录: {dir_name}, 文件: {file_name}")

# 分离文件名和扩展名
name, ext = os.path.splitext('file.txt')
print(f"文件名: {name}, 扩展名: {ext}")

# 获取绝对路径
abs_path = os.path.abspath('file.txt')
print(abs_path)

# 检查路径是否存在
exists = os.path.exists('file.txt')
print(f"文件存在: {exists}")
```

### 5.2 pathlib模块（推荐）
```python
from pathlib import Path

# 创建路径对象
path = Path('folder') / 'subfolder' / 'file.txt'
print(path)  # 输出: folder/subfolder/file.txt

# 获取文件名
filename = path.name
print(filename)  # 输出: file.txt

# 获取父目录
parent = path.parent
print(parent)  # 输出: folder/subfolder

# 获取扩展名
suffix = path.suffix
print(suffix)  # 输出: .txt

# 获取不带扩展名的文件名
stem = path.stem
print(stem)  # 输出: file

# 检查路径是否存在
exists = path.exists()
print(f"路径存在: {exists}")

# 获取绝对路径
abs_path = path.resolve()
print(abs_path)
```

### 5.3 路径操作示例
```python
from pathlib import Path

# 创建目录结构
base_dir = Path('project')
base_dir.mkdir(exist_ok=True)

# 创建子目录
sub_dir = base_dir / 'src' / 'utils'
sub_dir.mkdir(parents=True, exist_ok=True)

# 创建文件
config_file = base_dir / 'config.json'
config_file.write_text('{"name": "My Project"}')

# 遍历目录
for item in base_dir.rglob('*'):  # 递归遍历所有文件
    if item.is_file():
        print(f"文件: {item}")
    elif item.is_dir():
        print(f"目录: {item}")
```

---

## 6. 目录操作

### 6.1 创建和删除目录
```python
import os
import shutil

# 创建单个目录
os.mkdir('new_folder')

# 创建多级目录
os.makedirs('level1/level2/level3', exist_ok=True)

# 删除空目录
os.rmdir('empty_folder')

# 删除目录及其内容
shutil.rmtree('folder_to_delete')

# 使用pathlib
from pathlib import Path

# 创建目录
Path('new_folder').mkdir(exist_ok=True)
Path('level1/level2/level3').mkdir(parents=True, exist_ok=True)

# 删除目录
Path('empty_folder').rmdir()
```

### 6.2 遍历目录
```python
import os
from pathlib import Path

# 使用os.listdir()
for item in os.listdir('.'):
    print(item)

# 使用os.walk()递归遍历
for root, dirs, files in os.walk('.'):
    print(f"目录: {root}")
    for file in files:
        print(f"  文件: {file}")

# 使用pathlib
path = Path('.')
for item in path.iterdir():
    if item.is_file():
        print(f"文件: {item}")
    elif item.is_dir():
        print(f"目录: {item}")

# 递归遍历
for item in path.rglob('*.py'):  # 查找所有.py文件
    print(f"Python文件: {item}")
```

### 6.3 目录操作示例
```python
import os
import shutil
from pathlib import Path

def organize_files(source_dir, target_dir):
    """按文件类型整理文件"""
    source = Path(source_dir)
    target = Path(target_dir)
    
    # 创建目标目录
    target.mkdir(exist_ok=True)
    
    # 按扩展名分类
    file_types = {}
    for file_path in source.rglob('*'):
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(file_path)
    
    # 创建分类目录并移动文件
    for ext, files in file_types.items():
        if ext:  # 有扩展名的文件
            type_dir = target / f"{ext[1:]}_files"  # 去掉点号
            type_dir.mkdir(exist_ok=True)
            
            for file_path in files:
                new_path = type_dir / file_path.name
                shutil.move(str(file_path), str(new_path))
                print(f"移动: {file_path} -> {new_path}")

# 使用示例
organize_files('source_folder', 'organized_folder')
```

---

## 7. 文件信息获取

### 7.1 基本文件信息
```python
import os
from pathlib import Path
import time

# 使用os.stat()
file_path = 'example.txt'
stat_info = os.stat(file_path)

print(f"文件大小: {stat_info.st_size} 字节")
print(f"最后修改时间: {time.ctime(stat_info.st_mtime)}")
print(f"最后访问时间: {time.ctime(stat_info.st_atime)}")
print(f"创建时间: {time.ctime(stat_info.st_ctime)}")

# 使用pathlib
path = Path('example.txt')
if path.exists():
    print(f"文件大小: {path.stat().st_size} 字节")
    print(f"是否为文件: {path.is_file()}")
    print(f"是否为目录: {path.is_dir()}")
    print(f"是否为符号链接: {path.is_symlink()}")
```

### 7.2 文件权限
```python
import os
import stat

file_path = 'example.txt'
file_stat = os.stat(file_path)

# 检查权限
readable = os.access(file_path, os.R_OK)
writable = os.access(file_path, os.W_OK)
executable = os.access(file_path, os.X_OK)

print(f"可读: {readable}")
print(f"可写: {writable}")
print(f"可执行: {executable}")

# 修改权限
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)  # 用户读写权限
```

### 7.3 文件比较
```python
import filecmp
import hashlib

# 比较文件内容
same = filecmp.cmp('file1.txt', 'file2.txt')
print(f"文件内容相同: {same}")

# 计算文件哈希值
def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

hash1 = get_file_hash('file1.txt')
hash2 = get_file_hash('file2.txt')
print(f"文件1哈希: {hash1}")
print(f"文件2哈希: {hash2}")
print(f"哈希相同: {hash1 == hash2}")
```

---

## 8. 异常处理

### 8.1 文件操作异常
```python
# 文件不存在异常
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")

# 权限异常
try:
    with open('/root/protected.txt', 'r') as f:
        content = f.read()
except PermissionError:
    print("没有权限访问文件")

# 编码异常
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    print("文件编码错误，尝试其他编码")
    with open('file.txt', 'r', encoding='gbk') as f:
        content = f.read()
```

### 8.2 综合异常处理
```python
def safe_file_operation(file_path, operation='read'):
    """安全的文件操作"""
    try:
        if operation == 'read':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        elif operation == 'write':
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("Hello World")
                return True
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return None
    except PermissionError:
        print(f"没有权限访问文件 {file_path}")
        return None
    except UnicodeDecodeError:
        print(f"文件 {file_path} 编码错误")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 使用示例
result = safe_file_operation('example.txt', 'read')
if result:
    print("文件读取成功")
```

### 8.3 上下文管理器
```python
class FileManager:
    """自定义文件管理器"""
    
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            return self.file
        except FileNotFoundError:
            print(f"文件 {self.filename} 不存在")
            return None
        except Exception as e:
            print(f"打开文件时出错: {e}")
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"文件操作出错: {exc_type.__name__}: {exc_val}")
        return False  # 不抑制异常

# 使用自定义上下文管理器
with FileManager('example.txt', 'r') as f:
    if f:
        content = f.read()
        print(content)
```

---

## 9. 高级文件操作

### 9.1 临时文件
```python
import tempfile
import os

# 创建临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write('临时文件内容')
    temp_filename = f.name

print(f"临时文件: {temp_filename}")

# 读取临时文件
with open(temp_filename, 'r') as f:
    content = f.read()
    print(f"内容: {content}")

# 清理临时文件
os.unlink(temp_filename)

# 使用临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"临时目录: {temp_dir}")
    # 在临时目录中创建文件
    temp_file = os.path.join(temp_dir, 'temp.txt')
    with open(temp_file, 'w') as f:
        f.write('临时目录中的文件')
    # 临时目录会自动删除
```

### 9.2 文件压缩
```python
import zipfile
import tarfile
import gzip

# ZIP文件操作
# 创建ZIP文件
with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('file1.txt')
    zf.write('file2.txt')

# 读取ZIP文件
with zipfile.ZipFile('archive.zip', 'r') as zf:
    print("ZIP文件内容:")
    for info in zf.infolist():
        print(f"  {info.filename} ({info.file_size} 字节)")

# 解压ZIP文件
with zipfile.ZipFile('archive.zip', 'r') as zf:
    zf.extractall('extracted_folder')

# TAR文件操作
# 创建TAR文件
with tarfile.open('archive.tar', 'w') as tf:
    tf.add('file1.txt')
    tf.add('file2.txt')

# 读取TAR文件
with tarfile.open('archive.tar', 'r') as tf:
    print("TAR文件内容:")
    for member in tf.getmembers():
        print(f"  {member.name} ({member.size} 字节)")

# GZIP压缩
with open('file.txt', 'rb') as f_in:
    with gzip.open('file.txt.gz', 'wb') as f_out:
        f_out.write(f_in.read())
```

### 9.3 文件监控
```python
import time
from pathlib import Path

def monitor_file_changes(file_path, interval=1):
    """监控文件变化"""
    path = Path(file_path)
    if not path.exists():
        print(f"文件 {file_path} 不存在")
        return
    
    last_modified = path.stat().st_mtime
    print(f"开始监控文件: {file_path}")
    
    try:
        while True:
            current_modified = path.stat().st_mtime
            if current_modified != last_modified:
                print(f"文件已修改: {time.ctime(current_modified)}")
                last_modified = current_modified
            time.sleep(interval)
    except KeyboardInterrupt:
        print("停止监控")

# 使用示例
# monitor_file_changes('example.txt')
```

### 9.4 大文件处理
```python
def process_large_file(file_path, chunk_size=1024):
    """处理大文件"""
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # 处理数据块
            yield chunk

def copy_large_file(source, destination, buffer_size=8192):
    """复制大文件"""
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        while True:
            chunk = src.read(buffer_size)
            if not chunk:
                break
            dst.write(chunk)

# 使用示例
for chunk in process_large_file('large_file.bin'):
    # 处理每个数据块
    print(f"处理了 {len(chunk)} 字节")
```

---

## 10. 最佳实践

### 10.1 文件操作最佳实践
```python
# 1. 总是使用with语句
# 好的做法
with open('file.txt', 'r') as f:
    content = f.read()

# 不好的做法
f = open('file.txt', 'r')
content = f.read()
f.close()  # 可能忘记关闭

# 2. 指定编码
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. 处理异常
def read_file_safely(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return None
    except UnicodeDecodeError:
        print(f"文件 {file_path} 编码错误")
        return None
```

### 10.2 路径操作最佳实践
```python
from pathlib import Path

# 使用pathlib而不是字符串拼接
# 好的做法
file_path = Path('data') / 'config' / 'settings.json'

# 不好的做法
file_path = 'data' + '/' + 'config' + '/' + 'settings.json'

# 检查路径存在性
if file_path.exists():
    with open(file_path, 'r') as f:
        content = f.read()
```

### 10.3 性能优化
```python
# 1. 使用生成器处理大文件
def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# 2. 批量操作
def batch_process_files(file_paths, batch_size=100):
    for i in range(0, len(file_paths), batch_size):
        batch = file_paths[i:i + batch_size]
        for file_path in batch:
            # 处理文件
            pass

# 3. 使用内存映射
import mmap

def read_file_with_mmap(file_path):
    with open(file_path, 'r+b') as f:
        with mmap.mmap(f.fileno(), 0) as mm:
            return mm.read()
```

### 10.4 安全考虑
```python
import os
from pathlib import Path

def safe_file_operation(file_path):
    """安全的文件操作"""
    # 规范化路径
    path = Path(file_path).resolve()
    
    # 检查路径是否在允许的目录内
    allowed_dir = Path('/safe/directory').resolve()
    if not str(path).startswith(str(allowed_dir)):
        raise ValueError("文件路径不在允许的目录内")
    
    # 检查文件大小
    if path.exists() and path.stat().st_size > 100 * 1024 * 1024:  # 100MB
        raise ValueError("文件过大")
    
    return path

# 使用示例
try:
    safe_path = safe_file_operation('data/config.txt')
    with open(safe_path, 'r') as f:
        content = f.read()
except ValueError as e:
    print(f"安全错误: {e}")
```

### 10.5 配置文件处理
```python
import json
import yaml
import configparser
from pathlib import Path

# JSON配置文件
def load_json_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# YAML配置文件
def load_yaml_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# INI配置文件
def load_ini_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    return config

# 使用示例
config = load_json_config('config.json')
print(f"数据库主机: {config['database']['host']}")
```

---

## 总结

Python文件操作是编程中的重要技能，掌握好文件操作对于数据处理、配置管理、日志记录等任务至关重要。记住以下要点：

1. **总是使用with语句**：确保文件正确关闭
2. **指定编码**：避免编码问题
3. **处理异常**：提高程序健壮性
4. **使用pathlib**：更现代的路径操作
5. **考虑性能**：大文件使用流式处理
6. **注意安全**：验证文件路径和大小
7. **遵循最佳实践**：编写可维护的代码

通过不断练习和实践，您将能够熟练运用Python文件操作，处理各种文件相关的任务！
