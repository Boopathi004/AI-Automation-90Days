import sqlite3

connection = sqlite3.connect('employee.db')
print("Database Created Successfully!")

connection.close()