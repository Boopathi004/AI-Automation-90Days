import time


employees = [
    {"id": 101, "name": "Boopathi", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Arun", "department": "HR", "salary": 45000},
    {"id": 103, "name": "Kumar", "department": "IT", "salary": 55000},
    {"id": 104, "name": "Ravi", "department": "Finance", "salary": 48000},
    {"id": 105, "name": "Priya", "department": "IT", "salary": 60000}
]


def employee_generator(employees):

    for employee in employees:
        yield employee


def execution_logger(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        print(f"\nStarting: {func.__name__}")

        try:
            result = func(*args, **kwargs)
            return result

        except Exception as error:
            print(f"Error: {error}")

        finally:
            end_time = time.time()

            print(f"Completed: {func.__name__}")
            print(
                f"Execution Time: "
                f"{end_time - start_time:.4f} seconds"
            )

    return wrapper


@execution_logger
def process_employees(employees):

    total_employees = 0
    total_salary = 0
    highest_salary = 0
    highest_employee = ""

    departments = {}

    print("\n================================")
    print("    EMPLOYEE DATA PROCESSING")
    print("================================")

    for employee in employee_generator(employees):

        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: ₹{employee['salary']}"
        )

        total_employees += 1
        total_salary += employee["salary"]

        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_employee = employee["name"]

        department = employee["department"]

        if department not in departments:
            departments[department] = 0

        departments[department] += 1

    average_salary = total_salary / total_employees

    print("\n================================")
    print("        EMPLOYEE REPORT")
    print("================================")

    print(f"Total Employees : {total_employees}")
    print(f"Total Salary    : ₹{total_salary}")
    print(f"Average Salary  : ₹{average_salary:.2f}")
    print(f"Highest Salary  : {highest_employee} - ₹{highest_salary}")

    print("\n================================")
    print("      DEPARTMENT ANALYTICS")
    print("================================")

    for department, count in departments.items():
        print(f"{department}: {count} employees")


process_employees(employees)