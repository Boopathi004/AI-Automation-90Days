import csv

employee_id = input("Enter Employee ID : ")

with open("employee_data.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    found = False

    for row in reader:

        if row[0] == employee_id:
            print("\nEmployee Found")
            print(row)
            found = True
            break

    if not found:
        print("Employee Not Found")