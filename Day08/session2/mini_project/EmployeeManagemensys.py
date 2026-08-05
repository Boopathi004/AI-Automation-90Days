import csv
import os

FILENAME = "employees.csv"


# Create CSV File
def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["ID", "Name", "Department", "Salary", "Email", "Joining Date"]
            )
        print("Employee file created successfully.")
    else:
        print("Employee file already exists.")


# Add Employee
def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    email = input("Enter Email: ")
    joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [emp_id, name, department, salary, email, joining_date]
        )

    print("Employee added successfully.\n")


# View Employees
def view_employees():
    print("\n========== Employee Records ==========\n")

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


# Search Employee
def search_employee():
    search_id = input("Enter Employee ID: ")

    found = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[0] == search_id:
                print("\nEmployee Found")
                print(row)
                found = True
                break

    if not found:
        print("Employee Not Found.\n")


# Update Salary
def update_salary():
    search_id = input("Enter Employee ID: ")
    new_salary = input("Enter New Salary: ")

    employees = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        employees.append(header)

        updated = False

        for row in reader:
            if row[0] == search_id:
                row[3] = new_salary
                updated = True

            employees.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employees)

    if updated:
        print("Salary Updated Successfully.\n")
    else:
        print("Employee Not Found.\n")


# Menu
create_file()

while True:

    print("========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice\n")