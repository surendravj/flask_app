
from ast import Try
import MySQLdb
from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6529338'
app.config['MYSQL_PASSWORD'] = 'nsCdp5h8vi'
app.config['MYSQL_DB'] = 'sql6529338'

mysql = MySQL(app)


@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from putatoe")
        data = cur.fetchall()
        cur.close()
        return '"{}"."{}"'.format(data[0][1], data[0][1])
    except MySQLdb.Error as e:
        return "Unable to connect database"


@app.route('/admin', methods=['GET', "POST"])
def admin():
    if request.method == "POST":
        word = request.form['word']
        try:
            cur = mysql.connection.cursor()
            cur.execute('UPDATE putatoe '
                        'SET word =%s'
                        'WHERE id =1',
                        [word])
            mysql.connection.commit()
            cur.close()
            return redirect("/", code=302)
        except MySQLdb.Error as e:
            return "Unable to connect database"
    else:
        return render_template('./admin.html')
