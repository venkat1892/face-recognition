import xlrd
import MySQLdb

# Open the workbook and define the worksheet
# file = input("Enter the file name with extension ")
book = xlrd.open_workbook("import_details.xlsx")
sheet = book.sheet_by_name("Data")
# Establish a MySQL connection
database = MySQLdb.connect(host="localhost", user="root", passwd="root", db="my_excel")
# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()
# Create the INSERT INTO sql query
query = "INSERT Ignore INTO employee (emp_id, emp_name, phone, gender) VALUES (%s, %s, %s, %s)"
# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
# try:
for r in range(1, sheet.nrows):
    emp_id = sheet.cell(r, 0).value
    emp_name = sheet.cell(r, 1).value
    phone = sheet.cell(r, 2).value
    gender = sheet.cell(r, 3).value
    # Execute sql Query
    values = (emp_id, emp_name, phone, gender)
    cursor.execute(query, values)
cursor.close()
# close the cursor

# Commit the transaction
database.commit()

# Close the database connection
database.close()
# Print results
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported "+columns+" columns and "+rows+" rows to MySQL!")
