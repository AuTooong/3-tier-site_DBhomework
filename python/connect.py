#!/usr/bin/python3.8

import pymysql

db_settings = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "test",
    "password": "test",
    "db": "mid_courseselectsystem",
    "charset": "utf8"
}
try:
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:

        # 已選課表
        stdid = "D1060001" #前端傳的值

        # 查詢語句，參數化防止sql注入
        sql = 'SELECT * FROM `db_courseselected` WHERE `"學生學號"` LIKE "%s"'
        params = (stdid)

        cursor.execute(sql, params)
        result = cursor.fetchall() #type(result) = tuple
        print(result)

        
except Exception as ex:
    print(ex)






