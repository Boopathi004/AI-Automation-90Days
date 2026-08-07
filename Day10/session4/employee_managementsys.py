from database import *
from reports import *
from logger import logger

create_table()
print("Table Created Successfully!")

while True:

    print("Add the employee details First")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. move to next Reports & filters Section")
    print("5. To view more employees details and updates")

    option=input("Enter Option : ")

    if option=="1":
        name = input("Enter Employee Name : ")
        department = input("Enter Department : ")
        salary = float(input("Enter Salary : "))
        join_date = input("Enter Joining Date : ")
        phone = input("Enter Phone Number : ")
        email = input("Enter Email : ")

        add_employee(name, department, salary, join_date, phone, email)
        logger.info(f"Employee Added -> {name}, {department}, {salary}, {join_date}, {phone}, {email}")
        print("\n✅ Employee Added Successfully!")
        continue

    elif option=="2":

        view_employees()
        logger.info("Viewed Employees")
        

    elif option=="3":

        emp_id = int(input("Enter Employee ID : "))
        new_salary = float(input("Enter New Salary : "))

        update_salary(emp_id, new_salary)
        logger.info(f"Salary Updated -> ID: {emp_id}, New Salary: {new_salary}")
        print("\n✅ Salary Updated Successfully!")
        continue    
    elif option=="4":
        pass
    elif option=="5":
        continue
    else:
        print("\n❌ Invalid Option. Please try again.")

    print("\n========== EMPLOYEE MANAGEMENT ==========")
    print("1. Highest Salary")
    print("2. Lowest Salary")
    print("3. Average Salary")
    print("4. Total Salary")
    print("5. Total Employees")
    print("6. Department Report")
    print("7. Salary > Amount")
    print("8. Sort Salary")
    print("9. Exit")

    choice = input("Enter Choice : ")

    try:

        if choice == "1":
            highest_salary()
            logger.info("Viewed Highest Salary")

        elif choice == "2":
            lowest_salary()
            logger.info("Viewed Lowest Salary")

        elif choice == "3":
            average_salary()
            logger.info("Viewed Average Salary")

        elif choice == "4":
            total_salary()
            logger.info("Viewed Total Salary")

        elif choice == "5":
            total_employee()
            logger.info("Viewed Total Employees")

        elif choice == "6":
            department_report()
            logger.info("Viewed Department Report")

        elif choice == "7":
            amount = float(input("Enter Salary : "))
            salary_filter(amount)
            logger.info("Salary Filter Used")

        elif choice == "8":
            sort_salary()
            logger.info("Sorted Salary")

        elif choice == "9":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        logger.error(str(e))
        print("Error :", e)