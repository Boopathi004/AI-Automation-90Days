import sqlite3

conn = sqlite3.connect("employee1.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees1")

employees = cursor.fetchall()

print("=" * 80)
print("EMPLOYEE LIST")
print("=" * 80)

for emp in employees:
    print(emp)

conn.close()