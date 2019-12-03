from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL       #

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
        usr = request.form['username']
        passwd = request.form['password']
        mycur = mysql.connection.cursor()
        sql = "Select * from admin_users where username = %s and passwd = %s"
        val = (usr, passwd)
        mycur.execute(sql, val)
        myresult = mycur.fetchall()
        if mycur.rowcount != 1:
            error = 'Invalid Credentials.'
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
        msg = emp_name
        return render_template('add_success.html', msg=msg)
    return render_template("add.html")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        eid = request.form['id']
        ename = request.form['emp_name']
        mycur = mysql.connection.cursor()
        sql = "Delete from employee where id = %s or emp_name= %s"
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
    mycur.execute("select * from logs")
    data = mycur.fetchall()

    return render_template("logs.html", data=data)


@app.route('/logs_search', methods=['GET', 'POST'])
def logs_search():
    if request.method == 'POST':
        eid = request.form['id']
        ename = request.form['emp_name']
        mycur = mysql.connection.cursor()
        sql = "select * from logs where emp_id = %s or emp_name= %s"
        val = (eid, ename)
        mycur.execute(sql, val)
        msg = mycur.fetchall()
        return render_template('logs_success.html', msg=msg)
    return render_template("logs_search.html")


@app.route('/employee')
def employee():
    mycur = mysql.connection.cursor()
    mycur.execute("select * from employee")
    data = mycur.fetchall()
    return render_template("employee.html", data=data)


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
