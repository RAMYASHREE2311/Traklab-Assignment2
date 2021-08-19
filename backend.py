import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',database='empdepsystem')


if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_employee = """SELECT * FROM employees ORDER BY empname DESC"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()
p = []
tbl ="<tr><td>ID</td><td>Name</td><td>Age</td><td>department</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)
    d = "<td>%s</td></tr>"%row[3]
    p.append(d)    


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

filename1 = 'webbrowser.html'

def main(contents, filename1):
    output = open(filename1,"w")
    output.write(contents)
    output.close()
main(contents, filename1)    
webbrowser.open(filename1)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")    

