import time

def employee_generator():
    employees = [
        {"id": 101, "name": "Boopathi", "salary": 50000},
        {"id": 102, "name": "Arun", "salary": 45000},
        {"id": 103, "name": "Kumar", "salary": 55000},
        {"id": 104, "name": "Ravi", "salary": 48000},
        {"id": 105, "name": "Priya", "salary": 60000}
    ]

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

            execution_time = end_time - start_time

            print(f"Completed: {func.__name__}")
            print(f"Execution Time: {execution_time:.4f} seconds")

    return wrapper

@execution_logger
def process_employees():

    employees = employee_generator()
    print("=== Employee Data Processing ===")

    for employee in employees:

        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Salary: {employee['salary']}" 
        )
    print("=== Employee Report ===")

    employee_generator()
    print(

         f"total employees: {len(list(employee_generator()))}\n"
         f"total salary: {sum(emp['salary'] for emp in employee_generator())}\n"
         f"average salary: {sum(emp['salary'] for emp in employee_generator()) / len(list(employee_generator()))}\n"
         f"highest salary: {max(emp['salary'] for emp in employee_generator())}\n"

        )
      

process_employees()