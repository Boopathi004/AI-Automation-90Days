import sqlite3
connection = sqlite3.connect('employee1.db')
print("Database Created Successfully!")

cursor = connection.cursor()

name = input("Enter Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
join_date = input("Enter Joining Date (YYYY-MM-DD): ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

#create table if not exists

cursor.execute("""CREATE TABLE IF NOT EXISTS employees1
                  (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, join_date TEXT, phone_number TEXT, email TEXT)""")

print("Table Created Successfully!")

#insert data into the table

cursor.execute("""
INSERT INTO employees1
(name, department, salary, join_date, phone_number, email)
VALUES (?, ?, ?, ?, ?, ?)
""", (name, department, salary, join_date, phone, email))

print("Data Inserted Successfully!")

connection.commit()
connection.close()
