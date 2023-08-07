import os
from flask import Flask,render_template,url_for,session,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

#Home page routing start
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/")
def home():
    return render_template('index.html')
#Home page routing end
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("form.html")
     
    if request.method == 'POST':
        name = request.form['ism']
        age = request.form['yosh']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(%s,%s)',(name,age))
        mysql.connection.commit()
        cursor.close()
        return redirect('/show')
    

@app.route('/show')
def show():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')
    result=cursor.fetchall()
    cursor.close()
    return render_template('show.html',result=result)

        

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

if(__name__=='__main__'):
    app.run(debug=True,use_reloader=True)