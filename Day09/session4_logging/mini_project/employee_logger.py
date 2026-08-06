import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

employees = []

print("=" * 50)
print("EMPLOYEE LOGGER SYSTEM")
print("=" * 50)

while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    try:

        if choice == "1":
    
            emp_id = int(input("Employee ID: "))
            name = input("Employee Name: ")
            department = input("Department: ")
            salary = float(input("Salary: "))

            employee = {
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": salary
            }

            employees.append(employee)

            logging.info(f"Employee Added -> {employee}")

            print("\nEmployee Added Successfully!")

        elif choice == "2":

            print("\nEmployee List")

            for emp in employees:
                print(emp)

            logging.info("Viewed Employee List")

        elif choice == "3":

            logging.info("Application Closed")

            print("Good Bye!")

            break

        else:

            raise ValueError("Invalid Menu Option")

    except Exception as e:

        logging.exception("Program Error")

        print("Error:", e)