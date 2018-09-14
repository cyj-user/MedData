import pymysql

# 打开数据库连接
db = pymysql.connect("120.77.253.60", "root", "kellydc", "MedData")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM RM_Report LIMIT 10;"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
   print ("Error: unable to fetch data")