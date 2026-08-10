import sqlite3

connection = sqlite3.connect("employee_constraints.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    salary REAL CHECK(salary > 0),
    department TEXT DEFAULT 'IT'
)
""")

connection.commit()
connection.close()

print("Employee table created successfully!")