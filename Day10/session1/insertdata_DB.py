import sqlite3
connection = sqlite3.connect('test.db')
cursor = connection.cursor()
cursor.execute("""
INSERT INTO employees
(id, name, department, salary, join_date, phone_number, email)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    2,
    "Boopathi",
    "IT",
    50000.0,
    "2024-06-10",
    "123-456-7890",
    "boopathi@example.com"
))
connection.commit()
print("Data Inserted Successfully!")
connection.close()