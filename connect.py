#!/usr/bin/python3.8


import pymysql
import charts

# 資料庫設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "test",
    "password": "test",
    "db": "mid_courseselectsystem",
    "charset": "utf8"
}
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
      #資料表相關操作
except Exception as ex:
    print(ex)


#import mysql.connector

#cnx = mysql.connector.connect(user='test', 
#                              password='test',
#                              host='127.0.0.1',
#                              database='mid_courseselectsystem')

#cnx.close()




