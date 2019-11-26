import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_opencv')

c = conn.cursor()

sql = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
           id integer unique primary key auto_increment,
           name text,
           emp_id varchar(5) unique
);
"""
c.execute(sql)
print("Users table created")

conn.close()