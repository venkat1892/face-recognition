import cv2
import numpy as np
import mysql.connector
import os
from datetime import datetime, date

conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database='face_recognition', buffered=True)
c = conn.cursor()
fname = "recognizer/trainingData.yml"
if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        ids, conf = recognizer.predict(gray[y:y + h, x:x + w])
        c.execute("select name,emp_id,id from users where id = (%s);", (ids,))
        result = c.fetchall()
        name = result[0][0]
        emp_id = result[0][1]

        if conf < 50:
            cv2.putText(img, name + str(round(conf, 2)), (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0),
                        2)
            sql = "select check_out from logs where emp_id = %s  and check_out is null"
            val = emp_id
            c.execute(sql, (val,))
            res = c.fetchone()
            row_count = c.rowcount
            if row_count == 1:
                now = datetime.now()
                sql = "update logs set check_out = %s where emp_id = %s and check_out is null"
                val = (now, emp_id)
                c.execute(sql, val)

        else:
            cv2.putText(img, 'No Match', (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Face Recognizer', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
conn.commit()
conn.close()
cap.release()
cv2.destroyAllWindows()
