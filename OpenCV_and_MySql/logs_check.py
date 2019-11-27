import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_recognition')

c = conn.cursor()

c.execute("SELECT * FROM logs")

myresult = c.fetchall()

for x in myresult:
    print(x)
