from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

"""@app.route('/')
def login():
    return render_template("login.html")  """


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


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/update')
def update():
    return render_template("update.html")


if __name__ == '__main__':
    app.run(debug=True)
