import csv

employee = [
    input("ID : "),
    input("Name : "),
    input("Department : "),
    input("Salary : "),
    input("Email : "),
    input("Joining Date : ")
]

with open("employee_data.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(employee)

print("Employee Added Successfully")