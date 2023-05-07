from flask import Flask, render_template, request, url_for

app = Flask(__name__)



@app.route('/search', methods=['GET','POST'])
def search():
   ''' code = request.form['code']
    # 在此處使用代碼進行查詢並返回課程信息
    course_info = get_course_info(code)
    return render_template('search.html', course_info=course_info)'''

@app.route('/select', methods=['POST'])
def selection():


    return render_template('select.html')

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     #  利用request取得使用者端傳來的方法為何
#     if request.method == 'POST':
#                           #  利用request取得表單欄位值
#         return render_template('search.html')

#     #  非POST的時候就會回傳一個空白的模板
#     return render_template('login.html')

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('search'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("login.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

