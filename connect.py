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
except Exception as ex:
    print(ex)






