import sqlite3

connection = sqlite3.connect("employee_constraints.db")
cursor = connection.cursor()

name = input("Enter employee name: ")
email = input("Enter email: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")

try:
    cursor.execute("""
        INSERT INTO employees
        (name, email, salary, department)
        VALUES (?, ?, ?, ?)
    """, (name, email, salary, department))
    connection.commit()
    print("✅ Employee added successfully!")
except sqlite3.IntegrityError as e:
    print(f"❌ Error: {e}")
finally:
    connection.close()