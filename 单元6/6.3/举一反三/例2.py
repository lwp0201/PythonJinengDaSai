import sqlite3

conn = sqlite3.connect(r'C:\Users\lwp57\Desktop\Pytho技能大赛\源代码\单元6\6.3\举一反三\AP.db')  # 连接到 AP.db 数据库
cur = conn.cursor()   # 创建游标对象

kind='水产'
query = 'SELECT sum(金额（元）) FROM order_detail where 农产品类别=?'   # 编写查询语句
cur.execute(query,(kind,))  # 执行查询语句，准备结果集

totalsales = cur.fetchone()  # 提取所有行，将结果集中所有行存储在 rows 变量

print(totalsales)

conn.close()    # 关闭数据库的连接
