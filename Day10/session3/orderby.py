import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM employees_details
ORDER BY salary DESC
""")

employees = cursor.fetchall()

print("=" * 70)
print("EMPLOYEES SORTED BY SALARY")
print("=" * 70)

for emp in employees:
    print(emp)

conn.close()