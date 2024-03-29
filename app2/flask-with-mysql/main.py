from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='/app2/templates/')


app.config['MYSQL_HOST'] = '192.168.1.2'
app.config['MYSQL_USER'] = 'app2'
app.config['MYSQL_PASSWORD'] = 'P@$$w0rd'
app.config['MYSQL_DB'] = 'app2'

mysql = MySQL(app)


@app.route('/app1', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers (FirstName, LastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

