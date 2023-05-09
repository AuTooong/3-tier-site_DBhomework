#!/usr/bin/python3.8

import pymysql

db_settings = {
     "host": "127.0.0.1",
     "port": 3306,
     "user": "test",
     "password": "test",
     "db": "mid_courseselectsystem",
     "charset": "utf8"
}

def check_student_info(stdid,password):
    conn = pymysql.connect(**db_settings)
    flag = 0
    with conn.cursor() as cursor:
        sql_std = 'SELECT * FROM `db_students` WHERE `"學生學號"` = %s AND `"密碼"` = %s'
        params_std = (stdid, password)
        cursor.execute(sql_std,params_std)
        if cursor.fetchone() is not None:
            flag = 1  # 找到了
        cursor.close()
    conn.close()
    return flag


def get_student_info(stdid):
    conn = pymysql.connect(**db_settings)
    student = []
    with conn.cursor() as cursor:
        sql_std = 'SELECT * FROM `db_students` WHERE `"學生學號"` = %s'
        params_std = (stdid)
        cursor.execute(sql_std,params_std)
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            student.append(line)
        cursor.close()
    conn.close()
    return student

def get_search_course(courid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # if flag == 1:#
        sql_search = 'SELECT * from `db_course` LEFT JOIN `db_coursetime` ON `db_course`.`"選課代號"`= `db_coursetime`.`"選課代號"`where `db_course`.`"選課代號"` = %s;'
        params_search = (courid)
        cursor.execute(sql_search,params_search)

        search = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            search.append(line)
        return search
        # if flag == 2:#全
        #     sql_search = 'SELECT * from `db_course` LEFT JOIN `db_coursetime` ON `db_course`.`"選課代號"`= `db_coursetime`.`"選課代號"`where `db_course`.`"選課代號"` = %s;'
        #     params_search = (courid)
        #     cursor.execute(sql_search,params_search)

        #     search = []
        #     for row in cursor:
        #         line = []
        #         for i in row:
        #             line.append(i)
        #         search.append(line)
        #     return search


    
def get_focus_courses(stdid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        sql_focus = 'SELECT * FROM db_studentsfocus LEFT JOIN db_coursetime ON ddb_studentsfocus.`"選課代號"`= db_coursetime.`"選課代號"` where db_studentsfocus.`"選課代號"` IN (SELECT `"已關注課程代碼"` FROM db_studentsfocus where `"學生學號"` = %s GROUP by `"已關注課程代碼"`) GROUP by db_studentsfocus.`"選課代號"`'
        params_focus = (stdid)
        cursor.execute(sql_focus,params_focus)

        focus = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            focus.append(line)
            for i in cursor:
            # 判斷是否已選
                flag = 1
                i.append(flag) 
        return focus
    
def get_all_courses():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        sql_courses = 'SELECT DISTINCT * FROM db_course LEFT JOIN db_coursetime ON db_course.`"選課代號"`= db_coursetime.`"選課代號"` GROUP by db_course.`"選課代號"`'
        cursor.execute(sql_courses)
        courses = []
        for row in cursor.fetchall():
            line = []
            for i in row:
                line.append(i)
            courses.append(line)
        for i in cursor:
            # 判斷是否已選
            flag = 0
            i.append(flag) 
        return courses




def get_selected_courses(stdid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        sql_selected = 'SELECT * FROM db_course LEFT JOIN db_coursetime ON db_course.`"選課代號"`= db_coursetime.`"選課代號"` where db_course.`"選課代號"` IN (SELECT `"已選課程代碼"` FROM db_courseselected where `"學生學號"` = %s GROUP by `"已選課程代碼"`) GROUP by db_course.`"選課代號"`'
        params_selected = (stdid)
        cursor.execute(sql_selected,params_selected)

        selected = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            selected.append(line)
        return selected
 

def get_selectable_courses(stdid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        sql_selectable = 'SELECT * from db_course LEFT JOIN db_coursetime ON `db_course`.`"選課代號"`= `db_coursetime`.`"選課代號"` where `db_course`.`"選課代號"` NOT IN (SELECT `"選課代號"` from db_course WHERE db_course.`"開課科系"` IN (SELECT SUBSTR(`"學生班級"`, 1,2) as class FROM db_students where `"學生學號"` = %s GROUP by class) and db_course.`"開課年級"` IN (SELECT SUBSTR(`"學生班級"`, 3,1) as grade FROM db_students where `"學生學號"` = %s GROUP by grade) and db_course.`"必選修"` = "M" GROUP BY db_course.`"選課代號"`) GROUP BY db_course.`"選課代號"`;'
        params_selectable = (stdid,stdid)
        cursor.execute(sql_selectable,params_selectable)

        selectable = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            selectable.append(line)

        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            selectable.append(line)

        flag = 0 # 0:可選 1:已滿 2:衝堂 3:超分 4:已選 5.不可選碩 
        
        selected = get_selected_courses(stdid)
        student = get_student_info(stdid)

        for i in selectable:
            # 判斷是否已選
            flag = 0
            for j in selected:
                if i[0] == j[0]:
                    flag = 4
                    break
            # 判斷是否已選滿 
            if i[9] >= i[8] and flag != 2:
                flag = 1


            # 判斷是否衝堂
            for j in selected:
                # i 要選的課程 j 已選的課程
                # 13:星期 14:開始時間 15:結束時間
                if ((i[13] == j[13]) and ((int(i[14]) >= int(j[14]) and int(i[14]) <= int(j[15])) or (int(i[15]) >= int(j[14]) and int(i[15]) <= int(j[15])) or (int(i[14]) <= int(j[14]) and int(i[15]) >= int(j[15])))) and flag != 2:
                    flag = 2
                    break

            # 判斷是否超過學分
            if int(i[5]) + int(student[0][3]) > 30 and flag != 2:
                flag = 3
         

            # 判斷為碩班課
            for j in selected:
                if (student[0][2][2:2] !="碩" and i[4] == "碩一" ):
                    flag = 5
                


            i.append(flag) 

        return selectable
# 加關注
def add_focus(stdid,courseid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:     
        student = get_student_info(stdid)
        course = get_search_course(courseid)
    
        sql_add = 'INSERT INTO db_studentsfocus (`"學生姓名 "`, `"學生學號"`, `"學生班級"`, `"已關注課程代碼"`) VALUES (%s,%s,%s,%s)'
        params_add = (student[0][0], student[0][1], student[0][2], courseid)
        cursor.execute(sql_add, params_add)

        conn.commit()


 # 加選
def add_course(stdid,courseid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # 查詢學分數
        sql_score = 'SELECT `"學分數"` FROM `db_course` WHERE `"選課代號"` = %s'
        params_score = (courseid)
        cursor.execute(sql_score,params_score)
        score = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            score.append(line)
         
        student = get_student_info(stdid)
        course = get_search_course(courseid)
    
        if((int(student[0][3]) + int(course[0][5]))<=30):
            # 插入已選課程
            sql_add = 'INSERT INTO db_courseselected (`"學生姓名 "`, `"學生學號"`, `"學生班級"`, `"已選課程代碼"`, `"學分數"`) VALUES (%s,%s,%s,%s,%s)'
            params_add = (student[0][0], student[0][1], student[0][2], courseid, score)
            cursor.execute(sql_add, params_add)

            # 修改已收授人數
            sql_modify_num = 'UPDATE db_course SET `"已收授人數"` = `"已收授人數"` + 1 WHERE `"選課代號"` = %s'
            params_modify_num = (courseid)
            cursor.execute(sql_modify_num, params_modify_num)

            # 修改已選學分
            sql_modify_score = 'UPDATE db_students SET `"已選學分"` = `"已選學分"` + %s WHERE `"學生學號"` = %s'
            params_modify_score = (score, stdid)
            cursor.execute(sql_modify_score, params_modify_score)

        conn.commit()


 # # 退選
def drop_course(stdid, courseid):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # 查詢學分數
        sql_score = 'SELECT `"學分數"` FROM `db_course` WHERE `"選課代號"` = %s'
        params_score = (courseid)
        cursor.execute(sql_score,params_score)
        score = []
        for row in cursor:
            line = []
            for i in row:
                line.append(i)
            score.append(line)
         
        student = get_student_info(stdid)
        course = get_search_course(courseid)

        if((int(student[0][3]) - int(course[0][5]))>= 12):    
            sql_delete = 'DELETE FROM db_courseselected WHERE `"學生學號"` = %s AND `"已選課程代碼"` = %s'
            params_delete = (stdid,courseid)
            cursor.execute(sql_delete,params_delete)

            sql_modify_num = 'UPDATE db_course SET `"已收授人數"` = `"已收授人數"` - 1 WHERE `"選課代號"` = %s'
            params_modify_num = (courseid)
            cursor.execute(sql_modify_num,params_modify_num)

            sql_modify_score = 'UPDATE db_students SET `"已選學分"` = `"已選學分"` - %s WHERE `"學生學號"` = %s'
            params_modify_score = (score[0][0],stdid)
            cursor.execute(sql_modify_score,params_modify_score)

            conn.commit()
        
            # # sql_score1 = 'SELECT `"必選修"` FROM `db_course` WHERE `"選課代號"` = %s'
            # # params_score = (courseid)
            # # cursor.execute(sql_score1,params_score)
            # # score1 = []
            # # for row in cursor:
            # #     line = []
            # # for i in row:
            # #     line.append(i)
            # # score1.append(line)
            # # if(score1[0] != 'M'):
            # sql_delete = 'DELETE FROM db_courseselected WHERE `"學生學號"` = %s AND `"已選課程代碼"` = %s'
            # params_delete = (stdid,courseid)
            # cursor.execute(sql_delete,params_delete)

            # sql_modify_num = 'UPDATE db_course SET `"已收授人數"` = `"已收授人數"` - 1 WHERE `"選課代號"` = %s'
            # params_modify_num = (courseid)
            # cursor.execute(sql_modify_num,params_modify_num)

            # sql_modify_score = 'UPDATE db_students SET `"已選學分"` = `"已選學分"` - %s WHERE `"學生學號"` = %s'
            # params_modify_score = (score[0][0],stdid)
            # cursor.execute(sql_modify_score,params_modify_score)

            # conn.commit()
            



## 課表
def get_timetable(stdid):
    selected = get_selected_courses(stdid)
    result = [["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""],
              ["","","","","","","",""]]
    for i in selected:
        x = 0
        y = 0
        if i[13] == "一":
            x = 1
        elif i[13] == "二":
            x = 2
        elif i[13] == "三":
            x = 3
        elif i[13] == "四":
            x = 4
        elif i[13] == "五":
            x = 5
        elif i[13] == "六":
            x = 6
        elif i[13] == "日":
            x = 7
        for j in range(int(i[15])-int(i[14])+1):
            result[int(i[14])+j-1][x] = str(i[0])+" "+str(i[1])
    
    result[0][0] = "08:10~09:00"
    result[1][0] = "09:10~10:00"
    result[2][0] = "10:10~11:00"
    result[3][0] = "11:10~12:00"
    result[4][0] = "12:10~13:00"
    result[5][0] = "13:10~14:00"
    result[6][0] = "14:10~15:00"
    result[7][0] = "15:10~16:00"
    result[8][0] = "16:10~17:00"
    result[9][0] = "17:10~18:00"
    result[10][0] = "18:30~19:20"
    result[11][0] = "19:25~20:15"
    result[12][0] = "20:25~21:15"
    result[13][0] = "21:20~22:10"
    return result
