import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", auth_plugin='mysql_native_password')


c = conn.cursor()
sql = """ 
DROP DATABASE IF EXISTS face_opencv;
    CREATE DATABASE face_opencv; """

c.execute(sql)
print("Database created: face_openCV")


conn.close()

