import requests # type: ignore


BASE_URL = "https://jsonplaceholder.typicode.com/users"


# ==========================================================
# GET ALL EMPLOYEES
# ==========================================================

def get_all_employees():

    try:

        response = requests.get(BASE_URL, timeout=10)

        response.raise_for_status()

        employees = response.json()

        print("\n========== ALL EMPLOYEES ==========")

        for employee in employees:

            print(
                f"ID: {employee['id']} | "
                f"Name: {employee['name']} | "
                f"Username: {employee['username']} | "
                f"Email: {employee['email']}"
            )

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.HTTPError as error:

        print("❌ HTTP Error:", error)

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)

    except ValueError:

        print("❌ Invalid JSON response.")


# ==========================================================
# SEARCH EMPLOYEE
# ==========================================================

def search_employee():

    employee_id = input("Enter Employee ID: ")

    url = f"{BASE_URL}/{employee_id}"

    try:

        response = requests.get(url, timeout=5)

        response.raise_for_status()

        employee = response.json()

        print("\n========== EMPLOYEE FOUND ==========")

        print("ID       :", employee["id"])
        print("Name     :", employee["name"])
        print("Username :", employee["username"])
        print("Email    :", employee["email"])

    except requests.exceptions.HTTPError:

        if response.status_code == 404:

            print("❌ Employee not found.")

        else:

            print("❌ HTTP Error:", response.status_code)

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)

    except ValueError:

        print("❌ Invalid JSON response.")


# ==========================================================
# CREATE EMPLOYEE
# ==========================================================

def create_employee():

    name = input("Enter Employee Name: ")
    username = input("Enter Username: ")
    email = input("Enter Email: ")

    data = {

        "name": name,
        "username": username,
        "email": email

    }

    try:

        response = requests.post(
            BASE_URL,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        employee = response.json()

        print("\n========== EMPLOYEE CREATED ==========")

        print("ID       :", employee.get("id"))
        print("Name     :", employee.get("name"))
        print("Username :", employee.get("username"))
        print("Email    :", employee.get("email"))

        print("\n✅ Employee created successfully.")

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.HTTPError as error:

        print("❌ HTTP Error:", error)

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)


# ==========================================================
# UPDATE EMPLOYEE
# ==========================================================

def update_employee():

    employee_id = input("Enter Employee ID to update: ")

    name = input("Enter New Name: ")
    username = input("Enter New Username: ")
    email = input("Enter New Email: ")

    data = {

        "name": name,
        "username": username,
        "email": email

    }

    url = f"{BASE_URL}/{employee_id}"

    try:

        response = requests.put(
            url,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        employee = response.json()

        print("\n========== EMPLOYEE UPDATED ==========")

        print("ID       :", employee.get("id"))
        print("Name     :", employee.get("name"))
        print("Username :", employee.get("username"))
        print("Email    :", employee.get("email"))

        print("\n✅ Employee updated successfully.")

    except requests.exceptions.HTTPError:

        if response.status_code == 404:

            print("❌ Employee not found.")

        else:

            print("❌ HTTP Error:", response.status_code)

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)


# ==========================================================
# DELETE EMPLOYEE
# ==========================================================

def delete_employee():

    employee_id = input("Enter Employee ID to delete: ")

    confirm = input(
        "Are you sure you want to delete this employee? (yes/no): "
    )

    if confirm.lower() != "yes":

        print("❌ Delete operation cancelled.")

        return

    url = f"{BASE_URL}/{employee_id}"

    try:

        response = requests.delete(
            url,
            timeout=5
        )

        response.raise_for_status()

        print("\n✅ Employee deleted successfully.")

        print("Status Code:", response.status_code)

    except requests.exceptions.HTTPError:

        if response.status_code == 404:

            print("❌ Employee not found.")

        else:

            print("❌ HTTP Error:", response.status_code)

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)


# ==========================================================
# EMPLOYEE SUMMARY
# ==========================================================

def employee_summary():

    try:

        response = requests.get(BASE_URL, timeout=5)

        response.raise_for_status()

        employees = response.json()

        total_employees = len(employees)

        print("\n========== EMPLOYEE SUMMARY ==========")

        print("Total Employees:", total_employees)

        if total_employees > 0:

            print(
                "First Employee:",
                employees[0]["name"]
            )

            print(
                "Last Employee:",
                employees[-1]["name"]
            )

    except requests.exceptions.Timeout:

        print("⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:

        print("🌐 Unable to connect to the API.")

    except requests.exceptions.RequestException as error:

        print("❌ API Error:", error)


# ==========================================================
# MAIN MENU
# ==========================================================

def main():

    while True:

        print("\n")
        print("=" * 45)
        print("       EMPLOYEE API MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. View All Employees")
        print("2. Search Employee")
        print("3. Create Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Employee Summary")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            get_all_employees()

        elif choice == "2":

            search_employee()

        elif choice == "3":

            create_employee()

        elif choice == "4":

            update_employee()

        elif choice == "5":

            delete_employee()

        elif choice == "6":

            employee_summary()

        elif choice == "7":

            print("\n👋 Thank you for using Employee API System.")

            break

        else:

            print("\n❌ Invalid option. Please try again.")


# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":

    main()