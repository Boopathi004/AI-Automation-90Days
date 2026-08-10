import sqlite3

#create DataBase
connection = sqlite3.connect("company.db")

# Important for SQLite foreign keys
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

#create & insert departments

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

departments = [
    ("IT",),
    ("HR",),
    ("Finance",),
    ("Marketing",)
]

cursor.executemany("""
INSERT OR IGNORE INTO departments (name)
VALUES (?)
""", departments)

#create & insert employees

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary REAL CHECK(salary > 0),
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
)
""")

employees = [
    ("Boopathi", 60000, 1),
    ("Kumar", 50000, 2),
    ("Bala", 55000, 3),
    ("Arun", 45000, 1)
]

cursor.executemany("""
INSERT INTO employees
(name, salary, department_id)
VALUES (?, ?, ?)
""", employees)

connection.commit()

cursor.execute("""
SELECT
    employees.name,
    employees.salary,
    departments.name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;""")

details = cursor.fetchall()

print("Employee Details with Department:")
for row in details:
    print(f"Name: {row[0]}, Salary: {row[1]}, Department: {row[2]}")

cursor.execute("""SELECT
    e.name,
    e.salary,
    d.name AS department
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;""")

employee_details = cursor.fetchall()

print("Employee Details with Department:")
for row in employee_details:
    print(f"Name: {row[0]}, Salary: {row[1]}, Department: {row[2]}")

print("Database and tables created successfully with data inserted!")

cursor.execute("""SELECT
    e.name,
    e.salary,
    d.name AS department
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;""")

left_join_details = cursor.fetchall()

print("Employee Details with Department (LEFT JOIN):")
for row in left_join_details:
    print(f"Name: {row[0]}, Salary: {row[1]}, Department: {row[2]}")