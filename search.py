from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello world from Flask!"
if __name__ == "__main__":
    app.run()
# library.py
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empdepsystem'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        employees = request.form['employees']
        # search by author or book
        cursor.execute("SELECT empname,department from employees WHERE depname LIKE med% OR author LIKE %l", (employees,employees))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and employees == 'all': 
            cursor.execute("SELECT empname, department from employees")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')
if __name__ == '__main__':
    app.debug = True
    app.run()
