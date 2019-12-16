import xlwt
import MySQLdb
import os

# Establish a MySQL connection
database = MySQLdb.connect(host="localhost", user="root", passwd="root", db="my_excel")
cursor = database.cursor()
query = "Select * from employee"
cursor.execute(query)
result = cursor.fetchall()
for x in result:
    print(x)
os.chdir("C:/Users/LENOVO/PycharmProjects/flask_projects")
filename = input("Please enter the file name to be saved,No suffix required: ") + '.xlsx'
wbk = xlwt.Workbook(encoding='utf-8')
test = wbk.add_sheet('test', cell_overwrite_ok=True)
# How to get column names
fileds = [u'emp_id', u'emp_name', u'phone', u'gender']
trans_data = list(result)
# Write column names
for filed in range(0, len(fileds)):
    test.write(0, filed, fileds[filed])
for row in range(1, len(trans_data) + 1):
    for col in range(0, len(fileds)):
        test.write(row, col, str(trans_data[row - 1][col]))
wbk.save(filename)
print(filename + " is succesfully created")
