import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER
)
""")

connection.commit()

print("Database and table created successfully!")

cursor.execute("""
INSERT INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?)
""", (101, "Boopathi", "AI Engineering", 50000))

cursor.execute("""
INSERT INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?)
""", (102, "Arun", "HR", 45000))

cursor.execute("""
INSERT INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?)
""", (103, "Kumar", "IT", 55000))

connection.commit()
cursor.execute("SELECT * FROM employees")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

connection.close()