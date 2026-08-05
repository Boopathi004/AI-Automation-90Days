import csv
from datetime import date
joining_date=date.today()
employees = [
    [101, "Boopathi", "IT", 50000,"boopathi17ucsb007@gmail.com",joining_date],
    [102, "Ram", "HR", 45000,"ram@gmail.com",joining_date],
    [103, "Arjun", "Sales", 55000,"donr123@gmail.com",joining_date],
    [104, "Priya", "Finance", 60000,"resr@gmail.com",joining_date],
    [105, "John", "Support", 40000,"john@gmail.com",joining_date]
]

with open("employee_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID","Name","Department","Salary","Email","joining Date"])

    writer.writerows(employees)

print("Employee CSV Generated Successfully")

# Read CSV
with open("employee_data.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)