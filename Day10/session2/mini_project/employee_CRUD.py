import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Employees Salary > 50000")
    print("7. Total Employees")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        cursor.execute("""CREATE TABLE IF NOT EXISTS employees_details
                  (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, join_date TEXT, phone TEXT, email TEXT)""")

        print("Table Created Successfully!")

        name = input("Name: ")
        department = input("Department: ")
        salary = float(input("Salary: "))
        join_date = input("Joining Date: ")
        phone = input("Phone: ")
        email = input("Email: ")

        cursor.execute("""
        INSERT INTO employees_details
        (name, department, salary, join_date, phone_number, email)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, department, salary, join_date, phone, email))

        conn.commit()
        print("✅ Employee Added")

    elif choice == "2":

        cursor.execute("SELECT * FROM employees_details")

        for emp in cursor.fetchall():
            print(emp)

    elif choice == "3":

        emp_id = int(input("Employee ID: "))
        salary = float(input("New Salary: "))

        cursor.execute(
            "UPDATE employees_details SET salary=? WHERE id=?",
            (salary, emp_id)
        )

        conn.commit()

        print("✅ Salary Updated")

    elif choice == "4":

        emp_id = int(input("Employee ID: "))

        cursor.execute(
            "SELECT * FROM employees_details WHERE id=?",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee:
            cursor.execute(
                "DELETE FROM employees_details WHERE id=?",
                (emp_id,)
            )
            conn.commit()
            print("✅ Employee Deleted")
        else:
            print("❌ Employee Not Found")
            
    elif choice == "5":
        name = input("Enter Employee Name: ")

        cursor.execute(
            "SELECT * FROM employees_details WHERE name LIKE ?",
            ('%' + name + '%',)
        )
        employees = cursor.fetchall()

        if employees:
            print("\nEmployee Found\n")
            for emp in employees:
                print(emp)
        else:
            print("\n❌ Employee Not Found")

    elif choice == "6":
        cursor.execute("SELECT * FROM employees_details WHERE salary > ?", (50000,))
        employees = cursor.fetchall()

        if employees:
            print("\nEmployees with Salary > 50000\n")
            for emp in employees:
                print(emp)
        else:
            print("\n❌ No Employees Found with Salary > 50000")

    elif choice == "7":
        cursor.execute("SELECT COUNT(*) FROM employees_details")
        total_employees = cursor.fetchone()[0]
        print(f"\nTotal Employees: {total_employees}")

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

conn.close()