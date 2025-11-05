import sqlite3

conn = sqlite3.connect('AP.db')  # 连接到 ncp.db 数据库
cur = conn.cursor()   # 创建游标对象

# 编写 SQL 语句来创建 系统用户表（users）
query = '''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
);
'''
cur.execute(query)  # 执行 SQL 命令

conn.commit()   # 提交更改
conn.close()    # 关闭数据库的连接