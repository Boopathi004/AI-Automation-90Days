import requests # type: ignore


print("Welcome to Employee Management System")

print("1. Get All Employees")
print("2. Get Employee by ID")
print("3. Create Employee")
print("4. Exit")
print("Requests Version:", requests.__version__)

if __name__ == "__main__":
    choice = input("Enter your choice: ")

    if choice == "1":
        url = "https://jsonplaceholder.typicode.com/users"

        response = requests.get(url)

        print("Status Code:", response.status_code)
        print(response.json())

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

        response = requests.get(url)

        print("Status Code:", response.status_code)
        print(response.json())

    elif choice == "3":
        url = "https://jsonplaceholder.typicode.com/users"

        emp_name = input("Enter Employee Name: ")
        emp_username = input("Enter Employee Username: ")
        emp_email = input("Enter Employee Email: ")

        data = {
            "name": emp_name,
            "username": emp_username,
            "email": emp_email
        }

        response = requests.post(url, json=data)

        print("Status Code:", response.status_code)
        print(response.json())

    elif choice == "4":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")