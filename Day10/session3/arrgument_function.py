import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM employees_details")
print("Total Employees :", cursor.fetchone()[0])

cursor.execute("SELECT SUM(salary) FROM employees_details")
print("Total Salary :", cursor.fetchone()[0])

cursor.execute("SELECT AVG(salary) FROM employees_details")
print("Average Salary :", cursor.fetchone()[0])

cursor.execute("SELECT MAX(salary) FROM employees_details")
print("Highest Salary :", cursor.fetchone()[0])

cursor.execute("SELECT MIN(salary) FROM employees_details")
print("Lowest Salary :", cursor.fetchone()[0])

conn.close()