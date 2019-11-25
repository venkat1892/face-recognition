import cv2
import numpy as np
import mysql.connector
import os

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_opencv')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

uname = input("Enter your name: ")
emp_id = input("Enter Employee_id ")
# sql = 'Insert into users (uid,uname) values (%s,%s)'
# val = (uid, uname)
# c.execute('INSERT INTO users (name,uid) VALUES (%s,%s)', (uname,uid))
c.execute('INSERT INTO users (name,emp_id) VALUES (%s,%s)', (uname, emp_id, ))

# c.execute(sql,val)
uid = c.lastrowid

sampleNum = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataset/User." + str(uid) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.waitKey(500)
    cv2.imshow('img', img)
    cv2.waitKey(1);
    if sampleNum > 20:
        break
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
