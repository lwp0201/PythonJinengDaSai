import sqlite3

conn = sqlite3.connect(r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元6\6.3\举一反三\AP.db')  # 连接到 AP.db 数据库
cur = conn.cursor()   # 创建游标对象

query = 'SELECT * FROM product_info'   # 编写查询语句
cur.execute(query)  # 执行查询语句，准备结果集

rows = cur.fetchall()  # 提取所有行，将结果集中所有行存储在 rows 变量
for row in rows:       # 遍历 rows，打印每一行
    print(row)

conn.close()    # 关闭数据库的连接


