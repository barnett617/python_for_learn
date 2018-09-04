#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
import pymysql

db_ip = "45.76.52.16"
db_username = "root"
db_password = "toor"
db_name = "python_for_learn"

db_list = []

# f = open('../db.db','r')
# result = list()
# for line in open('../db.db'):
#     line = f.readline()
#     db_list.insert(line)
#     print line
#     result.append(line)
# print result
# f.close()          
 
# 打开数据库连接
db = pymysql.connect(db_ip, db_username, db_password, db_name)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# sql = """INSERT INTO USER(id,username, info)
#          VALUES ('3', 'jingtao', 'houhouhou')"""

sql = "SELECT * FROM USER"

# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#   #  print(results)
#   #  for row in results:
#   #     username = row[1]
#   #     info = row[2]
#   #      # 打印结果
#   #     print ("username=%s,info=%d" % \
#   #            (username, info ))
#    # 提交到数据库执行
#    # db.commit()
# except:
#    # 如果发生错误则回滚
#   #  db.rollback()
#   print ("Error: unable to fetch data")

# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")

cursor.execute("SELECT 1 from USER")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()