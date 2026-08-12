import time


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
def generate_employee_report():

    print("Generating employee report...")

    for i in range(1, 6):

        print(f"Processing employee {i}")

        time.sleep(0.5)


generate_employee_report()