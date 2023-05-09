# from pickle import EMPTY_LIST
from flask import Flask, render_template, request, url_for,redirect
from conn import *

app = Flask(__name__)
SID = "D0000000"

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    global SID
  
    if request.method == 'POST':
        stdid = request.form.get('student_id')
        stdps = request.form.get('password')
        flag = check_student_info(stdid,stdps)
        # if student is not EMPTY_LIST:
        if flag==1:
            SID = stdid
            # return render_template('index.html')
            return redirect(url_for('index'))
        else:
            return render_template('login.html')       
    return render_template('login.html')


# def login():
#     #  利用request取得使用者端傳來的方法為何
#     if request.method == 'POST':
#         stdid = request.form.get('student_id')
#         stdps = request.form.get('password')
#         student = get_student_info(stdid,stdps)                 
#         # if student is not EMPTY_LIST:
#         if student[]:                                 #flag
#             SID = student[0][1]

#             Student = []
#             for i in range(0,4):
#                 Student.append(student[0][i])

#             available_courses = get_selectable_courses(SID)
#             return render_template('index.html',Student = Student,available_courses = available_courses,)
#         else:
#             return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    student = get_student_info(SID)
    Student = []
    for i in range(0,4):
        Student.append(student[0][i])
    available_courses = get_selectable_courses(SID)
    courses = get_all_courses()
    # focus = get_focus_courses(SID)

    # selected_courses = get_selected_courses(SID)

    # return render_template('index.html',Student = Student, available_courses = available_courses, courses = courses,focus=focus)
    return render_template('index.html',Student = Student, available_courses = available_courses, courses = courses)

    # return '''
    # <html><body> 
    
    # %s</body></html>'''% c[0]

def index(course):
    student = get_student_info(SID)
    Student = []
    for i in range(0,4):
        Student.append(student[0][i])
    available_courses = get_selectable_courses(SID)
    courses = get_all_courses()
    course= get_search_course
    return render_template('index.html',Student = Student, available_courses = available_courses, courses = courses,course = course[0])
    # return
    # selected_courses = get_selected_courses(SID)



    # return render_template('index.html',Student = Student, available_courses = available_courses, courses = courses)



@app.route('/loookup', methods=['GET', 'POST'])
def lookup():#查看
    selected_courses = get_selected_courses(SID)
    table = get_timetable(SID)

    return render_template('lookup.html',selected_courses = selected_courses, table = table)
    # return '''
    # <html><body> 
    
    # {{selected_course}}</body></html>'''


@app.route('/add', methods=['GET', 'POST'])
def add():#加選
    if request.method == 'POST':
        corid = request.form.get('已選')
        if corid != "0000":
            add_course(SID, corid)
    return redirect(url_for('index'))


@app.route('/drop', methods=['GET', 'POST'])
def drop():#退選
    if request.method == 'POST':
        corid = request.form.get('退選')
        drop_course(SID, corid)
    return redirect(url_for('lookup'))


@app.route('/search', methods=['GET', 'POST'])
def search():#搜尋
    if request.method == 'POST':
        corid = request.form.get('code')
        course = get_search_course(corid)
    return redirect(url_for('index', course = course))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        SID = "D0000000"
        return render_template('login.html')
    
@app.route('/focus', methods=['GET', 'POST'])
def focus():
    if request.method == 'POST':
        corid = request.form.get('關注')
        if corid != "0000":
            add_focus(SID, corid)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
