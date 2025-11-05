import sqlite3

conn = sqlite3.connect(r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元6\6.3\体验预备\AP.db')  # 连接到 AP.db 数据库
cur = conn.cursor()   # 创建游标对象

# 编写 SQL 语句来向 农产品信息表（product_info） 中插入新的记录
query = '''
INSERT INTO product_info (农产品代码, 农产品名称, 农产品类别, 单价)
VALUES (?, ?, ?, ?)
'''
products = [                    # 定义一个元组，保存新记录的数据
    ('P012', '牛肉', '畜肉', 65.0),
    ('P013', '猪肉', '畜肉', 45),
    ('P014', '鸡肉', '禽类', 30.0)
]

cur.executemany(query, products)  # 执行 SQL 语句

# 假设要更新农产品信息表中指定农产品编号的价格
product_code = 'P003'  # 原始数据 ('P003', '猪肉', '畜肉', 45.0)
new_price = 40.0  # 新的价格

query = 'UPDATE product_info SET 单价 = ? WHERE 农产品代码 = ?'   # 编写查询语句
cur.execute(query, (new_price, product_code))  # 执行查询语句，准备结果集

conn.commit()   # 提交更改
conn.close()    # 关闭数据库的连接