# from pickle import EMPTY_LIST
from flask import Flask, render_template, request, url_for,redirect
from conn import *

app = Flask(__name__)
SID = "D0000000"

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    global SID
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        stdid = request.form.get('student_id')
        stdps = request.form.get('password')
        flag = check_student_info(stdid,stdps)
        # if student is not EMPTY_LIST:
        if flag==1:
            SID = stdid
            
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
    return render_template('index.html',Student = Student,available_courses = available_courses)




@app.route('/loookup', methods=['GET', 'POST'])
def lookup():#查看
    selected_courses = get_selected_courses(SID)
    return render_template('lookup.html', selected_courses = selected_courses)


@app.route('/add', methods=['GET', 'POST'])
def add():#加選
    if request.method == 'POST':
        corid = request.form.get('corid')
        add_course(SID, corid)
    return redirect(url_for('index'))


@app.route('/drop', methods=['GET', 'POST'])
def drop():#退選
    if request.method == 'POST':
        corid = request.form.get('corid')
        drop_course(SID, corid)
    return redirect(url_for('lookup'))


@app.route('/search', methods=['GET', 'POST'])
def search():#搜尋
    if request.method == 'POST':
        selected_courses = get_selected_courses(SID)
    return render_template('search.html', selected_courses = selected_courses)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        SID = "D0000000"
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
