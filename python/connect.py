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
        
        sql_std = 'SELECT * FROM db_students WHERE `"學生學號"` = %s'
        params_std = (stdid)
        cursor.execute(sql_std,params_std)
        stduent = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            stduent.append(line)
        print(stduent)
        
    # 已選課表
        # 查詢語句，參數化防止sql注入 
        sql_selected = 'SELECT * FROM db_course LEFT JOIN db_coursetime ON db_course.`"選課代號"`= db_coursetime.`"選課代號"` where db_course.`"選課代號"` IN (SELECT `"已選課程代碼"` FROM db_courseselected where `"學生學號"` = %s GROUP by `"已選課程代碼"`) GROUP by db_course.`"選課代號"`'
        params_selected = (stdid)
        cursor.execute(sql_selected,params_selected)

        selected = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            selected.append(line)
        print(selected)
        
    # 可選課表
        sql_selectable = 'SELECT * from db_course LEFT JOIN db_coursetime ON `db_course`.`"選課代號"`= `db_coursetime`.`"選課代號"` where `db_course`.`"選課代號"` NOT IN (SELECT `"選課代號"` from db_course WHERE db_course.`"開課科系"` IN (SELECT SUBSTR(`"學生班級"`, 1,2) as class FROM db_students where `"學生學號"` = %s GROUP by class) and db_course.`"開課年級"` IN (SELECT SUBSTR(`"學生班級"`, 3,1) as grade FROM db_students where `"學生學號"` = %s GROUP by grade) and db_course.`"必選修"` = "M" GROUP BY db_course.`"選課代號"`) GROUP BY db_course.`"選課代號"`;'
        params_selectable = (stdid,stdid)
        cursor.execute(sql_selectable,params_selectable)

        selectable = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            selectable.append(line)
        print(selectable)

    # 判斷
        flag = 0 # 0:可選 1:不可選 2:已選

        for i in selectable:
            # 判斷是否已選
            flag = 0
            for j in selected:
                if i[0] == j[0]:
                    flag = 2
                    break
            # 判斷是否已選滿 
            if i[9] >= i[8] and flag != 2:
                flag = 1


            # 判斷是否衝堂
            for j in selected:
                # i 要選的課程 j 已選的課程
                # 13:星期 14:開始時間 15:結束時間
                if ((i[13] == j[13]) and ((int(i[14]) >= int(j[14]) and int(i[14]) <= int(j[15])) or (int(i[15]) >= int(j[14]) and int(i[15]) <= int(j[15])) or (int(i[14]) <= int(j[14]) and int(i[15]) >= int(j[15])))) and flag != 2:
                    print(i[13],j[13],i[14],i[15],j[14],j[15])
                    flag = 3
                    break

            # 判斷是否超過學分
            if int(i[5]) + int(stduent[0][3]) > 30 and flag != 2:
                flag = 4
         
            print(flag)
        #    i.append(flag) 

       # print(selectable)

        for i in selectable:
            i.append(flag)

        #print(selectable)

    # 加選
        courseid = "3011" #前端傳的值
        
        sql_score = 'SELECT `"學分數"` FROM `db_course` WHERE `"選課代號"` = %s'
        params_score = (courseid)
        cursor.execute(sql_score,params_score)
        score = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            score.append(line)

        sql_add = 'INSERT INTO db_courseselected (`"學生姓名 "`, `"學生學號"`, `"學生班級"`, `"已選課程代碼"`, `"學分數"`) VALUES (%s,%s,%s,%s,%s)'
        params_add = (stduent[0][0],stduent[0][1],stduent[0][2],courseid,score[0][0])
        print(cursor.execute(sql_add,params_add))

        sql_modify_num = 'UPDATE db_course SET `"已收授人數"` = `"已收授人數"` + 1 WHERE `"選課代號"` = %s'
        params_modify_num = (courseid)
        cursor.execute(sql_modify_num,params_modify_num)

        sql_modify_score = 'UPDATE db_students SET `"已選學分"` = `"已選學分"` + %s WHERE `"學生學號"` = %s'
        params_modify_score = (score[0][0],stdid)
        cursor.execute(sql_modify_score,params_modify_score)

    # 退選
        courseid = "1317" #前端傳的值

        sql_score = 'SELECT `"學分數"` FROM `db_course` WHERE `"選課代號"` = %s'
        params_score = (courseid)
        cursor.execute(sql_score,params_score)
        score = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            score.append(line)

        sql_delete = 'DELETE FROM db_courseselected WHERE `"學生學號"` = %s AND `"已選課程代碼"` = %s'
        params_delete = (stdid,courseid)
        cursor.execute(sql_delete,params_delete)

        sql_modify_num = 'UPDATE db_course SET `"已收授人數"` = `"已收授人數"` - 1 WHERE `"選課代號"` = %s'
        params_modify_num = (courseid)
        cursor.execute(sql_modify_num,params_modify_num)

        sql_modify_score = 'UPDATE db_students SET `"已選學分"` = `"已選學分"` - %s WHERE `"學生學號"` = %s'
        params_modify_score = (score[0][0],stdid)
        cursor.execute(sql_modify_score,params_modify_score)



        
except Exception as ex:
    print(ex)






