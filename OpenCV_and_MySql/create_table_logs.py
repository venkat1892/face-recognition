import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_recognition')

c = conn.cursor()

sql = """
DROP TABLE IF EXISTS users;
create table logs(
   emp_id varchar(5) ,
   emp_name varchar(30),
   check_in timestamp,
   check_out timestamp);
"""
c.execute(sql)
print("Logs table created")

conn.close()