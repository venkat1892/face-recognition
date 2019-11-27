from flask import Flask, render_template, url_for, redirect, request, Response
from flask_mysqldb import MySQL
from camera import VideoCamera

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'face_recognition'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/success')
def success():
    return render_template("add_success.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = request.form['id']
        emp_name = request.form['emp_name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        blood_group = request.form['blood_group']
        mycur = mysql.connection.cursor()
        mycur.execute("Insert into employee(id, emp_name, dob, gender, email, phone, address, blood_group) values(%s, "
                      "%s, %s, %s, %s, %s, %s, %s)", (id, emp_name, dob, gender, email, phone, address, blood_group))
        mysql.connection.commit()
        mycur.close()
        # msg = emp_name
        return redirect(url_for('success'))
    return render_template("add.html")
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        eid = request.form['id']
        ename = request.form['emp_name']
        mycur = mysql.connection.cursor()
        sql = "Delete from employee where id = %s and emp_name= %s"
        val = (eid, ename)
        mycur.execute(sql, val)
        mysql.connection.commit()
        mycur.close()
        msg = eid
        return render_template('delete_success.html', msg=msg)
    return render_template("delete.html")


@app.route('/delete_success')
def delete_success():
    return render_template("delete_success.html")


@app.route('/logs')
def logs():
    mycur = mysql.connection.cursor()
    mycur.execute("select * from employee")
    data = mycur.fetchall()
    return render_template("logs.html", data=data)


@app.route('/update', methods=['get', 'post'])
def update():
    if request.method == 'POST':
        eid = request.form['id']
        phone = request.form['phone']
        address = request.form['address']
        mycur = mysql.connection.cursor()
        sql = "update employee set phone = %s , address = %s where id = %s"
        val = (phone, address, eid)
        mycur.execute(sql, val)
        msg = eid
        mysql.connection.commit()
        mycur.close()
        return render_template('update_success.html', msg=msg)
    return render_template("update.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        eid = request.form['id']
        ename = request.form['emp_name']
        mycur = mysql.connection.cursor()
        sql = "select * from employee where id = %s or emp_name= %s"
        val = (eid, ename)
        mycur.execute(sql, val)
        msg = mycur.fetchall()
        return render_template('search_success.html', msg=msg)
    return render_template("search.html")

if __name__ == '__main__':
    app.run(debug=True)
