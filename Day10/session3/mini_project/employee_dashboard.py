import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()


def view_all():
    cursor.execute("SELECT * FROM employees_details")
    employees = cursor.fetchall()

    print("\n========== EMPLOYEES ==========")

    for emp in employees:
        print(emp)


def highest_salary():
    cursor.execute("""
    SELECT * FROM employees_details
    ORDER BY salary DESC
    LIMIT 1
    """)

    print("\nHighest Salary Employee")
    print(cursor.fetchone())


def lowest_salary():
    cursor.execute("""
    SELECT * FROM employees_details
    ORDER BY salary ASC
    LIMIT 1
    """)

    print("\nLowest Salary Employee")
    print(cursor.fetchone())


def average_salary():
    cursor.execute("""
    SELECT AVG(salary)
    FROM employees_details
    """)

    avg = cursor.fetchone()[0]

    print(f"\nAverage Salary : ₹{avg:.2f}")


def total_salary():
    cursor.execute("""
    SELECT SUM(salary)
    FROM employees_details
    """)

    total = cursor.fetchone()[0]

    print(f"\nTotal Salary : ₹{total:.2f}")


def total_employees():
    cursor.execute("""
    SELECT COUNT(*)
    FROM employees_details
    """)

    total = cursor.fetchone()[0]

    print(f"\nTotal Employees : {total}")


def department_wise():
    cursor.execute("""
    SELECT department, COUNT(*)
    FROM employees_details
    GROUP BY department
    """)

    rows = cursor.fetchall()

    print("\nEmployees By Department")

    for row in rows:
        print(f"{row[0]} : {row[1]}")


def sort_salary():
    cursor.execute("""
    SELECT *
    FROM employees_details
    ORDER BY salary DESC
    """)

    employees = cursor.fetchall()

    print("\nEmployees Sorted By Salary")

    for emp in employees:
        print(emp)


while True:

    print("\n========== EMPLOYEE DASHBOARD ==========")
    print("1. View All Employees")
    print("2. Highest Salary Employee")
    print("3. Lowest Salary Employee")
    print("4. Average Salary")
    print("5. Total Salary")
    print("6. Total Employees")
    print("7. Employees by Department")
    print("8. Sort by Salary")
    print("9. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        view_all()

    elif choice == "2":
        highest_salary()

    elif choice == "3":
        lowest_salary()

    elif choice == "4":
        average_salary()

    elif choice == "5":
        total_salary()

    elif choice == "6":
        total_employees()

    elif choice == "7":
        department_wise()

    elif choice == "8":
        sort_salary()

    elif choice == "9":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice")

conn.close()