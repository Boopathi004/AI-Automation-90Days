import sqlite3
# Create a database connection and enable foreign key support

DB_NAME = "company.db"


def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            salary REAL NOT NULL CHECK(salary > 0),
            department_id INTEGER NOT NULL,
            FOREIGN KEY (department_id)
                REFERENCES departments(id)
        )
    """)

    connection.commit()
    connection.close()

    print("✅ Database initialized successfully.")

# Adding Default Departments 

def add_default_departments():
     connection = get_connection()
     cursor = connection.cursor()
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

     connection.commit()
     connection.close()

# Adding Employess 

def add_employee():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        name = input("Enter employee name: ").strip()
        email = input("Enter email: ").strip()
        salary = float(input("Enter salary: "))
        department_id = int(input("Enter department ID: "))

        cursor.execute("""
            INSERT INTO employees
            (name, email, salary, department_id)
            VALUES (?, ?, ?, ?)
        """, (name, email, salary, department_id))

        connection.commit()

        print("✅ Employee added successfully.")

    except ValueError:
        print("❌ Please enter valid numeric values.")

    except sqlite3.IntegrityError as error:
        print(f"❌ Database error: {error}")

    finally:
        connection.close()

#view Employees 
def view_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.email,
            e.salary,
            d.name AS department
        FROM employees e
        INNER JOIN departments d
            ON e.department_id = d.id
        ORDER BY e.id
    """)

    employees = cursor.fetchall()

    print("\n========== EMPLOYEES ==========")

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)

    connection.close()

#Search Employees

def search_employee():
    connection = get_connection()
    cursor = connection.cursor()

    name = input("Enter employee name: ").strip()

    cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.email,
            e.salary,
            d.name AS department
        FROM employees e
        INNER JOIN departments d
            ON e.department_id = d.id
        WHERE e.name LIKE ?
    """, (f"%{name}%",))

    employees = cursor.fetchall()

    if employees:
        for employee in employees:
            print(employee)
    else:
        print("❌ No employee found.")

    connection.close()

#update Employees

def update_employee():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        employee_id = int(input("Enter employee ID to update: "))
        new_name = input("Enter new name: ").strip()
        new_email = input("Enter new email: ").strip()
        new_salary = float(input("Enter new salary: "))
        new_department_id = int(input("Enter new department ID: "))

        cursor.execute("""
            UPDATE employees
            SET name = ?, email = ?, salary = ?, department_id = ?
            WHERE id = ?
        """, (new_name, new_email, new_salary, new_department_id, employee_id))

        if cursor.rowcount == 0:
            print("❌ No employee found with the given ID.")
        else:
            connection.commit()
            print("✅ Employee updated successfully.")

    except ValueError:
        print("❌ Please enter valid numeric values.")

    except sqlite3.IntegrityError as error:
        print(f"❌ Database error: {error}")

    finally:
        connection.close()
#delete Employees
def delete_employee():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        employee_id = int(input("Enter employee ID to delete: "))

        cursor.execute("""
            DELETE FROM employees
            WHERE id = ?
        """, (employee_id,))

        if cursor.rowcount == 0:
            print("❌ No employee found with the given ID.")
        else:
            connection.commit()
            print("✅ Employee deleted successfully.")

    except ValueError:
        print("❌ Please enter a valid numeric value.")

    finally:
        connection.close()

# Department Reports

def department_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            d.name AS department,
            COUNT(e.id) AS employee_count,
            AVG(e.salary) AS average_salary,
            SUM(e.salary) AS total_salary
        FROM departments d
        LEFT JOIN employees e
            ON d.id = e.department_id
        GROUP BY d.id, d.name
        ORDER BY d.name
    """)

    reports = cursor.fetchall()

    print("\n========== DEPARTMENT REPORT ==========")

    for report in reports:
        print(
            f"Department: {report[0]} | "
            f"Employees: {report[1]} | "
            f"Average Salary: {report[2] or 0:.2f} | "
            f"Total Salary: {report[3] or 0:.2f}"
        )

    connection.close()

# Highest Salary Employee

def highest_salary_employee():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.email,
            e.salary,
            d.name AS department
        FROM employees e
        INNER JOIN departments d
            ON e.department_id = d.id
        ORDER BY e.salary DESC
        LIMIT 1
    """)

    employee = cursor.fetchone()

    if employee:
        print("\n========== HIGHEST SALARY EMPLOYEE ==========")
        print(employee)
    else:
        print("❌ No employees found.")

    connection.close()

# Average Salary employee
def average_salary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT AVG(salary) FROM employees
    """)

    average_salary = cursor.fetchone()[0]

    print(f"\nAverage Salary of Employees: {average_salary:.2f}" if average_salary else "No employees found.")

    connection.close()
# Employee Count 
def employee_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM employees
    """)

    count = cursor.fetchone()[0]

    print(f"\nTotal Number of Employees: {count}")

    connection.close()

# Main Menu 
def main():

    create_tables()
    add_default_departments()

    while True:

        print("""
========================================
       COMPANY MANAGEMENT SYSTEM
========================================

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Department Report
7. Highest Salary
8. Average Salary
9. Employee Count
10. Exit

========================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            department_report()

        elif choice == "7":
            highest_salary_employee()

        elif choice == "8":
            average_salary()

        elif choice == "9":
            employee_count()

        elif choice == "10":
            print("👋 Thank you for using Company Management System.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()