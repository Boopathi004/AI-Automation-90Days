import sqlite3

def get_connection():
    return sqlite3.connect("employee_database.db")


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees_details(
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL,
        join_date TEXT,
        phone TEXT,
        email TEXT
    )
    """)
def add_employee(name, department, salary, join_date, phone, email):
   connection = sqlite3.connect('employee_database.db')
   cursor = connection.cursor()

   cursor.execute("""
    INSERT INTO employees_details (name, department, salary, join_date, phone, email)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, department, salary, join_date, phone, email))

def update_salary(emp_id, new_salary):
    conn = get_connection()
    cursor = conn.cursor()
      
    cursor.execute(
            "UPDATE employees_details SET salary=? WHERE id=?",
            (new_salary, emp_id)
        )
    cursor.execute("""
    UPDATE employees_details
    SET salary = ?
    WHERE id = ?
    """, (new_salary, emp_id))

def view_employees():
    conn = get_connection() 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees_details")
    employees = cursor.fetchall()
    for emp in employees:
        print(emp)
    

    conn.commit()
    conn.close()
    