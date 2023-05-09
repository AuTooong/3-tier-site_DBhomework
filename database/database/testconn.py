#!/usr/bin/python3.8

from connect import *
stdid = "D1060001"
courseid = "1310"

# 學生資料
student = get_student_info(stdid)
print(type(student[0][1]))

'''
# 已選課程
selected_courses = get_selected_courses(stdid)
print(selected_courses)

# 可選課程
available_courses = get_selectable_courses(stdid)
print(available_courses)

# 加選
add_course(stdid, "1310")

# 退選
drop_course(stdid, courseid)
'''