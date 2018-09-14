#-*- coding: utf-8 -*-
import csv
import os
import pymysql
import pandas as pd

# 一个根据pandas自动识别type来设定table的type
def make_table_sql(df):
    columns = df.columns.tolist()
    types = df.ftypes
    # 添加id 制动递增主键模式
    make_table = []
    for item in columns:
        if 'int' in types[item]:
            char = item + ' INT'
        elif 'float' in types[item]:
            char = item + ' FLOAT'
        elif 'object' in types[item]:
            char = item + ' longtext'           
        elif 'datetime' in types[item]:
            char = item + ' DATETIME'            
        make_table.append(char)
    return ','.join(make_table)


# csv 格式输入 mysql 中
def csv2mysql(db_name, table_name, df):
    # 创建database
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
    # 选择连接database
    conn.select_db(db_name)
    print("hello")
    # 创建table
    cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
    cursor.execute('CREATE TABLE {}({})'.format(table_name,make_table_sql(df)))
    # 提取数据转list 这里有与pandas时间模式无法写入因此换成str 此时mysql上格式已经设置完成
    # df['日期'] = df['日期'].astype('str')
    values = df.values.tolist()
    # 根据columns个数
    s = ','.join(['%s' for _ in range(len(df.columns))])
    # executemany批量操作 插入数据 批量操作比逐个操作速度快很多
    cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name,s), values)

# 参数设置 DictCursor使输出为字典模式 连接到本地用户root 密码为kellydc
config = dict(host='localhost', user='root', password='kellydc',
             cursorclass=pymysql.cursors.DictCursor
             )
# 建立连接
conn = pymysql.Connect(**config)
# 自动确认commit True
conn.autocommit(1)
# 设置光标
cursor = conn.cursor()

df = pd.read_csv('/Users/daven/Github/MedDataPro/sampleData/clear/clear_set.csv', encoding='utf-8', low_memory=False)
df = df.astype(object).where(pd.notnull(df), None)
# print(df.head())

csv2mysql("MedData","RM_Report", df)

cursor.execute('SELECT * FROM RM_Report LIMIT 5')

cursor.scroll(4)
cursor.fetchall()

