import sqlite3

conn = sqlite3.connect("employee1.db")
cursor = conn.cursor()

name = input("Enter Employee Name: ")
salary = float(input("Enter New Salary: "))

cursor.execute("""
UPDATE employees1
SET salary = ?
WHERE name = ?
""", (salary, name))

conn.commit()

print("\n✅ Salary Updated Successfully!")

conn.close()