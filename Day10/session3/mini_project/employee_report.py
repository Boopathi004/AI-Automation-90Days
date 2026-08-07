import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

print("=" * 60)
print("EMPLOYEE REPORT")
print("=" * 60)

cursor.execute("SELECT COUNT(*) FROM employees_details")
print("Total Employees :", cursor.fetchone()[0])

cursor.execute("SELECT AVG(salary) FROM employees_details")
print("Average Salary :", round(cursor.fetchone()[0], 2))

cursor.execute("SELECT MAX(salary) FROM employees_details")
print("Highest Salary :", cursor.fetchone()[0])

cursor.execute("SELECT MIN(salary) FROM employees_details")
print("Lowest Salary :", cursor.fetchone()[0])

cursor.execute("""
SELECT * FROM employees_details
ORDER BY salary DESC
""")

print("\nEmployees Ranked by Salary\n")

for emp in cursor.fetchall():
    print(emp)

conn.close()