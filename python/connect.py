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

        stdid = "D1060001" #前端傳的值

    # 已選課表

        # 查詢語句，參數化防止sql注入 
        sql_selected = 'SELECT * FROM db_course where db_course.`"選課代號"` IN (SELECT `"已選課程代碼"` FROM db_courseselected where `"學生學號"` = %s GROUP by `"已選課程代碼"`) GROUP by `"選課代號"`'
        params_selected = (stdid)

        cursor.execute(sql_selected,params_selected)
        selected = cursor.fetchall() #type(result) = tuple
        print(selected)
        
        '''以下是半成品
        sql_selectedID_from_stdid = 'SELECT `"已選課程代碼"` FROM `db_courseselected` WHERE `"學生學號"`= %s'
        params = (stdid)

        cursor.execute(sql_selectedID_from_stdid,params)
        selected_ID = cursor.fetchall() #type(result) = tuple
        for i in selected_ID:
            sql_course_from_courseID ='SELECT * from `db_course` where `"課程" sqli[0]
        print()
        '''

    # 可選課表
        sql_selectable = 'SELECT * from db_course where `db_course`.`"選課代號"` NOT IN (SELECT `"選課代號"` from db_course WHERE db_course.`"開課科系"` IN (SELECT SUBSTR(`"學生班級"`, 1,2) as class FROM db_students where `"學生學號"` = %s GROUP by class) and db_course.`"開課年級"` IN (SELECT SUBSTR(`"學生班級"`, 3,1) as grade FROM db_students where `"學生學號"` = %s GROUP by grade) and db_course.`"必選修"` = "M" GROUP BY db_course.`"選課代號"`) GROUP BY db_course.`"選課代號"`;'
        params_selectable = (stdid,stdid)
        cursor.execute(sql_selectable,params_selectable)
        selectable = cursor.fetchall() #type(result) = tuple
        print(selectable)
        
         
        
except Exception as ex:
    print(ex)






