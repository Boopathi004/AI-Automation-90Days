import requests # type: ignore


BASE_URL = "https://jsonplaceholder.typicode.com/users"


def get_all_employees():
    """Get all employees from the API."""

    try:
        response = requests.get(BASE_URL, timeout=5)

        response.raise_for_status()

        employees = response.json()

        print("\n========== ALL EMPLOYEES ==========")

        for employee in employees:
            print(
                f"ID: {employee['id']} | "
                f"Name: {employee['name']} | "
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


def search_employee():
    """Search employee by ID."""

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


def main():

    while True:

        print("\n========================================")
        print("       SAFE EMPLOYEE API CLIENT")
        print("========================================")

        print("1. Get All Employees")
        print("2. Search Employee")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            get_all_employees()

        elif choice == "2":

            search_employee()

        elif choice == "3":

            print("👋 Exiting Employee API Client...")
            break

        else:

            print("❌ Invalid option. Please try again.")


main()