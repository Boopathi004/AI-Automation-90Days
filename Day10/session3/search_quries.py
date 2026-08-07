import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

dept = input("Enter Department: ")

cursor.execute("""
SELECT * FROM employees_details
WHERE department = ?
""", (dept,))

employees = cursor.fetchall()

if employees:
    print("\nEmployees Found\n")
    for emp in employees:
        print(emp)
else:
    print("No Employees Found.")

conn.close()