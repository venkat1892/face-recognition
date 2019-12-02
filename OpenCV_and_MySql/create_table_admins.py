import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_recognition')

c = conn.cursor()

sql = """
DROP TABLE IF EXISTS admin_users;
create table admin_users(
   username varchar(10) ,
   passwd varchar(10));
"""
c.execute(sql)
print("Admin_users table created")

conn.close()